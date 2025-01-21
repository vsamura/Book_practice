# Это игра по угадыванию чисел
import random

def getNumber():
    while type:
        getNumber = input()                 
        try:                                   
            getTempNumber = int(getNumber)
        except ValueError:                      
            print('"' + getNumber + '"' + ' - не является числом!')
            print('Надо ввести число цифрами что бы угадать!')
        else:                                   
            break
    return int(getNumber)                   


guessesTaken = 0
print('Привет! Как тебя зовут?')
myName = input()
number = random.randint(1, 100)
print('Что ж, ' + myName + ', я загадываю число от 1 до 100.')
print('Попробуй угадать!')

for guessesTaken in range(6):
	guess = getNumber()
	if guess < number:
		print('Твое число слишком маленькое.')
	if guess > number:
		print('Твое число слишком большое.')
	if guess == number:
		break
	if guessesTaken < 5:
		print('Попробуй ещё раз!')

if guess == number:
	guessesTaken = guessesTaken + 1
	declension = 'попытки!'
	if guessesTaken == 1:
		declension = 'попытку!'
	elif guessesTaken > 4:
		declension = 'попыток!'
	print('Отлично, ' + myName + '!')
	print('Ты справился за ' + str(guessesTaken) + ' ' + declension)
else:
	print('Увы, но попытки кончились!\n Я загадал число ' + str(number) + '.')
