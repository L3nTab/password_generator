import random
chars = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
length = int(input("Введите нужную длину пароля: "))
password = ""
for i in range(length):
    password += random.choice(chars)
print("Сгенерированный пароль:", password)
