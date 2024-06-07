class Book:
    all_books = []

    def __init__(self, title):
        if not isinstance(title, str) or not title:
            raise Exception("Title must be a non-empty string")
        self._title = title
        Book.all_books.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str) or not value:
            raise Exception("Title must be a non-empty string")
        self._title = value

    def contracts(self):
        return [contract for contract in Contract.all_contracts if contract.book == self]

    def authors(self):
        return [contract.author for contract in self.contracts()]

class Author:
    all_authors = []

    def __init__(self, name):
        if not isinstance(name, str) or not name:
            raise Exception("Name must be a non-empty string")
        self._name = name
        Author.all_authors.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not value:
            raise Exception("Name must be a non-empty string")
        self._name = value

    def contracts(self):
        return [contract for contract in Contract.all_contracts if contract.author == self]

    def books(self):
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())

class Contract:
    all_contracts = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("Author must be an instance of the Author class")
        if not isinstance(book, Book):
            raise Exception("Book must be an instance of the Book class")
        if not isinstance(date, str) or not date:
            raise Exception("Date must be a non-empty string")
        if not isinstance(royalties, int) or royalties < 0:
            raise Exception("Royalties must be a non-negative integer")

        self._author = author
        self._book = book
        self._date = date
        self._royalties = royalties
        Contract.all_contracts.append(self)

    @property
    def author(self):
        return self._author

    @property
    def book(self):
        return self._book

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if not isinstance(value, str) or not value:
            raise Exception("Date must be a non-empty string")
        self._date = value

    @property
    def royalties(self):
        return self._royalties

    @royalties.setter
    def royalties(self, value):
        if not isinstance(value, int) or value < 0:
            raise Exception("Royalties must be a non-negative integer")
        self._royalties = value

    @classmethod
    def contracts_by_date(cls, date):
        if not isinstance(date, str) or not date:
            raise Exception("Date must be a non-empty string")
        return [contract for contract in cls.all_contracts if contract.date == date]

