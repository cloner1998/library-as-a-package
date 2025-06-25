
import mylibrary.book
import mylibrary.library




def add_library():
    number_of_books = int(input("How many books do you want to add? "))
    list_of_books = []
    for i in range(number_of_books):
        print("Adding book #{}".format(i+1))
        title = input("Enter title: ")
        author = input("Enter author: ")
        list_of_books.append(mylibrary.book.Book(title, author))

    my_library = mylibrary.library.Library(list_of_books)
    print(f"your library now has : {my_library.show_book()}")
    return my_library


def add_book(current_lib, title, author):
    current_lib.add_book(title, author)
    return current_lib


def remove_book(current_lib , title):
    current_lib.remove_book(title)
    return current_lib


def search_book(current_lib, title):
    print(current_lib.search_book(title))

def show_current_lib(current_lib):
    print("your current library is:")
    print(current_lib.show_book())

if __name__ == "__main__":
    print("Hi, Welcome to my book library")
    ans = input("do you want to add a library? (y/n)")
    if ans.upper() == "Y":
        current_lib = add_library()

        end = False
        while not end:
            print("____________________")
            ans = input("How do you want to modify you library(add, remove, search)?")
            if ans.upper() == "ADD":
                title = input("Enter title: ")
                author = input("Enter author: ")
                add_book(current_lib, title, author)
                show_current_lib(current_lib)
            elif ans.upper() == "REMOVE":
                title = input("Enter title: ")
                remove_book(current_lib, title)
                show_current_lib(current_lib)
            elif ans.upper() == "SEARCH":
                title = input("Enter title: ")
                search_book(current_lib, title)

            else:
                print("there is no such modification, please try again")

            end_check = input("Do you want to continue? (y/n)")

            if end_check.upper() == "N":
                end = True
                print("____________________")
                print("thank you for using this program")
    else:
        print("exit")

