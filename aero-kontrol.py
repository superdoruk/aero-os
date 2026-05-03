#!/usr/bin/env python3
import gi
import subprocess
import os
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class AeroKontrol(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="AERO OS — Kontrol Merkezi")
        self.set_default_size(500, 600)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_resizable(False)
        
        # Ana kutu
        ana = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        ana.set_margin_top(20)
        ana.set_margin_bottom(20)
        ana.set_margin_start(20)
        ana.set_margin_end(20)
        self.add(ana)
        
        # Başlık
        baslik = Gtk.Label()
        baslik.set_markup('<span font="18" color="#5DCAA5"><b>AERO Kontrol Merkezi</b></span>')
        ana.pack_start(baslik, False, False, 0)
        
        mod = open(os.path.expanduser("~/.aero/mod.conf")).read().strip() if os.path.exists(os.path.expanduser("~/.aero/mod.conf")) else "AEROEG"
        mod_label = Gtk.Label()
        mod_label.set_markup(f'<span color="#85B7EB">Aktif mod: {mod}</span>')
        ana.pack_start(mod_label, False, False, 0)
        
        ayirici = Gtk.Separator()
        ana.pack_start(ayirici, False, False, 5)
        
        # Mod değiştir
        self.buton_ekle(ana, " Mod Değiştir", self.mod_degistir, "#1D9E75")
        
        ayirici2 = Gtk.Separator()
        ana.pack_start(ayirici2, False, False, 5)
        
        # Sistem
        sistem_label = Gtk.Label()
        sistem_label.set_markup('<span color="#5DCAA5"><b>Sistem</b></span>')
        sistem_label.set_halign(Gtk.Align.START)
        ana.pack_start(sistem_label, False, False, 0)
        
        self.buton_ekle(ana, "Antivirüs Tarama", self.tarama)
        self.buton_ekle(ana, "Sistem Güncelle", self.guncelle)
        self.buton_ekle(ana, "Sistem Monitörü", self.monitor)
        
        ayirici3 = Gtk.Separator()
        ana.pack_start(ayirici3, False, False, 5)
        
        # Görünüm
        gorunum_label = Gtk.Label()
        gorunum_label.set_markup('<span color="#5DCAA5"><b>Görünüm</b></span>')
        gorunum_label.set_halign(Gtk.Align.START)
        ana.pack_start(gorunum_label, False, False, 0)
        
        self.buton_ekle(ana, "Task Bar Konumu", self.taskbar)
        self.buton_ekle(ana, "Wallpaper Değiştir", self.wallpaper)
        
        ayirici4 = Gtk.Separator()
        ana.pack_start(ayirici4, False, False, 5)
        
        # Güvenlik
        guvenlik_label = Gtk.Label()
        guvenlik_label.set_markup('<span color="#5DCAA5"><b>Güvenlik</b></span>')
        guvenlik_label.set_halign(Gtk.Align.START)
        ana.pack_start(guvenlik_label, False, False, 0)
        
        self.buton_ekle(ana, "İzin Yöneticisi", self.izin)
        
        self.connect("destroy", Gtk.main_quit)
        self.show_all()
    
    def buton_ekle(self, kutu, etiket, fonksiyon, renk=None):
        buton = Gtk.Button(label=etiket)
        buton.connect("clicked", fonksiyon)
        kutu.pack_start(buton, False, False, 0)
        return buton
    
    def mod_degistir(self, w):
        subprocess.Popen(["bash", "-c", "bash ~/aero-mod-gecis.sh"])
    
    def tarama(self, w):
        subprocess.Popen(["bash", "-c", "gnome-terminal -- bash ~/aero-tarama.sh"])
    
    def guncelle(self, w):
        subprocess.Popen(["bash", "-c", "gnome-terminal -- bash -c 'sudo apt update && sudo apt upgrade -y; read'"])
    
    def monitor(self, w):
        subprocess.Popen(["gnome-system-monitor"])
    
    def taskbar(self, w):
        subprocess.Popen(["bash", "-c", "bash ~/aero-taskbar.sh"])
    
    def wallpaper(self, w):
        subprocess.Popen(["bash", "-c", "nautilus ~/Pictures/AERO"])
    
    def izin(self, w):
        subprocess.Popen(["bash", "-c", "python3 ~/aero-izin.py"])

pencere = AeroKontrol()
Gtk.main()
