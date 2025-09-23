#File reader
name = input('Enter the name of the file to open: ')#Ask user for filename
try:
    with open (name) as f:
        details = f.read()
        print(details)
except FileNotFoundError:
        print('File not found')
except PermissionError:
     print('Permission denied')
except Exception as e:
     print('An unknown error occured',e)
