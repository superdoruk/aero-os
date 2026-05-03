#!/usr/bin/env python3
import gi
import subprocess
import os
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf

class AeroBaslat(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="AERO Başlatıcı")
        self.set_default_size(400, 500)
        self.set_position(Gtk.WindowPosition.CENTER)
        
        ana = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        ana.set_margin_top(15)
        ana.set_margin_bottom(15)
        ana.set_margin_start(15)
        ana.set_margin_end(15)
        self.add(ana)
        
        # Arama kutusu
        arama = Gtk.SearchEntry()
        arama.set_placeholder_text("Uygulama ara...")
        arama.connect("search-changed", self.ara)
        ana.pack_start(arama, False, False, 0)
        
        # Uygulama listesi
        self.liste = Gtk.ListBox()
        self.liste.set_selection_mode(Gtk.SelectionMode.SINGLE)
        
        scroll = Gtk.ScrolledWindow()
        scroll.add(self.liste)
        scroll.set_min_content_height(400)
        ana.pack_start(scroll, True, True, 0)
        
        # Uygulamalar
        # Tüm uygulamaları oku
        self.uygulamalar = []
        klasorler = [
            "/usr/share/applications",
            "/var/lib/snapd/desktop/applications",
            os.path.expanduser("~/.local/share/applications")
        ]
        
        for klasor in klasorler:
            if not os.path.exists(klasor):
                continue
            for dosya in os.listdir(klasor):
                if not dosya.endswith(".desktop"):
                    continue
                yol = os.path.join(klasor, dosya)
                try:
                    isim = ""
                    komut = ""
                    gizli = False
                    with open(yol, 'r', errors='ignore') as f:
                        for satir in f:
                            if satir.startswith("Name=") and not isim:
                                isim = satir[5:].strip()
                            if satir.startswith("Exec=") and not komut:
                                komut = satir[5:].strip()
                                komut = komut.replace("%u","").replace("%U","").replace("%f","").replace("%F","").strip()
                            if satir.startswith("NoDisplay=true"):
                                gizli = True
                    if isim and komut and not gizli:
                        self.uygulamalar.append((isim, komut))
                except:
                    continue
        
        self.uygulamalar.sort(key=lambda x: x[0])
        
        self.satırlar = []
        for isim, komut in self.uygulamalar:
            satir = Gtk.ListBoxRow()
            kutu = Gtk.Box(spacing=10)
            kutu.set_margin_top(8)
            kutu.set_margin_bottom(8)
            kutu.set_margin_start(10)
            etiket = Gtk.Label(label=isim)
            etiket.set_halign(Gtk.Align.START)
            kutu.pack_start(etiket, True, True, 0)
            satir.add(kutu)
            satir.komut = komut
            satir.isim = isim.lower()
            self.liste.add(satir)
            self.satırlar.append(satir)
        
        self.liste.connect("row-activated", self.ac)
        self.connect("destroy", Gtk.main_quit)
        self.show_all()
    
    def ara(self, widget):
        metin = widget.get_text().lower()
        for satir in self.satırlar:
            satir.set_visible(metin in satir.isim or metin == "")
    
    def ac(self, liste, satir):
        subprocess.Popen(["bash", "-c", satir.komut])
        self.destroy()
        Gtk.main_quit()

pencere = AeroBaslat()
Gtk.main()
