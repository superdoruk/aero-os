#!/bin/bash
clear
echo "================================"
echo "   Hoş geldiniz - AERO OS"
echo "   Sürüm: 0.1 Alpha"
echo "   Geliştirici: AERO PC"
echo "================================"
echo ""
echo "Sistem Bilgisi"
echo "  Kullanıcı : $(whoami)"
echo "  Tarih     : $(date)"
echo "  Ram       : $(free -h | awk '/^Mem:/{print $2}')"
echo ""
echo "Mod seçin:"
echo "  1) AEROEG - Grafik mod"
echo "  2) AEROTB - Terminal mod"
echo ""
read -p "Seçiminiz (1/2): " mod

if [ "$mod" = "1" ]; then
    echo "AEROEG modu aktif - Hoş geldiniz!"
elif [ "$mod" = "2" ]; then
    echo "AEROTB modu aktif - Terminal hazır, Hoş geldiniz!"
else
    echo "N'apıyon mal!"
fi
