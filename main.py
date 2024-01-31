class Passport:
    def __init__(self, series, number, full_name):
        self.series = series
        self.number = number
        self.full_name = full_name

    def dispay_info(self):
        print(f"Passport information: \nSeries: {self.series}\nNumber: {self.number}\nFull name: {self.full_name}")

class ForeignPassport(Passport):
    def __init__(self, series, number, full_name, name_visa, passport_number):
        super().__init__(series, number, full_name)
        self.name_visa = name_visa
        self.passport_number = passport_number

    def dispay_info(self):
        super().dispay_info()
        print(f"Foreign Passport Information:\nVisa Info: {self.name_visa}\nForeign Passport Number: {self.passport_number}")

passport = Passport("SA", 34532, "Antony")
passport.dispay_info()

print("\n")
foreign_passprot = ForeignPassport("SA", 231252, "Antony", "UK", 34532)
foreign_passprot.dispay_info()