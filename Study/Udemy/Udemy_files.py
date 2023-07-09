from pathlib import Path

file_path = Path('text.txt')

atrs_path = [a for a in dir(file_path) if not a.startswith('_')]

print(Path.cwd())  # absolute path from Class
print(Path('C:/').joinpath('folder').joinpath('workfolder'))  # make root
print(Path('Udemy_1.py').exists())  # local file exist?
print(Path('D:/100').exists())  # root exist?

print(Path('E:/pythonProject_ii_bd/python/Study/Udemy').is_file())
print(Path('E:/pythonProject_ii_bd/python/Study/Udemy').is_dir())
print(Path('../Udemy/test.txt').is_file())
print(Path('../Udemy').is_dir())

for f in Path('.').iterdir():
    print(f)

django = Path('D:/django')
if not django.exists():
    django.mkdir()

if django.exists():
    django.rmdir()

if Path('new_d.txt').exists():
    Path('new_d.txt').unlink()    # deleting file

