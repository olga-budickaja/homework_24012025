class Book:
    def __init__(self,
                 title:str,
                 author:str,
                 genre:str,
                 publication_year:str,
                 ):
        self.title = title
        self.author = author
        self.genre = genre
        self.publication_year = publication_year

    def print_info(self):
        print(f"назва: {self.title}\n"
              f"автор: {self.author}\n"
              f"жанр: {self.genre}\n"
              f"рік видання: {self.publication_year}\n\n"
              )

    def __str__(self):
        return f'Книгу "{self.title}", яку написав {self.author} в жанрі {self.genre}, було видано у {self.publication_year} році.\n'

    def __repr__(self):
        return f'Book("{self.title}", "{self.author}", "{self.genre}", "{self.publication_year}")'


book1 = Book("Тигролови", "Іван Багряний", "пригодницький роман", "1944")
book2 = Book("Захар Беркут", "Іван Франко", "історична повість", "1883")
book3 = Book("Місто", "Валер'ян Підмогильний", "урбаністичний роман", "1928")

book1.print_info()
book2.print_info()
book3.print_info()

print(str(book1))
print(str(book2))
print(str(book3))

print(repr(book1))
print(repr(book2))
print(repr(book3))
