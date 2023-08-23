#MSB & LSB

num=int(input("Input a number: "))

msb=num%10
lsb=num//10**(len(str(num))-1)

print("LSB: ",lsb)
print("MSB: ",msb)
