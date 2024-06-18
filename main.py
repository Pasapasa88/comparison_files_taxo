import filecmp, os, re

def main(file_1, file_2):
    return filecmp.cmp(file_1, file_2, shallow=True)

def get_files_in_directory(directory):
  files = []
  for root, _, filenames in os.walk(directory):
    for filename in filenames:
        if '-definition.xml' in filename and '\\tab\\' in root:
            files.append(os.path.join(root.split(directory)[1], filename))
  return files

def merge_files(list_files1, list_files2,directory1,directory2):
    for x1 in list_files1:
        for x2 in list_files2:

            if  re.sub('\d{4}-\d{2}-\d{2}\\\\', '', x1) ==  re.sub('\d{4}-\d{2}-\d{2}\\\\', '', x2):
                print(f'Файл {x1} результат {main(directory1+x1, directory2+x2)}')

if __name__ == '__main__':
    directory1 = r'C:\Users\BuyanovPV\Desktop\Таксон\final_6_0\final_6_0\www.cbr.ru\xbrl\nso'
    directory2 = r'C:\Users\BuyanovPV\Desktop\Таксон\final_6\final_6\www.cbr.ru\xbrl\nso'
    file_list_1 = get_files_in_directory(directory1)
    file_list_2 = get_files_in_directory(directory2)
    merge_files(file_list_1,file_list_2,directory1,directory2)