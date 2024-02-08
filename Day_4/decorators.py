def make_pretty(func):
    #import pdb;pdb.set_trace()
    print("Hello")
    def inner():
        #import pdb;pdb.set_trace()
        print("I got decorated")
        func()
    return inner

@make_pretty
def ordinary():
    print("I am ordinary")

ordinary()  