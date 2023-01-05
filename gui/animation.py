from PIL import Image, ImageTk

from gui.common import asset_path


class Animation:
    def __init__(self, description):
        self.__frames = []

        for frame_description in description:
            self.__frames.append({
                "image": self.__load_image(frame_description["image"]),
                "len": frame_description["len"]
            })

        self.__frame_num = 0
        self.__frames_done = 0

    def __load_image(self, path):
        img = Image.open(asset_path(path)).resize((100,100))
        return ImageTk.PhotoImage(img)

    def get_image(self):
        self.__frames_done += 1
        current_frame = self.__frames[self.__frame_num]

        if self.__frames_done == current_frame['len']:
            self.__frames_done = 0
            self.__frame_num = (self.__frame_num + 1) % len(self.__frames)

        return current_frame["image"]

    def reset(self):
        self.__frames_done = 0
        self.__frame_num = 0
