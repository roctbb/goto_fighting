from tkinter import Tk, Canvas


class Screen:
    def __init__(self, window):
        w, h = window.winfo_screenwidth(), window.winfo_screenheight()
        canvas = Canvas(window, width=w, height=h)
        canvas.pack()
        self.__canvas = canvas
        self.__objects = []
        self.__window = window
        self.__frames = 0
        canvas.configure(bg='white')

    @property
    def frames(self):
        return self.__frames

    def reset(self):
        self.clear()
        self.__frames = 0

    @property
    def width(self):
        return self.__canvas.winfo_width()

    @property
    def height(self):
        return self.__canvas.winfo_height()

    @property
    def canvas(self):
        return self.__canvas

    def add_object(self, obj):
        self.__objects.append(obj)

    def clear(self):
        self.__frames += 1

        for obj in self.__objects:
            self.__canvas.delete(obj)
        self.__objects = []

    @property
    def window(self):
        return self.__window
