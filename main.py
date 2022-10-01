import string

password = input("Введите пароль: ")

upper_case = any([1 if i in string.ascii_uppercase else 0 for i in password])
lower_case = any([1 if i in string.ascii_lowercase else 0 for i in password])
special = any([1 if i in string.punctuation else 0 for i in password])
digits = any([1 if i in string.digits else 0 for i in password])
length = len(password)

if length >= 10:
    length = True
else:
    length = False

chatacters = [upper_case, lower_case, special, digits, length]

score = 0

for i in range(len(chatacters)):
    if chatacters[i]:
        score += 1

print("Надежность вашего пароля %s из 5 " %score)