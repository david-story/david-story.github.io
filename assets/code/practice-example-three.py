""""
Practice File 3
Created By David Story

Description: All about bit operators!
"""

# Some basic examples of hex, dec, and bin in Python
print("Example Using 0xAA:")
hexvalue = 0xAA
print(hex(hexvalue))
print(int(hexvalue))
print(bin(hexvalue))

print("Example Using decimal 65:")
decimal = 65
print(int(decimal))
print(hex(decimal))
print(bin(decimal))

print("Converting decimal 65 to ASCII:", chr(decimal))

# The following are examples of bit operators in Python

# Shifting bits to the right
value = 0xF0
print("Value before right shift by 4 bits:", bin(value))
newvalue = value >> 4
print("Value after right shift by 4 bits:", bin(newvalue))

# Shifting bits to the left
value = 0x01
print("Value before left shift by 4 bits:", bin(value))
newvalue = value << 4
print("Value after right shift by 4 bits:", bin(newvalue))

# We will now do bit AND, OR, XOR, and complement

x = 0xFF
y = 0xAA
print("Values to AND:", bin(x), "and'd with", bin(y))
z = x & y
print(bin(z))

x = 0xAA
y = 0x55
print("Values to OR:", bin(x), "or'd with", bin(y))
z = x | y
print(bin(z))

x = 0xFF
y = 0xAA
print("Values to XOR:", bin(x), "xor'd with", bin(y))
z = x ^ y
print(bin(z))

val = 0x00
print("Values to complement:", bin(val))
complement = ~val
print(bin(complement))

