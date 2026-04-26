#!/usr/bin/env python3
import os

AYAR_DOSYASI = os.path.expanduser("~/.aero/izin_ayar.conf")

def ayar_oku():
    os.makedirs(os.path.dirname(AYAR_DOSYASI), exist_ok=True)
    if not os.path.exists(AYAR_DOSYASI):
        ayar_yaz("acik")
    with open(AYAR_DOSYASI, "r") as f:
        return f.read().strip()

def ayar_yaz(deger):
    os.makedirs(os.path.dirname(AYAR_DOSYASI), exist_ok=True)
    with open(AYAR_DOSYASI, "w") as f:
        f.write(deger)

def izin_sor(uygulama):
    durum = ayar_oku()
    if durum == "kapali":
        print(f"✓ İzin yöneticisi kapalı — '{uygulama}' açılıyor!")
        return True
    print("=" * 40)
    print("  AERO OS — İzin Yöneticisi")
    print("=" * 40)
    print(f"\n  '{uygulama}' çalışmak istiyor!")
    print("\n  1) İzin ver")
    print("  2) Reddet")
    print()
    secim = input("  Seçiminiz (1/2): ")
    if secim == "1":
        print(f"\n  ✓ '{uygulama}' için izin verildi!")
        return True
    else:
        print(f"\n  ✗ '{uygulama}' engellendi!")
        return False

def ayar_degistir():
    durum = ayar_oku()
    print(f"\n  Şu anki durum: {durum}")
    print("  1) Aç")
    print("  2) Kapat")
    secim = input("\n  Seçiminiz (1/2): ")
    if secim == "1":
        ayar_yaz("acik")
        print("  ✓ İzin yöneticisi açıldı!")
    elif secim == "2":
        ayar_yaz("kapali")
        print("  ✓ İzin yöneticisi kapatıldı!")

# Test
print("1) Uygulama aç")
print("2) Ayarları değiştir")
secim = input("\nSeçim: ")

if secim == "1":
    izin_sor("Firefox")
elif secim == "2":
    ayar_degistir()
