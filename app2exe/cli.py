# app2exe/cli.py
import argparse
import sys
import subprocess
import os
import shutil
import platform

def main():
    parser = argparse.ArgumentParser(description="app2exe: Python betiklerinizi hızlıca executable yapar.")
    parser.add_argument("script", help="Paketlenecek ana Python dosyasının yolu (.py)")
    parser.add_argument("-n", "--name", help="Oluşturulacak dosyanın adı")
    parser.add_argument("-i", "--icon", help="Uygulama ikonu (.ico / .icns)")
    parser.add_argument("--clean", action="store_true", help="Derleme sonrası geçici dosyaları temizler")

    args = parser.parse_args()

    if not os.path.exists(args.script):
        print(f"❌ [app2exe] Hata: '{args.script}' dosyası bulunamadı!")
        return

    # Çıktı ismi belirleniyor
    output_name = args.name if args.name else os.path.splitext(os.path.basename(args.script))[0]
    
    print(f"📦 [app2exe] {args.script} analiz ediliyor... (Sistem: {platform.system()})")
    
    # Temel PyInstaller komutu
    cmd = ["pyinstaller", "--onefile", f"--name={output_name}", args.script]
    
    # --- MAC İÇİN ÖZEL PARAMETRE ---
    if platform.system() == "Darwin":  # macOS algılandıysa
        cmd.append("--windowed")  # .app uzantılı Mac paketi oluşturmasını söyler
    
    if args.icon:
        cmd.extend(["--icon", args.icon])
        
    try:
        subprocess.run(cmd, check=True)
        print("🚀 [app2exe] İşlem başarıyla tamamlandı!")
        
        # --- TEMİZLİK BÖLÜMÜ ---
        if args.clean:
            print("🧹 [app2exe] Geçici dosyalar temizleniyor...")
            if os.path.exists("build"):
                shutil.rmtree("build")
            spec_file = f"{output_name}.spec"
            if os.path.exists(spec_file):
                os.remove(spec_file)
            print("✨ [app2exe] Temizlik tamamlandı.")
            
    except subprocess.CalledProcessError:
        print("❌ [app2exe] Derleme sırasında bir hata oluştu.")

if __name__ == "__main__":
    main()