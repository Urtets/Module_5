import hashlib
import time


class User:
    def __init__(self, nickname, password, confirm_pass, age=0):
        self.nickname = nickname
        if hash(password) == hash(confirm_pass):
            self.password = hash(password)
        self.age = age

    def __str__(self):
        return self.nickname

    def __hash__(self):
        return hash(self.password)


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return self.title


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def register(self, nickname, password, passwrod_confirm, age):
        # if password != passwrod_confirm:
        #     checker = True
        #     while checker:
        #         print("Your passwords don't match. Try again: ")
        #         password = input("Enter your password: ")
        #         passwrod_confirm = input("Confirm your password: ")
        #         if password == passwrod_confirm:
        #             checker = False

        some_user = User(nickname, password, passwrod_confirm, age)
        if len(self.users) > 0:
            for user in self.users:
                if user.nickname == nickname:
                    print(f'Пользователь {nickname} уже существует')
                    return
                else:
                    self.users.append(some_user)
                    self.log_in(nickname, password)
        else:
            self.users.append(some_user)
            self.log_in(nickname, password)

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.password == hash(password):
                self.current_user = user
                break
                # self.entered_tube()
            else:
                print("Access denied.")

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        if len(self.videos) == 0:
            self.videos = args
        else:
            for item in args:
                for video in self.videos:
                    if video.title == item.title:
                        print("Such video exists")
                    else:
                        self.videos.append(item)

    def get_videos(self, any_words):
        print("See what we have found for you: ")
        # print(self.videos)
        line = []
        for video in self.videos:
            if any_words.lower() in video.title.lower():
                line.append(video.title)
        for video in line:
            print(video)

    def watch_video(self, video_title):
        if self.current_user == None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return
        if self.current_user.adult_mode and self.current_user.age < 18:
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
        else:
            for video in self.videos:
                if video.title == video_title:
                    counter = ''
                    for i in range(video.duration):
                        counter = counter + str(i + 1) + ' '
                    print(counter + ' Конец видео')

    # secondary functions

    # def entered_tube(self):
    #     exit_button = True
    #     while exit_button:
    #         choice = input("Choose action: 1 - Search, 2 - Watch a video, 3 - log out: ")
    #         if choice == 1:
    #             text = input("Enter text: ")
    #             self.get_videos(text)
    #         if choice == 2:
    #             text = input("Enter exact name: ")
    #             self.watch_video(text)
    #         if choice == 3:
    #             exit()
    #
    # def lobby(self):
    #     while True:
    #         choice = int(input("Please, choose 1 for log in or 2 for registration: "))
    #         if choice == 1:
    #             self.log_in(input("Enter your nickname: "), hash(input("Enter your password: ")))
    #         if choice == 2:
    #             self.register(input("Enter your nickname: "), hash(input("Enter your password: ")),
    #                           hash(input("Confirm your password: ")), int(input("Enter your age: ")))
    #
    # def hash_coder(self, some_password):
    #     coded_password = hashlib.sha512(some_password.encode('UTF-8'))
    #     return coded_password
