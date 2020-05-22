# Casting Data Type -> Changed one Data Type to another Data Type

# Integer
print("====INTEGER====")
integerData = 9
print("data = ", integerData, ", type = ", type(integerData))

# Operator Casting
floatData = float(integerData)
stringData = str(integerData)
boolData = bool(integerData) # will false if value int = 0
print("data = ", floatData, ", type = ", type(floatData))
print("data = ", stringData, ", type = ", type(stringData))
print("data = ", boolData, ", type = ", type(boolData))


print("\n")

# Float
print("====FLOAT====")
floatData = 10
print("data = ", floatData, ", type = ", type(floatData))

# Operator Casting
integerData = int(floatData) # will numeric circle in down
stringData = str(floatData)
boolData = bool(floatData) # will false if value int = 0
print("data = ", integerData, ", type = ", type(integerData))
print("data = ", stringData, ", type = ", type(stringData))
print("data = ", boolData, ", type = ", type(boolData))

print("\n")

# Boolean
print("====BOOLEAN====")
boolData = True
print("data = ", boolData, ", type = ", type(boolData))

# Operator Casting
integerData = int(boolData) # will numeric circle in down
stringData = str(boolData)
floatData = float(boolData) # will false if value int = 0
print("data = ", integerData, ", type = ", type(integerData))
print("data = ", stringData, ", type = ", type(stringData))
print("data = ", floatData, ", type = ", type(floatData))

print("\n")

# String
print("====STRING====")
stringData = "0"
print("data = ", stringData, ", type = ", type(stringData))

# Operator Casting
integerData = int(stringData) # String must be number
boolData = bool(stringData) # False if String null
floatData = float(stringData) # String must be number
print("data = ", integerData, ", type = ", type(integerData))
print("data = ", boolData, ", type = ", type(boolData))
print("data = ", floatData, ", type = ", type(floatData))