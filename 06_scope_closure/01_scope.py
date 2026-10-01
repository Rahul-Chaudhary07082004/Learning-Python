# closure = a function that remembers and can access variables from its outer function even after that outer function has finished executing

def chaicode(num):
    def chai(x):
        return x ** num
    return chai

f = chaicode(2) # chaicode(num) = chaicode(2) = f
g = chaicode(3) # chaicode(num) = chaicode(3) = g

print(f(3)) # 9 chai(x) = f(3)
print(g(3)) # 27 chai(x) = g(3)

# scope = means where a variable can be accessed in your program

x = "global"
def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print(x)
    inner()
outer()