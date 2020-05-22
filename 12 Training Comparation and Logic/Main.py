# membuat gabungan area rentang dari angka

# +++++++3----------10++++++++++

inputUser = float(input("Masukkan angka yang bernilai \nkurang dari 3 \natau \nlebih besar dari 10: "))

# +++++3----------
# Memeriksa angka kurang dari 3
isKurangDari = (inputUser < 3)
print("Kurang dari 3 =",isKurangDari)

#  ------------10++++++++
# Memeriksa angka lebih dari 10
isLebihDari = (inputUser > 10)
print("Lebih dari 10 =",isLebihDari)

# +++++3---------10+++++++
isCorrect = isKurangDari or isLebihDari
print("Angka yang anda masukkan: ",isCorrect)

# -----3++++++++10----------
# Slice Case
print("\n",10*"=","\n")
inputUser = float(input("Masukkan angka yang bernilai \nlebih dari 3 \ndan \nkurang dari 10: "))

# ----3++++++
isLebihDari = inputUser > 3
print("Lebih dari 3 =",isLebihDari)

# +++++10--------
isKurangDari = inputUser < 10
print("Kurang dari 10 =",isKurangDari)

# --------3++++++10-----------
isCorrect = isKurangDari and isLebihDari
print("Angka yang anda masukkan: ",isCorrect)


# LATIHANNN
# Soal 1. -------0+++++++5------8++++++11--------
inputUser = float(input("Masukkan angka lebih dari 0 \ndan \nkurang dari 5 \natau \nlebih dari 8 \ndan \nkurang dari 11: "))

isLebih0 = (inputUser > 0)
# print("Lebih dari 0 =",isLebih0)

isKurang5 = (inputUser < 5)
# print("Kurang dari 5 =",isKurang5)

isCorrect1 = isKurang5 and isLebih0
# print("Angka yang dimasukkan Lebih dari 0 dan Kurang dari 5 =",isCorrect1)

isLebih8 = (inputUser > 8)
# print("Lebih dari 8 =",isLebih8)

isKurang11 = (inputUser < 11)
# print("Kurang dari 11 =",isKurang11)

isCorrect2 = isKurang11 and isLebih8
# print("Angka yang dimasukkan Lebih dari 8 dan Kurang dari 11 =",isCorrect2)

final = isCorrect1 or isCorrect2
print("Angka yang anda masukkan",final)

print("\n",10*"=","\n")
# Soal 2. +++++0---------5+++++8---------11+++++
inputUser = float(input("Masukkan angka kurang dari 0 \natau \nlebih dari 5 \ndan \nkurang dari 8 \natau \nlebih dari 11: "))

iskurang0 = (inputUser < 0)
# print("Lebih dari 0 =",isLebih0)

islebih5 = (inputUser > 5)
# print("Kurang dari 5 =",isKurang5)

isCorrect1 = islebih5 or iskurang0
# print("Angka yang dimasukkan Lebih dari 0 dan Kurang dari 5 =",isCorrect1)

isKurang8 = (inputUser < 8)
# print("Lebih dari 8 =",isLebih8)

isLebih11 = (inputUser > 11)
# print("Kurang dari 11 =",isKurang11)

isCorrect2 = isLebih11 or isKurang8
# print("Angka yang dimasukkan Lebih dari 8 dan Kurang dari 11 =",isCorrect2)

final = isCorrect1 and isCorrect2
print("Angka yang anda masukkan",final)