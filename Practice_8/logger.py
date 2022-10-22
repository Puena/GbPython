import datetime
_filename = "unnamed.log"


def init(filename: str):
    global _filename
    _filename = filename


def log_info(message: str):
    global _filename
    with open(_filename, 'a') as f:
        f.write(str(datetime.datetime.now()) + " " + message + "\n")
