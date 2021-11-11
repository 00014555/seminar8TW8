t0 = 'a'
t1 = 'a',
t2 = tuple()
t3 = tuple('lupins')
print(type(t1))
print(type(t0))
print(t2)
print(t3)
print(t3[0])
print(t3.index('u'))
print(t3[1:3])
t3 = ('A',)+t3[1:]
print(t3)
t4 = tuple('next')
print(t4)
t4 = ('t',)+t4[1:]
print(t4)
if (0,1,2)<(1,2,3):
    print("True")
else:
    print("False")
    #Task1
if ('00014555', 20, 'Tashkent' ) < ('00013444', 21, 'Tashkent'):
    print("True")
else:
    print("False")
a = 10
b = 55
a,b = b,a
print(a,b)
addr = "info@wiut.uz"
uname, domain = addr.split('@')
print(uname)
print(domain)
def printall(*args):
 print(args)
printall(1, 2.0, '3')
s = tuple('wiut')
n = (1,2,3,4)
new = zip(s,n)
for pair in new:
    print(pair)
#newList = list(new)
newList = list(zip(s,n))
print(newList)
def has_match(t1, t2):
   for x, y in zip(t1, t2):
     if x == y:
       return True
     else:
       return False
