import time
print('\033[1;34mTodos os números pares de 1 até 50')
for c in range(1, 51):
    if c % 2 == 0:
        print('\033[1;36m{}'.format(c))
        time.sleep(0.33)
