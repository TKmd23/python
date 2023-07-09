with open('test.txt') as test_file:
    print(test_file.read())

with open('test.txt') as test_file:
    for i in test_file.readlines():
        if i.endswith('\n'):
            print(i[:-2])
        else:
            print(i)

with open('test.txt', 'w') as test_file:
    test_file.write("Test fuccccccccccccccc\n")

with open('test.txt', 'a') as test_file:
    test_file.write("Second test line\n")
