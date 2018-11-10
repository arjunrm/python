def add(num1, num2):
    print(num1 + num2)

try:
    add(5, 10)
except:
    print("Exception occured")
else:
    print("Works")

try:
    num = input('Enter Line no: ')
    print(num)
    f = open('testfile', 'r')
    f.seek(2)
    f.write(num + '\n')
except TypeError:
    print("There was a type error!")
except OSError:
    print("There was an OS Error!")
else:
    f.seek(0)
    print(f.name + ' Contents:')
    print(f.read())
finally:
    print("I always run")
    f.close()
