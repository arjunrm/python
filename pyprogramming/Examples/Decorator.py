def hello(name='Jose'):
    print("Hello {}".format(name))

    def greet():
        return '\t This is greet'
    
    def welcome():
        return '\t\t This is welcome'

    print(greet())
    print(welcome())
    print("End of hello()")

    return [greet, welcome]

def who_is_this(func):
    print("This is who is this")
    print(func())

returnedFuncs = hello()

for func in returnedFuncs:
    print(func())

who_is_this(returnedFuncs[0])

print('')
print('')

def new_decorator(org_func):
    def wrap_func():
        print('Extra code before orig func')
        org_func()
        print('After orig func')
    
    return wrap_func

@new_decorator
def func_needs_decorator():
    print('Func needs decorator')

#decorated_func = new_decorator(func_needs_decorator)

func_needs_decorator()

