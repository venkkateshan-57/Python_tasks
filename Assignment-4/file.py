try:
    with open('sample.txt', 'r') as b:
        c=b.read()
        print(c)
except FileNotFoundError:
    print("There is no such file")
finally:
    print("Good Bye")