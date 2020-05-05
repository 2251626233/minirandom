import random

correctPassword = "3543" # Вводим пароль, который нужно забрутить
wrongPasswords = [] # В этот список будут добавляться уже подобранные пароли, чтобы не повторяться
password = "" # В эту переменную будет записываться сгенерированный пароль,  и, если он ложный, пойдет в wrongPassword
length = 4 # Длина пароля. Эта переменная нужна будет в будущем
chars = "1234567890"  # Символы, из которых будет генерироваться пароль.
run = True

while run:
    password = ""

    for i in range(length):
        password += random.choice(chars)

    if password not in wrongPasswords:
        print(password)
    if password != correctPassword:
        wrongPasswords.append(password)
    else:
        run = False
        break
print(password + " is correct")