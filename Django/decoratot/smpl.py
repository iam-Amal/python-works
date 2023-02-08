'''
def sub(n1,n2):
    if n1<n2:
        (n1,n2)=(n2,n1)
    return n1-n2

def div(n1,n2):
    if n1<n2:
        (n1,n2)=(n2,n1)
    return n1/n2


print(sub(5,10))
print(div(2,10))
'''
# using a decorator

def dec(fn):
    def wrappr(n1,n2):
        if n1<n2:
            (n1,n2)=(n2,n1)
        return fn(n1,n2)
    return wrappr

@dec
def sub(n1,n2):

    return n1-n2

@dec
def div(n1,n2):
    return n1/n2


print(sub(5,10))
print(div(5,10))