import importlib.resources
from cool_lib import data

print("i am b")


def load_some_data():
    return importlib.resources.open_text(data, "some-data.txt")
