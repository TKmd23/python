import zipfile
import os

folder_path = "E:\\pythonProject_ii_bd\\python\\Study"
zip_path = "E:\\pythonProject_ii_bd\\python\\Study\\test.zip"
zip_name = "test.zip"
my_zip = zipfile.ZipFile(zip_path, "w")
# my_zip.write("pars.txt", compress_type=zipfile.ZIP_DEFLATED, arcname="newname.txt")   # Pack 1 file

for folder, subfolder, files in os.walk(folder_path):
    print(folder, files)
    for file in files:
        if file == zip_name:
            continue
        my_zip.write(os.path.join(folder, file),
                     os.path.relpath(os.path.join(folder, file), folder_path),
                     compress_type=zipfile.ZIP_DEFLATED,
                     )


my_zip.close()
