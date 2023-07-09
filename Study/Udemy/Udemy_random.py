import random

print(random.random())
print(random.randint(1, 10))
print(random.choice('abcd'))
print(random.choice(('fast', 'test', 'new')))
print(random.choices(('fast', 'test', 'new'), k=3))
my_list = ['fast', 'test', 'new']
random.shuffle(my_list)
print(my_list)
random.shuffle(my_list)
print(my_list)
