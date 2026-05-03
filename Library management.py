my_books = []
wish_books = []

print('| Welcome to the books management |')

book = input('Enter the name of book you have: ').strip().capitalize()
my_books.append(book)

while True:
    another_book = input('\nDo you have another book (Yes/No)? ').lower().strip()
    if another_book not in ['yes', 'no']:
        print('Please enter "Yes" or "No"')
    elif another_book == 'no':
        print(f'\nYour library now contains:\n{my_books}')
        break
    else:
        new_book = input('Enter the name of the other book: ').strip().capitalize()
        my_books.append(new_book)

while True:
    wish_book = input('\nIs there a book you want to have (Yes/No)? ').lower().strip()
    if wish_book not in ['yes', 'no']:
        print('Please enter "Yes" or "No"')
    elif wish_book == 'no':
        if wish_books:
            print(f'\nThe books you want to have:\n{wish_books}')
        else:
            print('I am sure there is a book you may want to have someday')
        break
    else:
        target_book = input('Enter the name of the book you want to have: ').strip().capitalize()
        if target_book in my_books:
            print('You already have this book')
        elif target_book in wish_books:
            print('The book is already in your wishlist')
        else:
            wish_books.append(target_book)

while True:
    see_library = input('\nDo you want to see your library (Yes/No)? ').lower().strip()
    if see_library not in ['yes', 'no']:
        print('Please enter "Yes" or "No"')
    elif see_library == 'no':
        print('Thank you for using our service\nExiting...')
        break
    else:
        if my_books:
            print(f'\nYour books:\n{my_books}')
            print(f'\nThe books you want to have:\n{wish_books}')
        else:
            print('Sorry, You do not have books to see')
        break