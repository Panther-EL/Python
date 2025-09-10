#Building a translator

def translate(word): 
     translation = ''
     for letter in word:
         if letter in 'AEIOUaieou':
             translation = translation + 'r'
         else:
             translation + translation + letter
     return translation

print(translate(input('Enter your keyword:')))            
