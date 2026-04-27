#!/usr/bin/env python3
import os
import shutil

APPLICATIONS_DIR = "/usr/share/applications"
BACKUP_DIR = os.path.expanduser("~/.aero/desktop-backup")

def patch_desktop_files():
    os.makedirs(BACKUP_DIR, exist_ok=True)
    
    for filename in os.listdir(APPLICATIONS_DIR):
        if not filename.endswith(".desktop"):
            continue
            
        filepath = os.path.join(APPLICATIONS_DIR, filename)
        backup_path = os.path.join(BACKUP_DIR, filename)
        
        with open(filepath, 'r', errors='ignore') as f:
            content = f.read()
        
        # Zaten patch yapılmışsa atla
        if "aero-launcher" in content:
            continue
            
        # Backup al
        shutil.copy2(filepath, backup_path)
        
        # Exec satırını değiştir
        new_content = []
        for line in content.split('\n'):
            if line.startswith('Exec=') and 'aero-launcher' not in line:
                cmd = line[5:]  # "Exec=" sonrası
                line = f'Exec=aero-launcher {cmd}'
            new_content.append(line)
        
        # Kaydet
        with open(filepath, 'w') as f:
            f.write('\n'.join(new_content))
        
        print(f"✓ {filename} güncellendi")
    
    print("\nTüm uygulamalar AERO launcher'a bağlandı!")

patch_desktop_files()
