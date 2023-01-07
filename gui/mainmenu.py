from gui.screen import Screen


class MainMenu:
    def __init__(self, screen: Screen):
        self.__screen = screen
        self.__weidth = 0
        self.__hight = 0

    def draw_main(self):
        main = self.__screen.add_object(
            self.__screen.canvas.create_text(self.__screen.width / 2, self.__screen.height - self.__screen.height * 0.1,
                                             text="MainMenu"))

    def start_main(self):
        self.__main = MainMenu(self.__screen)

        self.__screen.window.after(20)

        mainloop()