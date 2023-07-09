from zipfile import ZipFile
from pathlib import Path

my_dir = Path('test')
if not my_dir.exists():
    my_dir.mkdir()

# with open('test/first.txt', 'w') as my_file:
#     my_file.write('First file\n')
# with open('test/second.txt', 'w') as my_file:
#     my_file.write('Second file\n')

with ZipFile('my_zip.zip', mode='w') as my_zip:
    for file in my_dir.iterdir():
        my_zip.write(file)

with ZipFile('my_zip.zip') as my_zip:
    # my_zip.extractall('my-unzip')
    print(my_zip.compression)
