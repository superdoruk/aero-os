#!/bin/bash
echo "================================"
echo "   AERO OS — Task Bar Konumu"
echo "================================"
echo ""
echo "  1) Alt bar "
echo "  2) Sol dock "
echo ""
read -p "Seçiminiz (1/2): " secim

if [ "$secim" = "1" ]; then
    gnome-extensions enable dash-to-panel@jderose9.github.com
    gnome-extensions disable ubuntu-dock@ubuntu.com
    echo "✓ Task bar alta alındı!"
elif [ "$secim" = "2" ]; then
    gnome-extensions disable dash-to-panel@jderose9.github.com
    gnome-extensions enable ubuntu-dock@ubuntu.com
    echo "✓ Sol dock aktif!"
else
    echo "Geçersiz seçim!"
fi
