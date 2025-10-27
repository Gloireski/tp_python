for i in range(1, 51):
    s = ('Fizz' if i % 3 == 0 else '') + ('Buzz' if i % 5 == 0 else '')
    print(s or i)