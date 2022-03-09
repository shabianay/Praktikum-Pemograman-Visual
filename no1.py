#Shabian Arsyl Yonanta
#NIM 20051397032

print("Pilih mode:")
print("1 encrypt")
mode = int(input())
print("Masukkan kunci (0 hingga 25):")
key = int(input())
print("Masukkan Kata:")
message = input()
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
translated = ''
message = message.upper()
for symbol in message:
    if symbol in letters:
        num = letters.find(symbol)
        if mode <= 1:
            num += key
        if num >= len(letters):
            num -= len(letters)
        translated += letters[num]
    else:
        translated += symbol
print(translated)