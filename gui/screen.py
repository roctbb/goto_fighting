from tkinter import Tk, Canvas


class Screen:
    def __init__(self, window):
        w, h = window.winfo_screenwidth(), window.winfo_screenheight()
        canvas = Canvas(window, width=w, height=h)
        canvas.pack()
        self.__canvas = canvas
        self.__objects = []

        canvas.configure(bg='white')


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
        for obj in self.__objects:
            self.__canvas.delete(obj)
        self.__objects = []
