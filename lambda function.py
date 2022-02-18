
x = lambda a : a + 10
print(x(5))

x= lambda a:a+20
print(x(5))

x= lambda a:a*5
print(x(5))

x=lambda a:a**2
print(x(2))

x = lambda a, b : a * b
print(x(5, 6))


x=lambda a,b:a+b
print(x(2,3))

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))


def myfunc(n):
  return lambda a : a * n
x=myfunc(2)
print(x(3))


def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))


def myfun(n):
    return lambda a:a+n
x=myfun(2)
y=myfun(3)
print(x(2))
print(y(3))

y=lambda x:x.swapcase()
print(y("python"))

y=lambda x:x.capitalize()
print(y("python"))