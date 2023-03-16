import re
import os
import shutil

main_folder = r"C:\Users\Usuario\Desktop\Nanatsu-No-Taizai\compacted-files"

def main():
    for root, dirs, files in os.walk(main_folder):
        iterate_files(root, dirs, files)
        
def rename_file(file, root):
    new_file_name = rarToCbr(file)
    
    old_file_full_path = os.path.join(root, file)
    new_file_full_path = os.path.join(root, new_file_name)
    
    print(f'Convertendo arquivo "{file}" para "{new_file_name}')
    shutil.move(old_file_full_path, new_file_full_path)
        
def rarToCbr(file):
    f_name, f_extension = os.path.splitext(file)
    f_name_numbers = re.findall(r'\d+', f_name)
    
    return f'{f_name}.cbr'
        
def iterate_files(root, dirs, files):
    for file in files:
        if re.search(r'\.rar$', file):
            rename_file(file, root)
    