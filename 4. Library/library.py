import book
import pickle
import os

class Library:
    def __init__(self) -> None:
        self.books = {}
        self.load_lib()
    
    def add_book(self, name, author, year, stat, tenant):
        keys = list(self.books.keys())
        id = keys[-1] + 1 if keys else 1
        self.books[id] = book.Book(name=name, author=author, year=year, stat=stat, tenant=tenant)
        print('Книга добавлена')

    def remove_book(self, num_book) -> None:
        if num_book in self.books:
            del self.books[num_book]
            self.reinit_books()
            print('Книга удалена')
        else:
            print('Неверный идентификатор книги')

    def reinit_books(self) -> None:
        new_books = {}
        counter = 1
        for i in self.books.keys():
            new_books[counter] = self.books[i]
            counter += 1
        self.books = new_books
    
    def var_to_string(self, id, book) -> str:
        return f'{id}. {book.name} - {book.author} ({book.year}) - {"В наличии" if book.stat else "Занята"} {f"({book.tenant})" if not book.stat else ""}'
    
    def search_book(self, query) -> list:
        list_books = []
        query = query.lower()
        for i in self.books.keys():
            if query in self.books[i].name.lower() or query in self.books[i].author.lower():
                list_books.append(self.var_to_string(i, self.books[i]))
        if list_books:
            return list_books
        else:
            print('Книг не найдено')
            return []

    def return_book(self, key):
        if key in self.books:
            self.books[key].stat = True
            self.books[key].tenant = ''
            print('Книга возвращена')
        else:
            print('Неверный идентификатор книги')

    def take_book(self, key):
        if key in self.books:
            if self.books[key].stat:
                self.books[key].stat = False
                self.books[key].tenant = input('Введите ФИО взявшего книгу: ')
                print('Книга взята в аренду')
            else:
                print('Книга уже в аренде')
        else:
            print('Неверный идентификатор книги')

    def print_all(self) -> list:
        list_books = []
        for i in self.books:
            list_books.append(self.var_to_string(i, self.books[i]))
        if list_books:
            return list_books
        else:
            print('Книг не найдено')
            return []

    def load_lib(self):
        if os.path.exists('data.pickle'):
            try:
                with open('data.pickle', 'rb') as file:
                    self.books = pickle.load(file)
            except (pickle.UnpicklingError, EOFError):
                print('Ошибка при загрузке данных. Файл поврежден.')
                self.books = {}
        else:
            print('Файл данных не найден. Создается новая библиотека.')
            self.books = {}

    def save_lib(self):
        with open('data.pickle', 'wb') as file:
            pickle.dump(self.books, file)
