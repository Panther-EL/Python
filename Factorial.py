 number = int(input('Enter your number: '))
factorial = 1
 for i in range(number,0,-1):
     factorial *= i
 print(f'The factorial of {number} is {factorial}')
