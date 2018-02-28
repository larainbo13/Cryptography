# Reverse Cipher Modified


print('Please enter the string to be reversed.')
message = input()
translated = ''

i = len(message) - 1
while i >= 0:
    translated = translated + message[i]
    i = i - 1

print(translated)
