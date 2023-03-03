import os


def read_dir(root):
    tree = os.walk(root)
    for r, dirs, files in tree:
        level = r.count(os.sep) - 1
        tab = "-" * 4 * level
        sub_tab = "-" * 4 * (level + 1)
        print(f"{tab} [{os.path.basename(r)}]")
        for i in files:
            print(f"{sub_tab} {os.path.basename(i)}")

read_dir(r"D:\tester")
