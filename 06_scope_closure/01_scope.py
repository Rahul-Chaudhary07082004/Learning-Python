# closure 
# a closure happens when:
# 1. an outer function creates a variable
# 2. an inner function uses that variable
# 3. the inner function is returned or otherwise survives after that outer function finishes 

def chaicode(num):
    def chai(x):
        return x ** num
    return chai

f = chaicode(2)
g = chaicode(3)

print(f(3))
print(g(3))

# scope = means where a variable can be accessed in your program

x = "global"
def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print(x)
    inner()
outer()