#Decorators in python

def decor(func):
    def wrap():
        print("---0----")
        func()
        print("---00---")
    return wrap

def print_text():
    print("Hello World!!")

decorated = decor(print_text)
decorated()

#output
#---0----
#Hello World!!
#---00---

