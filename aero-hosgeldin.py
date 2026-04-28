#!/usr/bin/env python3
import gi
import os
import subprocess
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf

class AeroHosgeldin(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="AERO OS")
        self.set_default_size(600, 400)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_resizable(False)
        self.maximize()
        self.set_decorated(False)
        screen = self.get_screen()
        self.resize(screen.get_width(), screen.get_height())
        self.move(0, 0)
        
        # Ana kutu
        kutu = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=20)
        kutu.set_margin_top(40)
        kutu.set_margin_bottom(40)
        kutu.set_margin_start(40)
        kutu.set_margin_end(40)
        self.add(kutu)
        
        # Hoş geldin yazısı
        kullanici = os.getenv("USER", "kullanıcı")
        hosgeldin = Gtk.Label()
        hosgeldin.set_markup(f'<span font="24" color="#5DCAA5"><b>Hoş geldin, {kullanici}! 👋</b></span>')
        kutu.pack_start(hosgeldin, False, False, 0)
        
        # AERO OS yazısı
        aero = Gtk.Label()
        aero.set_markup('<span font="14" color="#85B7EB">AERO OS — Sürüm 0.1 Alpha</span>')
        kutu.pack_start(aero, False, False, 0)
        
        # Ayırıcı
        ayirici = Gtk.Separator()
        kutu.pack_start(ayirici, False, False, 0)
        
        # Sistem bilgileri
        bilgi_kutu = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        
        # RAM
        ram = subprocess.getoutput("free -h | awk '/^Mem:/{print $2}'")
        ram_label = Gtk.Label()
        ram_label.set_markup(f'<span color="#D3D1C7">🖥️  RAM: {ram}</span>')
        ram_label.set_halign(Gtk.Align.START)
        bilgi_kutu.pack_start(ram_label, False, False, 0)
        
        # CPU
        cpu = subprocess.getoutput("cat /proc/cpuinfo | grep 'model name' | head -1 | cut -d: -f2").strip()
        cpu_label = Gtk.Label()
        cpu_label.set_markup(f'<span color="#D3D1C7">⚡  CPU: {cpu}</span>')
        cpu_label.set_halign(Gtk.Align.START)
        bilgi_kutu.pack_start(cpu_label, False, False, 0)
        
        # Mod
        mod = open(os.path.expanduser("~/.aero/mod.conf")).read().strip() if os.path.exists(os.path.expanduser("~/.aero/mod.conf")) else "AEROWS"
        mod_label = Gtk.Label()
        mod_label.set_markup(f'<span color="#D3D1C7">🔧  Mod: {mod}</span>')
        mod_label.set_halign(Gtk.Align.START)
        bilgi_kutu.pack_start(mod_label, False, False, 0)
        
        kutu.pack_start(bilgi_kutu, False, False, 0)
        
        # Ayırıcı
        ayirici2 = Gtk.Separator()
        kutu.pack_start(ayirici2, False, False, 0)
        
        # Butonlar
        buton_kutu = Gtk.Box(spacing=10)
        buton_kutu.set_halign(Gtk.Align.CENTER)
        
        ayarlar_btn = Gtk.Button(label="⚙️  Ayarlar")
        ayarlar_btn.connect("clicked", self.ayarlar_ac)
        buton_kutu.pack_start(ayarlar_btn, False, False, 0)
        
        kapat_btn = Gtk.Button(label="✓  Başla")
        kapat_btn.connect("clicked", Gtk.main_quit)
        buton_kutu.pack_start(kapat_btn, False, False, 0)
        
        kutu.pack_start(buton_kutu, False, False, 0)
        
        self.connect("destroy", Gtk.main_quit)
        self.show_all()
    
    def ayarlar_ac(self, widget):
        subprocess.Popen(["bash","-c", "bash ~/aero-ayarlar.sh"])

pencere = AeroHosgeldin()
Gtk.main()
