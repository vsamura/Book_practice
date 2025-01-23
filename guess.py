# Это игра по угадыванию чисел
import random

def get_number():
    while type:
        get_number = input()                 
        try:                                   
            get_temp_number = int(get_number)
        except ValueError:                      
            print('"' + get_number + '"' + ' - не является числом!')
            print('Надо ввести число цифрами что бы угадать!')
        else:                                   
            break
    return int(get_number)                   


guesses_taken = 0
print('Привет! Как тебя зовут?')
my_name = input()
number = random.randint(1, 100)
print('Что ж, ' + my_name + ', я загадываю число от 1 до 100.')
print('Попробуй угадать!')

for guesses_taken in range(6):
	guess = get_number()
	if guess < number:
		print('Твое число слишком маленькое.')
	if guess > number:
		print('Твое число слишком большое.')
	if guess == number:
		break
	if guesses_taken < 5:
		print('Попробуй ещё раз!')

if guess == number:
	guesses_taken = guesses_taken + 1
	declension = 'попытки!'
	if guesses_taken == 1:
		declension = 'попытку!'
	elif guesses_taken > 4:
		declension = 'попыток!'
	print('Отлично, ' + my_name + '!')
	print('Ты справился за ' + str(guesses_taken) + ' ' + declension)
else:
	print('Увы, но попытки кончились!\n Я загадал число ' + str(number) + '.')
