import decimal

a = 10
b = 3.14
c = 3
d = a ** 2

# a = 10.1
print (type(d)) # ** 符号是次方
print (d)

print (type (d/b)) # 一个int 除于 float 结果是 float

c = 2
print (type (a/c)) # 一个 int 除于 int 是 float
print (a/c)

## 总结

print ('------two int + - * always int------')
print (type (a+c),(a+c))
print (type (a-c),(a-c))
print (type (a*c),(a*c))
print (type (a/c),(a/c)) #但是如果是除的话无论是正除与否都是float
print ('------------')

print ('--one float with one int = float--')
print (type (b+c),(b+c))
print (type (b-c),(b-c))
print (type (b*c),(b*c))
print (type (b/c),(b/c))
print (type (b**c),round ((b**c),3),decimal.Decimal(b**c))
print ('------------')

print ()
