#!/bin/bash
clear
echo "================================"
echo "   AERO OS — Ayarlar"
echo "================================"
echo ""
echo "  Mevcut mod: $(cat ~/.aero/mod.conf 2>/dev/null || echo 'AEROEG')"echo ""
echo "  1) AEROEG moduna geç"
echo "  2) AEROTB moduna geç"
echo "  3) İzin yöneticisi aç/kapat"
echo "  4) Task bar konumu değiştir"
echo "  5) Antivirüs tarama"
echo "  6) Çıkış"
echo ""
read -p "  Seçiminiz: " secim

case $secim in
    1)
        bash ~/aero-mod-gecis.sh
        echo "✓ AEROEG moduna geçildi!"
        ;;
    2)
        bash ~/aero-mod-gecis.sh
        echo "✓ AEROTB moduna geçildi!"
        ;;
    3)
        bash ~/aero-izin.py
        ;;
    4)
        bash ~/aero-taskbar.sh
        ;;
    5)
        bash ~/aero-tarama.sh
        ;;
    6)
        echo "Çıkılıyor..."
        exit 0
        ;;
    *)
        echo "Geçersiz seçim!"
        ;;
esac
