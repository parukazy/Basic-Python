# Data Type in Python - Universe
# 1. Integer
integerData = 1
print("Data : ", integerData, ", Type : ", type(integerData))

# 2. Float -> point number -> 1.5 2.4
floatData = 1.2
print("Data : ", floatData, ", Type : ", type(floatData))

# 3. String -> Kumpulan Karakter
stringData = "Paruk"
print("Data : ", stringData, ", Type : ", type(stringData))

# 4. Boolean -> Type Data Binary
boolData = False
print("Data : ", boolData, ", Type : ", type(boolData))

# Example
first = "10" # String because value use quote
print("Data : ", first, ", Type : ", type(first))

# Data Type in Python -> not Universe
# Complex Numeric
complexData = complex(5,6)
print("Data : ", complexData, ", Type : ", type(complexData))

# Data Type from C Language
from ctypes import c_double

cDoubleData = c_double(10.5)
print("Data : ", cDoubleData, ", Type : ", type(cDoubleData))