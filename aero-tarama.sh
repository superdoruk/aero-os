#!/bin/bash
echo "================================"
echo "   AERO OS — Antivirüs Tarama"
echo "================================"
echo ""
echo "  1) Hızlı tarama (Ana klasör)"
echo "  2) Tam tarama (Tüm sistem)"
echo "  3) Çıkış"
echo ""
read -p "Seçiminiz (1/2/3): " secim

if [ "$secim" = "1" ]; then
    echo ""
    echo "Hızlı tarama başlıyor..."
    clamscan -r --bell ~/
elif [ "$secim" = "2" ]; then
    echo ""
    echo "Tam tarama başlıyor (uzun sürebilir)..."
    sudo clamscan -r --bell /
elif [ "$secim" = "3" ]; then
    echo "Çıkılıyor..."
else
    echo "Geçersiz seçim!"
fi
