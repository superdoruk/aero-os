# AEROTB Kullanım Kılavuzu

AEROTB (Aero Terminal Based) — güç kullanıcıları için terminal öncelikli mod.

## Temel Komutlar

### AERO Scriptleri
- `bash ~/aero-ayarlar.sh` — AERO ayarlar menüsü
- `bash ~/aero-mod-gecis.sh` — AEROEG/AEROTB geçişi
- `bash ~/aero-tarama.sh` — antivirüs tarama
- `bash ~/aero-taskbar.sh` — task bar konumu
- `python3 ~/aero-izin.py` — izin yöneticisi

### Sistem
- `sudo apt install <paket>` — uygulama kur
- `sudo apt remove <paket>` — uygulama kaldır
- `sudo apt update` — paket listesi güncelle
- `sudo apt upgrade` — sistemi güncelle
- `df -h` — disk kullanımı
- `free -h` — RAM kullanımı
- `top` — çalışan işlemler

### Dosya Yönetimi
- `ls` — dosyaları listele
- `cd <klasor>` — klasöre gir
- `mkdir <isim>` — klasör oluştur
- `rm <dosya>` — dosya sil
- `cp <kaynak> <hedef>` — dosya kopyala
- `mv <kaynak> <hedef>` — dosya taşı

### Flatpak
- `flatpak install <uygulama>` — uygulama kur
- `flatpak list` — kurulu uygulamalar
- `flatpak run <uygulama>` — uygulama çalıştır

### Firejail
- `firejail <uygulama>` — sandbox içinde çalıştır
