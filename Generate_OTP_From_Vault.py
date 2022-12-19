
import random

Generated_OTP = []

f = open('vault.txt','r')
for i in f:
    Generated_OTP.append(i[0:8])
    print(i)

print("These are the generated total numeric OTPs")
print(Generated_OTP)

index = random.randint(0,len(Generated_OTP))
print(index)

print("This is the generated number output for use......................")
print(Generated_OTP[index])

print("This is the generated character based OTP for use................")
#Generating the Character Based OTP algorithm:
alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numeric_OTP = str(Generated_OTP[index])
input_length = len(numeric_OTP)
shift_input = 4
print(input_length)
output = ""

for i in numeric_OTP:
    i = int(i)
    character = alphabets[i]
    output = output + character

print(output)
