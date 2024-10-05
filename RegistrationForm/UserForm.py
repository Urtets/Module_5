class Database:
    def __init__(self):
        self.data = {}

    def add_user(self, username, password):
        self.data[username] = password


class User:
    """
    Класс пользователя, содержащий атрибуты: логин и пароль
    """

    def __init__(self, username, password, password_confirmation):
        self.username = username
        if password == password_confirmation:
            self.password = password


def check_password(password: str):
    counter = 0
    while counter != 2:
        if (password.isalpha() == False and password.islower() == False and
                password.isupper() == False and password.isdigit() == False):
            counter = 1
        else:
            print("Пароль должен включать Заглавные и строчные буквы, а так же цифры")
            password = input("Попробуйте ещё раз: ")
        if len(password) > 8:
            counter = 2
        else:
            print("Пароль должен содержать не менее 8 символов")
            password = input("Попробуйте ещё раз: ")
    return password


if __name__ == '__main__':
    database = Database()
    while True:
        choice = int(input("Приветствую! Выберите действие: \n1 - Вход\n2 - Регистрация\n"))
        if choice == 1:
            login = input("Введите логин: ")
            password = input("Введите пароль: ")
            if login in database.data:
                if password == database.data[login]:
                    print(f'Вход выполнен, {login}')
                    break
                else:
                    print("Неверный пароль!")
            else:
                print("Пользователь не найден.")

        if choice == 2:
            user = User(input("Введите логин: "), password := check_password(input("Введите пароль: ")),
                        password2 := input("Повторите пароль: "))
            if password != password2:
                print("Пароли не совпадают, попробуйте ещё раз.")
                continue
            database.add_user(user.username, user.password)
        print(database.data)
