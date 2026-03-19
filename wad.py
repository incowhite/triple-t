
class Ticket:
    def __init__(self, movie, price, quantity, language="Georgian"):
        self.movie = movie
        self.price = price
        self.quantity = quantity
        self.language = language
    def __str__(self):
        return f"{self.movie} - {self.price}₾ (left: {self.quantity})"
    def __gt__(self, other):
        if isinstance(other, Ticket):
            return self.quantity > other.quantity
        return self.quantity > other
    def __lt__(self, other):
        if isinstance(other, Ticket):
            return self.quantity < other.quantity
        return self.quantity < other
class User:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
    def __str__(self):
        return f"{self.name} - {self.balance}₾"
    def deposit(self, amount):
        self.balance += amount
        print(f"Added {amount}₾, now you have {self.balance}₾")
    def buy(self, ticket, how_many):
        if how_many <= 0:
            print("Please enter number 1 or more")
            return
        total_price = ticket.price * how_many
        if how_many > ticket.quantity:
            print(f"Only {ticket.quantity} tickets left for {ticket.movie}")
            return
        if total_price > self.balance:
            print(f"Not enough money! Need {total_price}₾ but you have {self.balance}₾")
            return
        self.balance -= total_price
        ticket.quantity -= how_many
        print(f"You bought {how_many} ticket(s) for {ticket.movie}")
        print(f"Balance left: {self.balance}₾")