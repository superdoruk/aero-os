#!/bin/bash
SIMDIKI=$(cat ~/.aero/mod.conf 2>/dev/null || echo "AEROWS")

if [ "$SIMDIKI" = "AEROWS" ]; then
    # AEROUX'a gec
    echo "AEROUX" > ~/.aero/mod.conf
    echo "acik" > ~/.aero/izin_ayar.conf
    # Task bar sola al
    gnome-extensions enable ubuntu-dock@ubuntu.com
    gnome-extensions disable dash-to-panel@jderose9.github.com
    # Terminali goster
    rm -f ~/.local/share/applications/org.gnome.Terminal.desktop
    zenity --info --title="AERO OS" --text="AEROUX moduna gecildi!\nTerminal oncelikli mod aktif." --ok-label="Tamam"
else
    # AEROWS'a gec
    echo "AEROWS" > ~/.aero/mod.conf
    echo "kapali" > ~/.aero/izin_ayar.conf
    # Task bar alta al
    gnome-extensions disable ubuntu-dock@ubuntu.com
    gnome-extensions enable dash-to-panel@jderose9.github.com 2>/dev/null
    # Terminali gizle
    cp /usr/share/applications/org.gnome.Terminal.desktop ~/.local/share/applications/
    sed -i 's/OnlyShowIn=GNOME;Unity;/NotShowIn=GNOME;Unity;/' ~/.local/share/applications/org.gnome.Terminal.desktop
    update-desktop-database ~/.local/share/applications/
    zenity --info --title="AERO OS" --text="AEROWS moduna gecildi!\nGrafik mod aktif." --ok-label="Tamam"
fi
