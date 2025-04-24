from consts import FILENAME


def write_name_screen(name):
    with open(FILENAME, "w", encoding="utf-8") as f:
        f.write(name)


def read_name_screen():
    with open(FILENAME, "r", encoding="utf-8") as f:
        return f.read().strip()