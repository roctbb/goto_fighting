import os
import pathlib


def asset_path(asset):
    return str(pathlib.Path(__file__).parent.resolve()) + os.sep + ".." + os.sep + "assets" + os.sep + asset.lstrip('/').replace('/', os.sep)
