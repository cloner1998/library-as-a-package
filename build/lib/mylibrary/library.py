import mylibrary.book as book
class Library(book.Book):
    def __init__(self, books: list[book.Book], ):
        self.books = books


    def add_book(self, title: str, author: str):
        return self.books.append(book.Book(title, author))

    def remove_book(self, title: str):
        find_book = None
        for book_in_library in self.books:
            if book_in_library.title == title:
                find_book = book_in_library
                break
        if find_book is not None:
            self.books.remove(find_book)
        else:
            print("Book with title: '{}' not found".format(title))

        return self

    def search_book(self, title: str):

        desired_book = ""
        for book_in_library in self.books:
            if book_in_library.title == title:
                desired_book =book_in_library
                break

        if desired_book == "":
            return f"your book with title: '{title}' is not found in library"
        else:
            return f'your book is found and its title is: {desired_book.title}'
    def show_book(self):
        all_books = []
        for book_in_library in self.books:
            all_books.append(f"title: {book_in_library.title} , author: {book_in_library.author}")
        return all_books

if __name__ == "__main__":
    print("please use this file as module")