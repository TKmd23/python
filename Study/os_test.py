import os

# print(os.name)  # nt  'str'
# print(os.environ)  # Получить сведения, которые касаются конфигурации компьютера 'dict'
# print(os.getenv(""))  # При помощи функции getenv можно получить доступ к различным переменным среды.
# print(os.getcwd())  # возвращает полный адрес рабочего каталога диске.
# os.chdir(r"D:\tester")   # переход к новой рабочей директории
# print(os.path.exists(r"E:\pythonProject_ii_bd\python\Study\Test1.py"))   # Проверка существования пути "bool"
# print(os.path.isfile(r"D:\test.txt"))
# print(os.path.isdir(r"D:\tester"))   # для проверки объекта на принадлежность к классу директорий "bool"
# os.mkdir(r"D:\tester\pyt")   # New folder
# os.makedirs(r"D:\tester\test\first")   # можно создавать сразу несколько новых папок в неограниченном количестве
# os.remove(r"D:\tester\test\test.txt")   # Remove file
# os.rmdir(r"D:\tester\test")   # Remove dir if its empty
# os.removedirs(r"D:\tester\test")   # удаления множества пустых папок
# os.startfile(r"D:\tester\test\test.txt")   # Запуск на исполнение
# print(os.path.getsize(r"D:\tester\test\test.txt"))   # Вычисление размера "int"
# os.rename(r"D:\folder", r"D:\catalog")   # Переименование
# print(os.listdir(r"D:\tester"))   # Содержимое директорий 'list'


# for root, directories, files in os.walk(r"D:\tester"):
#     print(root)
#     for directory in directories:
#         print(directory)
#     for file in files:
#         print(file)
# названиям и путям всех подпапок и файлов, относящихся к заданному каталогу

# print(os.stat(r"D:\tester\test\test.txt"))   # Информация о файлах и директориях
# print(os.path.split(r"D:\tester\test\test.txt"))   # Обработка путей  "tuple"
# print(os.path.join(r"D:\tester\test", "test.txt"))   # Обратное действие 'str'

