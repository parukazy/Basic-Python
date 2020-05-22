# Program Konversi Celcius ke Satuan Lain

print("PROGRAM KONVERSI TEMPERATUR\n")

# celcius = float(input("Masukkan Suhu dalam Celcius: "))
# print("Suhu adalah",celcius, "Celcius")

# reamur = (4/5) * celcius
# print("Suhu dalam reamur adalah",reamur, "Reamur")

# fahrenheit = ((9/5) * celcius) + 32
# print("Suhu dalam fahrenheit adalah",fahrenheit, "Fahrenheit")

# kelvin = celcius + 273
# print("Suhu dalam kelvin adalah",kelvin, "Kelvin")
# ===================================================
# Program Konversi Reamur ke Satuan Lain
# reamur = float(input("Masukkan Suhu dalam Reamur: "))
# print("Suhu adalah",reamur,"Reamur")

# celcius = (5/4) * reamur
# print("Suhu dalam celcius adalah",celcius,"Celcius")

# fahrenheit = ((9/4) * reamur) + 32
# print("Suhu dalam fahrenheit adalah",fahrenheit,"Fahrenheit")
# 0
# kelvin = ((5/4) * reamur) + 273
# print("Suhu dalam kelvin adalah",kelvin,"Kelvin")
# ==============================================
# Program Konversi Fahrenheit ke Satuan Lain
# fahrenheit = float(input("Masukkan Suhu dalam Fahrenheit: "))
# print("Suhu adalah",fahrenheit,"Fahrenheit")

# celcius = 5/9 * (fahrenheit - 32)
# print("Suhu dalam celcius adalah",celcius,"Celcius")

# reamur = 4/9 * (fahrenheit - 32)
# print("Suhu dalam reamur adalah",reamur,"Reamur")
# 0
# kelvin = (5/9 * (fahrenheit - 32)) + 273
# print("Suhu dalam kelvin adalah",kelvin,"Kelvin")

# ==============================================
# Program Konversi Kelvin ke Satuan Lain
kelvin = float(input("Masukkan Suhu dalam Kelvin: "))
print("Suhu adalah",kelvin,"Kelvin")

celcius = kelvin - 273
print("Suhu dalam celcius adalah",celcius,"Celcius")

reamur = 4/5 * (kelvin - 273)
print("Suhu dalam reamur adalah",reamur,"Reamur")
0
fahrenheit = (9/5 * (kelvin - 273)) + 32
print("Suhu dalam fahrenheit adalah",fahrenheit,"Fahrenheit")
