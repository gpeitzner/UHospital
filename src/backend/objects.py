class User:
    def __init__(self, first_name, last_name, date, gender, nickname, password, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.date = date
        self.gender = gender
        self.nickname = nickname
        self.password = password
        self.phone = phone


class Medicine:
    def __init__(self, name, price, description, quantity):
        self.name = name
        self.price = price
        self.description = description
        self.quantity = quantity
