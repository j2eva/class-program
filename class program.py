class ticket:
    def __init__(self, theatername, price, moviename, seatnumber):
        self.theatername = theatername
        self.price = price
        self.moviename = moviename
        self.seatnumber = seatnumber

p1 = ticket("srisakthi", 250, "varisu", "j12")
print(p1.theatername)
print(p1.price)
print(p1.moviename)
print(p1.seatnumber)
