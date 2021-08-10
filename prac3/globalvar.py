a = 34
 

def f():
    print('Inside f() : ', a)
 

def g():   
    a = 16
    print('Inside g() : ', a)
 

def h():   
    global a
    a = 7
    print('Inside h() : ', a)
 

print('global : ',a)
f()
print('global : ',a)
g()
print('global : ',a)
h()
print('global : ',a)