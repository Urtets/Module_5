import hashlib
import time


class User:
    def __init__(self, nickname, password, confirm_pass, age=0):
        self.nickname = nickname
        if password == confirm_pass:
            self.password = hash(password)
        self.age = age

    def __str__(self):
        return self.nickname

    def __eq__(self, other):
        if isinstance(other, User):
            return self.nickname == other.nickname
        elif isinstance(other, str):
            return self.nickname == other


class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __str__(self):
        return self.title


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def register(self, nickname, password, password_confirm, age):
        # if password != passwrod_confirm:
        #     checker = True
        #     while checker:
        #         print("Your passwords don't match. Try again: ")
        #         password = input("Enter your password: ")
        #         passwrod_confirm = input("Confirm your password: ")
        #         if password == passwrod_confirm:
        #             checker = False

        for user in self.users:
            if user == nickname:
                print(f'Пользователь {nickname} уже существует')
                return
        new_user = User(nickname, password, password_confirm, age)
        self.users.append(new_user)
        self.log_in(nickname, password)


    def log_in(self, nickname, password):
        hashed_pass = hash(password)
        for user in self.users:
            if user == nickname and user.password == hashed_pass:
                self.current_user = user
                break
                # self.entered_tube()

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        if len(self.videos) == 0:
            self.videos = list(args)
        else:
            for item in args:
                for video in self.videos:
                    if video.title == item.title:
                        print("Such video exists")
                    else:
                        self.videos.append(item)

    def get_videos(self, any_words):
        # print(self.videos)
        line = []
        for video in self.videos:
            if any_words.lower() in video.title.lower():
                line.append('\n' + video.title)
        return line

    def watch_video(self, video_title):
        if self.current_user == None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return
        for video in self.videos:
            if video.title == video_title:
                if self.access_check(video.adult_mode, self.current_user.age):
                    print("Вам нет 18, чтобы смотреть это видео")
                    return

                counter = ''
                for i in range(video.duration):
                    counter = counter + str(i + 1) + ' '
                print(counter + ' Конец видео')

    # secondary functions

    def access_check(self, adult_mode, age):
        if adult_mode and age < 18:
            return False
        else:
            return True

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
