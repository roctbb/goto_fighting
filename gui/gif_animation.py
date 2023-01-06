from PIL import Image, ImageTk

from gui.common import asset_path


class GifAnimation:
    def __init__(self, filename, size=(100, 100), flip=False):
        self.image = self.__load_image(filename)

        self.__frames = []

        for i in range(self.image.n_frames):
            self.image.seek(i)
            self.__frames.append(ImageTk.PhotoImage(self.image.resize(size)))

        self.__frame_num  = 0

    def __load_image(self, path):
        return Image.open(asset_path(path))

    def get_image(self):
        current_frame = self.__frames[self.__frame_num]
        self.__frame_num = (self.__frame_num + 1) % len(self.__frames)
        return current_frame

    def reset(self):
        self.__frame_num  = 0

