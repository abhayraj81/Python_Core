# casting python

# Explicit type casting (type Conversion)
a = 1
print(type(a))

b = "1"
print(type(b))

c = int(b)
print(type(c))

print(a+c)
print(a+int(b))

f1 = 23.65
f2 = int(f1)
print(f2)
print(type(f2))

int1 = 23
int2 = float(int1)
print(int2)
print(type(int2))

# implicit type casting (coercion)
var1 = 10
var2 = 11.5
var3 = var1 +var2
print(type(var3))
print(var3)

at = bool(1)
af = bool(0)
print(at)
print(type(at))
print(af)
print(type(af))