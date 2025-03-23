book_list = list()

menu = """
1) Add Book
2) Remove Book
3) View Book
4) Press E to Exit
"""
def add_book(booklist, book):
    booklist.append(book)
    print("Book added Sucessfully")

def remove_book(booklist, book):
    if book in booklist:
       booklist.remove(book)
       print("Book removed Sucessfully")
    else:
        print("Cant Found this book in the list")

# View fuction to view all books

def view_list(booklist):
    if booklist:
        print("Your Book list ->", ", ".join(booklist))
    else:
        print("No books found in the list")

#Function to exit the program

def exit_program():
    print("Thankyou for visiting the command line library management system.")
    quit()

#main program loop
while True:
    print(menu)
    choice = input("Your choice: ")

    if choice == "1" : #add book
        book_name = input("Enter the book name you want to add in the list: ")
        add_book(book_list, book_name)

    elif choice == "2": #remove book
        book_name = input("Enter the book name you want to remove from the list: ")
        remove_book(book_list, book_name)

    elif choice == "3": #View Books
        view_list(book_list)

    elif choice.lower() == "e": #Exit Program
        exit_program()

    else:
        print("Invalid input")
        input("Press enter to return to the main menu!")

    