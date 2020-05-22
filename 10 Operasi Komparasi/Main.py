# Operasi Komparasi
# Setiap Hasil dari operasi tersebut adalah boolean (just true and false)

# >, <, >=, <=, ==, !=, is, is not
a = 4
b = 2
print("-- Lebih Besar Dari --")
# 1. > (lebih besar dari)
hasil = a > 3
print(a,'>',3,'=',hasil)
hasil = b > 3
print(b,'>',3,'=',hasil)
hasil = b > 2
print(b,'>',2,'=',hasil)

print("-- Kurang dari --")
# 2. < (Kurang dari)
hasil = a < 3
print(a,'<',3,'=',hasil)
hasil = b < 3
print(b,'<',3,'=',hasil)
hasil = b < 2
print(b,'<',2,'=',hasil)

print("-- Lebih besar dari sama dengan --")
# 3. >= (Lebih besar dari sama dengan)
hasil = a >= 3
print(a,'>=',3,'=',hasil)
hasil = b >= 3
print(b,'>=',3,'=',hasil)
hasil = b >= 2
print(b,'>=',2,'=',hasil)

print("-- Kurang dari sama dengan --")
# 4. >= (Kurang dari sama dengan)
hasil = a <= 3
print(a,'<=',3,'=',hasil)
hasil = b <= 3
print(b,'<=',3,'=',hasil)
hasil = b <= 2
print(b,'<=',2,'=',hasil)

print("-- Sama Dengan --")
# 5. == (Sama Dengan)
hasil = a == 4
print(a,'==',4,'=',hasil)
hasil = b == 4
print(b,'==',4,'=',hasil)

print("-- Tidak Sama Dengan --")
# 6. != (Tidak Sama Dengan)
hasil = a != 4
print(a,'!=',4,'=',hasil)
hasil = b != 4
print(b,'!=',4,'=',hasil)

print("-- Object Identity --") # 'is' sebagai komparasi object identity
# 7. iObject Identity (is)
x = 5 # assignment membuat object
y = 6
print('nilai x =',x,',id = ',hex(id(x)))
print('nilai y =',y,',id = ',hex(id(y)))
hasil = x is y
print('x is y =',hasil)

print("-- Object Identity --") # 'is not' sebagai komparasi object identity
# 7. Object Identity (is not)
x = 5 # assignment membuat object
y = 6
print('nilai x =',x,',id = ',hex(id(x)))
print('nilai y =',y,',id = ',hex(id(y)))
hasil = x is not y
print('x is not y =',hasil)