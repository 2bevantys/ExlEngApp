from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class ExlEngApp(MDApp):
    def build(self):
        return MDLabel(text="Hello, Words", halign="center")


if __name__ == "__main__":
    ExlEngApp().run()
