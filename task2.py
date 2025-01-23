class Review:
    def __init__(self,
                 text:str):
        self.text = text

    def __str__(self):
        return f'"{self.text}"'
    

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
        self.reviews = []

    def add_review(self, review: Review):
        self.reviews.append(review)

    def show_reviews(self):
        if not self.reviews:
            return f'До книги "{self.title}" ще немає відгуків.'
        return "Відгуки:\n" + "\n".join(f"- {review}" for review in self.reviews)

    def print_info(self):
        print(f"назва: {self.title}\n"
        f"автор: {self.author}\n"
        f"жанр: {self.genre}\n"
        f"рік видання: {self.publication_year}\n\n"
        )
        if not self.reviews:
            print("відгуки: ще немає відгуків")
        else:
            print(self.show_reviews())
            print()
            print()


book1 = Book("Тигролови", "Іван Багряний", "пригодницький роман", "1944")
book2 = Book("Захар Беркут", "Іван Франко", "історична повість", "1883")
book3 = Book("Місто", "Валер'ян Підмогильний", "урбаністичний роман", "1928")

book1.add_review(Review("Неймовірна історія боротьби за свободу!"))
book1.add_review(Review("Головний герой вражає своєю силою духу."))
book1.add_review(Review("Опис тайги настільки реалістичний, що здається, ніби сам там побував."))

book2.add_review(Review("Мудрість і патріотизм Захара Беркута — приклад для всіх поколінь."))
book2.add_review(Review("Прекрасний твір про боротьбу за рідну землю."))
book2.add_review(Review("Читається легко, хоча події розгортаються в давнину."))

book3.add_review(Review("Дуже цікава психологічна проза, яка змушує замислитися."))
book3.add_review(Review("Головний герой — типовий образ людини, яка прагне успіху."))
book3.add_review(Review("Актуальне навіть у наш час, особливо для тих, хто переїжджає у велике місто."))

book1.print_info()
book2.print_info()
book3.print_info()
