"""
Lesson 19: Automation and Scripting
Golden Source Solution: Automated Backup Script

This script demonstrates file system automation:
1. Scanning a directory
2. Creating a timestamped backup folder
3. Copying files
4. Logging actions
5. Reporting summary
"""
import os
import shutil
import datetime
from pathlib import Path

def create_dummy_files(source_dir):
    """Helper to create some dummy files to back up."""
    if not os.path.exists(source_dir):
        os.makedirs(source_dir)
    
    for i in range(1, 6):
        with open(os.path.join(source_dir, f"doc_{i}.txt"), "w") as f:
            f.write(f"This is the content of document {i}. Important data!")
    print(f"Created dummy files in '{source_dir}'")

def backup_files(source_dir, backup_root):
    """
    Backs up files from source_dir to a timestamped folder in backup_root.
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_folder_name = f"backup_{timestamp}"
    dest_dir = os.path.join(backup_root, backup_folder_name)
    
    # Create backup directory
    try:
        os.makedirs(dest_dir)
        print(f"Created backup directory: {dest_dir}")
    except OSError as e:
        print(f"Error creating directory: {e}")
        return

    log_file_path = os.path.join(dest_dir, "backup_log.txt")
    files_copied = 0
    total_size = 0

    print("Starting backup...")
    
    with open(log_file_path, "w") as log:
        log.write(f"Backup Log - {timestamp}\n")
        log.write("=" * 30 + "\n")

        # Iterate through files in source
        source_path = Path(source_dir)
        if not source_path.exists():
            print(f"Source directory '{source_dir}' does not exist!")
            return

        for item in source_path.iterdir():
            if item.is_file():
                try:
                    # Copy file
                    shutil.copy2(item, dest_dir)
                    
                    # Gather stats
                    size = item.stat().st_size
                    total_size += size
                    files_copied += 1
                    
                    # Log
                    log_entry = f"Copied: {item.name} ({size} bytes)\n"
                    log.write(log_entry)
                    print(f"  -> Backed up: {item.name}")
                    
                except Exception as e:
                    err_msg = f"Failed to copy {item.name}: {e}\n"
                    log.write(err_msg)
                    print(f"  !! Error: {err_msg.strip()}")

        # Write summary to log
        log.write("=" * 30 + "\n")
        log.write(f"Total Files: {files_copied}\n")
        log.write(f"Total Size: {total_size} bytes\n")
        log.write(f"Completed at: {datetime.datetime.now().isoformat()}\n")

    print("\n=== Backup Summary ===")
    print(f"Backup Location: {dest_dir}")
    print(f"Files Copied:    {files_copied}")
    print(f"Total Size:      {total_size} bytes")
    print(f"Log File:        {log_file_path}")

def main():
    # Setup paths
    base_dir = "Python-Learner/golden_source/L19"
    source_folder = os.path.join(base_dir, "my_documents")
    backup_folder = os.path.join(base_dir, "backups")

    # 1. Ensure we have something to backup
    create_dummy_files(source_folder)

    # 2. Run the backup
    backup_files(source_folder, backup_folder)

if __name__ == "__main__":
    main()
