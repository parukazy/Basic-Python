a = 10
b = 3

# Plus Operation (+)
hasil = a + b
print(a, '+', b, '=', hasil)

# Minus Operation (-)
hasil = a - b
print(a, '-', b, '=', hasil)

# Perkalian (*)
hasil = a * b
print(a, '*', b, '=', hasil)

# Pembagian (/)
hasil = a / b
print(a, '/', b, '=', hasil)

# Eksponen (pangkat (**))
hasil = a ** b
print(a, 'pangkat', b, '=', hasil)

# Modulus (% -> Sisa Pembagian)
hasil = a % b
print(a, 'modulus', b, '=', hasil)

# Floor Division (//)
hasil = a // b
print(a, '//', b, '=', hasil)

# Operational Precendence
'''
    1. ()
    2. Eksponen **
    3. Perkalian and Friends (* / ** % //)
    4. Pertambahan dan Pengurangan (+ -)
'''
x = 3
y = 2
z = 4

hasil = x + y - z * x ** z // y / y % z
print(x,'+',y,'-',z,'*',x,'**',z,'//',y,'/',y,'%',z, '=', hasil)