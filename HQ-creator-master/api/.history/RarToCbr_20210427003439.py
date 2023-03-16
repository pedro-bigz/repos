import re
import os
import shutil

main_folder = r"C:\Users\Usuario\Desktop\Nanatsu-No-Taizai\compacted-files"

class ConversorCbr:
    def __init__(self):
        for root, dirs, files in os.walk(main_folder):
            self.root = root
            self.iterate_files(dirs, files)
            
    def rename_file(self, file, root):
        new_file_name = self.rarToCbr(file)
        
        old_file_full_path = os.path.join(root, file)
        new_file_full_path = os.path.join(root, new_file_name)
        
        print(f'Convertendo arquivo "{file}" para "{new_file_name}')
        shutil.move(old_file_full_path, new_file_full_path)
            
    def rarToCbr(file):
        f_name, f_extension = os.path.splitext(file)
        f_name_numbers = re.findall(r'\d+', f_name)
        
        return f'{f_name}.cbr'
            
    def iterate_files(self, root, dirs, files):
        for file in files:
            if re.search(r'\.rar$', file):
                self.rename_file(file, root)
        