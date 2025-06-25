from mylibrary import library, book

my_books = [book.Book("salam", "ali"),
            book.Book("chetori", "mammad"),
            book.Book("khobi", "hossein"),
            book.Book("kojaei", "sajjad"),

            ]
print("_______")
print("making a local library: ...")
mylibrary = library.Library(my_books)
print("_______")

print("show all books in this library:")
print(mylibrary.show_book())
print("________")

print(mylibrary.search_book("kk"))
print(mylibrary.search_book("salam"))
print("________")

print("remove book from this library:")
mylibrary.remove_book("salam")
print("book with title : salam is removed")
print(mylibrary.show_book())
print("________")

