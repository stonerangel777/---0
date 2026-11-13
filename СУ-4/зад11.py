class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def print(self):
        print("Заглавие:", self.title)
        print("Автор:", self.author)
        print("Година на издаване:", self.year)


class EBook(Book):
    def __init__(self, title, author, year, format, size):
        super().__init__(title, author, year)
        self.format = format
        self.size = size

    def print(self):
        super().print()
        print("Файлов формат:", self.format)
        print("Размер:", self.size, "MB")


eb1 = EBook("Под игото", "Иван Вазов", 1894, "PDF", 5.2)
eb2 = EBook("Тютюн", "Димитър Димов", 1951, "EPUB", 3.5)

eb1.print()
print()
eb2.print()