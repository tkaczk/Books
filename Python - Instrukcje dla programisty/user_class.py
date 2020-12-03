class User:

    def __init__(self, first_name, last_name, city, job, hobby):
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.job = job
        self.hobby = hobby

    def describe_user(self):
        print(f'{self.first_name} {self.last_name} mieszka w {self.city}.\nZawód: {self.job}.\nHobby: {self.hobby}')

    def greet_user(self):
        print(f'{self.first_name}! Miło Ciebie widzieć!')


me = User('Krzysiek', 'Tkacz', 'Warszawa', 'bezrobotny', 'gry komputerowe')
kasia = User('Kasia', 'Tytkowska-Tkacz', 'Warszawa', 'HR system admin', 'ogrodnictwo')


me.describe_user()
kasia.describe_user()
me.greet_user()
kasia.greet_user()
