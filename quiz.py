from time import sleep

def loading():
	print(f'\033[30;107mLoading', end='')
	for c in range(3):
		print('.', end='', flush=True)
		sleep(0.5)
	print('\033[m\n')

win = 0
print('-'*25)
print('QUIZ BY HYOKOJIRO'.center(25))
print('-'*25)
while True:
	try:
		print('\n1° What year was Python created? ')
		print("""[\033[36;1m 1\033[m ] 1990
[\033[36;1m 2 \033[m] 1991
[\033[36;1m 3 \033[m] 2000
[\033[36;1m 4 \033[m] 1989""")
		answer1 = int(input('\nThe answer is... '))
		
		if answer1 == 2:
			loading()
			print(f"\033[32;1mCorrect\033[m answer! ")
			win += 1
		elif answer1 > 4 or answer1 < 1:
			print('\n')
			print('~'*37)
			print('Write only a number from 1 to 4.'.center(37))
			print('~'*37)
			sleep(0.8)
			continue
		else:
			loading()
			print('\033[31;1mWrong\033[m answer! Python was created in 1991.')
		
		break
	except ValueError:
		print('\n')
		print('~'*30)
		print('Write just a \033[32mreal\033[m number.'.center(40))
		print('~'*30)
		sleep(0.8)
	else:
		break




print('-'*40)
print('SEGOND QUESTION'.center(35))
print('-'*40)
sleep(1)
while True:
	try:
		print('\n2° Who created the Marvel Universe?')
		print("""[\033[36;1m 1\033[m ] Stan Lee
[\033[36;1m 2 \033[m] Joe Simon
[\033[36;1m 3 \033[m] Steve Ditko
[\033[36;1m 4 \033[m] Wolverine""")
		answer2 = int(input('\nThe answer is... '))
		if answer2 == 1:
			loading()
			print(f"\033[32;1mCorrect\033[m answer! ")
			win +=  1
		elif answer2 > 4 or answer2 < 1:
			print('\n')
			print('~'*37)
			print('Write only a number from 1 to 4.'.center(37))
			print('~'*37)
			sleep(0.8)
			continue
		else:
			loading()
			print('\033[31;1mWrong\033[m answer! Stan Lee the creator of Marvel.')
			
	except ValueError:
		print('\n')
		print('~'*30)
		print('Write just a \033[32mreal\033[m number.'.center(40))
		print('~'*30)
		sleep(0.8)
	else:
		break




print('-'*40)
print('THIRD QUESTION'.center(35))
print('-'*40)
sleep(1)
while True:
	try:
		print('\n3° Who created Python?')
		print("""[\033[36;1m 1\033[m ] A Fish
[\033[36;1m 2 \033[m] Mark Zuckerberg
[\033[36;1m 3 \033[m] Markus Persson
[\033[36;1m 4 \033[m] Guido van Rossum""")
		answer3 = int(input('\nThe answer is... '))
		if answer3 == 4:
			loading()
			print(f"\033[32;1mCorrect\033[m answer! ")
			win +=  1
		elif answer3 > 4 or answer3 < 1:
			print('\n')
			print('~'*37)
			print('Write only a number from 1 to 4.'.center(37))
			print('~'*37)
			sleep(0.8)
			continue
		else:
			loading()
			print('\033[31;1mWrong\033[m answer! Guido van Rossum is the creator of Python.')
			
	except ValueError:
		print('\n')
		print('~'*30)
		print('Write just a \033[32mreal\033[m number.'.center(40))
		print('~'*30)
		sleep(0.8)
	else:
		break
		
sleep(1)
print('-'*40)
print(f'You got the questions right {win} times.\n')
print(f'\033[33;4m{"=== End of Quiz ===":^40} \033[m')
