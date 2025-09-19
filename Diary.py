#Personal diary

def add_entry(): #Add a new entry
    f = open('diary.txt', 'a')
    f.write(input('Enter your entry:') + '\n')
    f.close()

def view_entry(): # Displays all entries
    f = open('diary.txt')
    print(f.read())
    f.close()

def search_entry():
    word_to_search = input('Enter the word you want to search:')
    f = open('diary.txt')
    diary = f.read()
    f.close()
    if word_to_search in diary:
        print(word_to_search)
    else:
        print('Word not found')

#Main program
while True:
    print('---Personal diary---')
    options = ['1.Add entry','2.View all entries','3.Search entry','4.Exit']
    for o in options:
        print(o)

    choice = input('Enter your choice:')
    if choice == '1':
            add_entry()
    elif choice == '2':
            view_entry()
    elif choice == '3':
            search_entry()
    elif choice == '4':
            print('Bye!')
            break
    else:
            print('Incorrect choice')
        
    
