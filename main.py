from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from database import DataBase
from kivy.graphics import Color, Rectangle
from kivy.resources import resource_add_path
import Long
import Long_back
import Pick
import Pick_back
import Small
import Small_back


class CreateAccountWindow(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count("@") == 1 and self.email.text.count(".") > 0:
            if self.password != "":
                db.add_user(self.email.text, self.password.text, self.namee.text)

                self.reset()

                sm.current = "login"
            else:
                invalidForm()
        else:
            invalidForm()

    def login(self):
        self.reset()
        sm.current = "login"


    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""


class LoginWindow(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def loginBtn(self):
        if db.validate(self.email.text, self.password.text):
            MainWindow.current = self.email.text
            self.reset()
            sm.current = "main"
        else:
            invalidLogin()

    def createBtn(self):
        self.reset()
        sm.current = "create"

    def reset(self):
        self.email.text = ""
        self.password.text = ""


class MainWindow(Screen):
    n = ObjectProperty(None)
    created = ObjectProperty(None)
    email = ObjectProperty(None)
    current = ""

    def logOut(self):
        sm.current = "login"

    def on_enter(self, *args):
        password, name, created = db.get_user(self.current)
        self.n.text = "姓名: " + name
        self.email.text = "電子郵件: " + self.current
        self.created.text = "創建於: " + created


class BadmintonWindow(Screen):
    pass
class FirstWindow(Screen):
    pass

class SecondWindow(Screen):
    def Long_ball(self):
        Long.long()
        sm.current = "second"

    def Long_ball_back(self):
        Long_back.long_back()
        sm.current = "second"

    def Pick_ball(self):
        Pick.pick()
        sm.current = "second"

    def Pick_ball_back(self):
        Pick_back.pick_back()
        sm.current = "second"
    def Small_ball(self):
        Small.small()
        sm.current = "second"
    def Small_ball_back(self):
        Small_back.small_back()
        sm.current = "second"

class WindowManager(ScreenManager):
    pass


def invalidLogin():
    pop = Popup(title='登入失敗', title_font='SourceHanSerifTW-Regular.otf',
                content=Label(text='帳號或密碼有誤', font_name='SourceHanSerifTW-Regular.otf'),
                size_hint=(None, None), size=(400, 400))
    pop.open()


def invalidForm():
    pop = Popup(title='格式錯誤', title_font='SourceHanSerifTW-Regular.otf',
                content=Label(text='請輸入正確的格式', font_name='SourceHanSerifTW-Regular.otf'),
                size_hint=(None, None), size=(400, 400)),

    pop.open()


kv = Builder.load_file("my.kv")

sm = WindowManager()
db = DataBase("users.txt")

screens = [LoginWindow(name="login"), CreateAccountWindow(name="create"), MainWindow(name="main"),
            BadmintonWindow(name="badminton"), FirstWindow(name="first"), SecondWindow(name="second")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "login"


class MyMainApp(App):
    def build(self):
        return sm


if __name__ == "__main__":
    MyMainApp().run()