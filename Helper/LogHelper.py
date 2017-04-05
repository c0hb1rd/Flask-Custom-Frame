from Config import LOG_PATH
from Helper.TimeHelper import TimeHelper


class LogHelper:

    def __init__(self):
        pass

    @staticmethod
    def read():
        with open(LOG_PATH, 'r') as f:
            for line in f.readlines():
                yield line

    @staticmethod
    def write(info):
        date = TimeHelper.formatTime(TimeHelper.getStamp())
        with open(LOG_PATH, 'a') as f:
            f.write(date + '\t' + info + '\n')

    @staticmethod
    def clear():
        with open(LOG_PATH, 'w') as f:
            f.close()
