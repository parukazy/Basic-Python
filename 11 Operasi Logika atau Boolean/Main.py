# Logika dan Boolean

# not, or, and, xor

# Not
print("-- NOT --") # Selalu kebalikan dari nilai yang ditentukan
a = True
c = not a
print('Data a =',a)
print('--------- NOT')
print('Data c =',c)

# Or
print("-- OR --") # Jika Salah satu True, maka akan TRUE
a = False
b = False
c = a or b
print(a,'OR',b,'=',c) 
a = False
b = True
c = a or b
print(a,'OR',b,' =',c) 
a = True
b = False
c = a or b
print(a,' OR',b,'=',c) 
a = True
b = True
c = a or b
print(a,' OR',b,' =',c) 

# And
print("-- AND --") # Jika Salah satu False, maka akan FALSE
a = False
b = False
c = a and b
print(a,'AND',b,'=',c) 
a = False
b = True
c = a and b
print(a,'AND',b,' =',c) 
a = True
b = False
c = a and b
print(a,' AND',b,'=',c) 
a = True
b = True
c = a and b
print(a,' AND',b,' =',c) 

# Xor
print("-- XOR --") # Jika keduanya sama maka hasilnya akan False
a = False
b = False
c = a ^ b
print(a,'XOR',b,'=',c) 
a = False
b = True
c = a ^ b
print(a,'XOR',b,' =',c) 
a = True
b = False
c = a ^ b
print(a,' XOR',b,'=',c) 
a = True
b = True
c = a ^ b
print(a,' XOR',b,' =',c) 