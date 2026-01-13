import os

def empty_clean_export_folder(files_to_spare: list[str] = []):
    clean_export = os.getenv("CLEAN_EXPORT")
    
    for filename in os.listdir(clean_export):
        if filename in files_to_spare:
            continue

        file_path = os.path.join(clean_export, filename)
        
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            # TODO: recursive subfolder removal
        except Exception as e:
            print(f'Failed to delete {file_path}\nReason:\n{e}')
    print(f'clean_export folder has been cleaned.')