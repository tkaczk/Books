class User:

    def __init__(self, first_name, last_name, city, job, hobby):
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.job = job
        self.hobby = hobby
        self.login_attempts = 0

    def describe_user(self):
        print(f'{self.first_name} {self.last_name} mieszka w {self.city}.\nZawód: {self.job}.\nHobby: {self.hobby}')

    def greet_user(self):
        print(f'{self.first_name}! Miło Ciebie widzieć!')

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Privileges:
    def __init__(self, privileges=('Can add post', 'Can delete post', 'Right to ban user')):
        self.privileges = privileges

    def show_privileges(self):
        print(self.privileges)


class Admin(User):
    def __init__(self, first_name, last_name, city, job, hobby):
        super().__init__(first_name, last_name, city, job, hobby)
        self.privileges = Privileges()


master_admin = Admin('Chris', 'Weaver', 'Capitol', 'administrator', 'crushing noobs')

me = User('Krzysiek', 'Tkacz', 'Warszawa', 'bezrobotny', 'gry komputerowe')
# kasia = User('Kasia', 'Tytkowska-Tkacz', 'Warszawa', 'HR system admin', 'ogrodnictwo')

# me.describe_user()
# # kasia.describe_user()
# me.greet_user()
# kasia.greet_user()


# me.increment_login_attempts()
# me.increment_login_attempts()
# me.increment_login_attempts()
# print(f'Podjęto {me.login_attempts} próby zalogowania się.')
# me.reset_login_attempts()
# print(me.login_attempts)

master_admin.describe_user()
master_admin.privileges.show_privileges()
