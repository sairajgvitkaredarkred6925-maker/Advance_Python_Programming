# 7. Product Inventory System
class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def category(self):
        return "Expensive" if self.price > 1000 else "Affordable"

class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def display_products(self):
        for p in self.products:
            print(f"ID: {p.product_id}, Name: {p.name}, Price: {p.price}, Category: {p.category()}")

# Example usage
inv = Inventory()
inv.add_product(Product(1, "Laptop", 50000))
inv.add_product(Product(2, "Book", 300))
inv.display_products()


# 8. Movie Collection Management System
class Movie:
    def __init__(self, name, rating, ticket_price):
        self.name = name
        self.rating = rating
        self.ticket_price = ticket_price

    def category(self):
        if self.rating >= 8:
            return "Hit"
        elif 5 <= self.rating < 8:
            return "Average"
        else:
            return "Flop"

class Cinema:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)

    def display_movies(self):
        for m in self.movies:
            print(f"Name: {m.name}, Rating: {m.rating}, Ticket Price: {m.ticket_price}, Category: {m.category()}")

# Example usage
cinema = Cinema()
cinema.add_movie(Movie("Inception", 9, 250))
cinema.add_movie(Movie("Random Comedy", 6, 150))
cinema.add_movie(Movie("Unknown Film", 3, 100))
cinema.display_movies()
