# WinReg_Backup
back up specific registry keys from windows using flash drive status 
Registry Backup to Ventoy Flash Drive

This Python script automates backing up the Windows registry key HKEY\_LOCAL\_MACHINE\\SOFTWARE\\7-Zip to a text file named yasser\_backup.txt, saving it to a flash drive labeled "Ventoy" when inserted. If the backup file already exists, it notifies the user and waits for an Enter key press to close.

Features

*   Exports the registry key HKEY\_LOCAL\_MACHINE\\SOFTWARE\\7-Zip to a text file.
    
*   Detects a flash drive named "Ventoy" and saves the backup there.
    
*   Checks for an existing yasser\_backup.txt and skips the backup if found.
    
*   Provides user feedback and waits for confirmation before closing.
    

Prerequisites

*   Operating System: Windows (tested on Windows 10/11).
    
*   Python: Version 3.x installed (download from [python.org](https://www.python.org/downloads/)).
    
*   Flash Drive: A USB drive with the volume label "Ventoy" (case-sensitive).
    
*   No additional Python packages required—uses built-in modules (os, winreg, time, sys, pathlib).
    

Installation

1.  Download the Script:
    
    *   Save the script as backup.py (or clone this repo if applicable).
        
2.  Ensure Python is Installed:
    
    *   Open a terminal and run python --version or python3 --version. Install Python if not present.
        
3.  Prepare Your Ventoy Drive:
    
    *   Insert your flash drive.
        
    *   Right-click it in File Explorer > Properties > Set the name to "Ventoy" (exact spelling).
        

Usage

1.  Run the Script:
    
    *   Double-click backup.py (if Python is associated with .py files), or
        
    *   Open a terminal, navigate to the script’s directory (cd path\\to\\script), and run:
        
        bash
        
            python backup.py
        
2.  Insert Ventoy Drive:
    
    *   Plug in your "Ventoy" flash drive when prompted.
        
3.  Follow Prompts:
    
    *   If yasser\_backup.txt exists on the drive, it’ll display:
        
            Backup already taken.
            Press Enter to close...
        
    *   If not, it’ll export the registry and save it:
        
            Backup successfully saved to E:\yasser_backup.txt
            Press Enter to close...
        

Script Details

*   File: backup.py
    
*   Registry Path: HKEY\_LOCAL\_MACHINE\\SOFTWARE\\7-Zip
    
*   Output File: yasser\_backup.txt on the Ventoy drive
    
*   Logic:
    
    *   Waits for the Ventoy drive to be detected.
        
    *   Checks for an existing backup file.
        
    *   Uses reg export to dump the registry key to a text file.
        
    *   Handles errors (e.g., registry export failures) with basic feedback.
        

Example Output

*   New Backup:
    
        Please insert your Ventoy flash drive...
        Backup successfully saved to E:\yasser_backup.txt
        Press Enter to close...
    
*   Existing Backup:
    
        Please insert your Ventoy flash drive...
        Backup already taken.
        Press Enter to close...
    

Troubleshooting

*   Ventoy Not Detected:
    
    *   Ensure the drive’s volume label is exactly "Ventoy" (check in File Explorer > Properties).
        
    *   Adjust the script’s if "Ventoy" in volume\_name line if the name varies (e.g., "Ventoy1").
        
*   Backup Fails:
    
    *   Run the script as Administrator (right-click > Run as administrator) if permissions block registry access.
        
    *   Check if HKEY\_LOCAL\_MACHINE\\SOFTWARE\\7-Zip exists (open regedit to verify).
        
*   Script Hangs:
    
    *   Ensure Python is correctly installed and associated with .py files.
        

Customization

*   Change Registry Path: Edit registry\_path = r"HKEY\_LOCAL\_MACHINE\\SOFTWARE\\7-Zip" to another key.
    
*   Change Filename: Modify backup\_filename = "yasser\_backup.txt" to your preference.
    
*   Change Drive Name: Update "Ventoy" in find\_ventoy\_drive() to match your drive’s label.
    

Potential Extensions

*   TrueNAS Integration: Copy backups to a TrueNAS share using shutil.copy()—ask for details if interested!
    
*   Auto-Run: Set up a Windows scheduled task to trigger on USB insertion (requires additional setup).
