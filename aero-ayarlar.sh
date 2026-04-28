#!/bin/bash
clear
echo "================================"
echo "   AERO OS — Ayarlar"
echo "================================"
echo ""
echo "  Mevcut mod: $(cat ~/.aero/mod.conf 2>/dev/null || echo 'AEROWS')"
echo ""
echo "  1) AEROWS moduna geç"
echo "  2) AEROUX moduna geç"
echo "  3) İzin yöneticisi aç/kapat"
echo "  4) Task bar konumu değiştir"
echo "  5) Antivirüs tarama"
echo "  6) Çıkış"
echo ""
read -p "  Seçiminiz: " secim

case $secim in
    1)
        echo "AEROWS" > ~/.aero/mod.conf
        echo "✓ AEROWS moduna geçildi!"
        ;;
    2)
        echo "AEROUX" > ~/.aero/mod.conf
        echo "✓ AEROUX moduna geçildi!"
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
