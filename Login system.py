ef register(): #User signs up
    f = open('form.txt','a')
    username = (input('Enter your username: ' ))
    password = (input('Enter your password: '))
    f.write(username + '\n')
    f.write(password + '\n')
    f.close()

def login(): #User gets access
    username = (input('Enter your username: ' ))
    password = (input('Enter your password: '))
    f = open('form.txt')
    content = f.read()
    f.close()


    if username in content and password in content:
        print('Login successful')
    else:
        print("Username or password doesn't exist")

def change_password(): #User changes the existing password
    f = open('form.txt','r')
    content = f.read()
    f.close()

    username = input('Enter your username: ')
    old_password = input('Enter your old password: ')

    if username in content and old_password in content:
      new_password =  input('Enter your new password:')
      content = content.replace(old_password,new_password,1)
      
      f = open('form.txt','w')
      f.write(content)
      f.close()
      print('Password changed successfully')
    else:
        print("Username or password doesn't exist")

               #Main program
while True:
    print('---Menu---')
    options = ['1.Register','2.Login','3.Change Password' ,'4.Exit']
    for o in options:
        print(o)

    choice = input('Enter your choice: ')
    if choice == '1':
        register()
    elif choice == '2':
        login()
    elif choice == '3':
        change_password()
    elif choice == '4':
        break

 
