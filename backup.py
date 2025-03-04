import os
import winreg  # For registry access
import time
import sys
from pathlib import Path

def export_registry_to_file(registry_path, output_file):
    """Export a registry key to a text file using reg export."""
    # Use reg export command via os.system (simpler than parsing with winreg)
    command = f'reg export "{registry_path}" "{output_file}" /y'
    result = os.system(command)
    if result == 0:
        return True
    else:
        print(f"Error exporting registry: {result}")
        return False

def find_ventoy_drive():
    """Find the Ventoy flash drive by its volume name."""
    for drive in range(ord('A'), ord('Z') + 1):
        drive_letter = chr(drive) + ":\\"
        if os.path.exists(drive_letter):
            try:
                volume_name = os.popen(f'vol {drive_letter[:-1]}').read().strip()
                if "Ventoy" in volume_name:
                    return drive_letter
            except Exception:
                continue
    return None

def main():
    # Registry path to backup
    registry_path = r"HKEY_LOCAL_MACHINE\SOFTWARE\7-Zip"
    backup_filename = "yasser_backup.txt"

    # Wait for Ventoy drive to be inserted
    print("Please insert your Ventoy flash drive...")
    while True:
        ventoy_path = find_ventoy_drive()
        if ventoy_path:
            break
        time.sleep(2)  # Check every 2 seconds

    # Full path for the backup file on Ventoy
    backup_path = os.path.join(ventoy_path, backup_filename)

    # Check if backup already exists
    if os.path.exists(backup_path):
        print("Backup already taken.")
        input("Press Enter to close...")
        sys.exit(0)

    # Export the registry key to the file
    if export_registry_to_file(registry_path, backup_path):
        print(f"Backup successfully saved to {backup_path}")
    else:
        print("Backup failed.")

    # Wait for user to press Enter before closing
    input("Press Enter to close...")

if __name__ == "__main__":
    main()