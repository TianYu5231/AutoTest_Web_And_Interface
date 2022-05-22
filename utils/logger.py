# coding=utf-8
# @Author: yutian
# @Version: Python 3.7
# @File: logger.py
# @Date: 2022/5/22 13:53
# @SoftWare: PyCharm
import logging

# 控制台输出日志颜色
import colorlog

from config.conf import cm

console_log_color = {
    'DEBUG': 'white',
    'INFO': 'green',
    'WARNING': 'yellow',
    'ERROR': 'red',
    'CRITICAL': 'bold_red',
}


class Log(object):
    def __init__(self):
        self.logger = logging.getLogger()

        self.logger.setLevel(logging.DEBUG)

        file_handler = logging.FileHandler(cm.log_file, encoding='utf-8')
        file_handler.setLevel(logging.INFO)

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)

        file_formatter = logging.Formatter(self.file_fmt)
        file_handler.setFormatter(file_formatter)

        console_formatter = colorlog.ColoredFormatter(self.console_fmt, log_colors=console_log_color)
        console_handler.setFormatter(console_formatter)

        if not self.logger.handlers:
            self.logger.addHandler(file_handler)
            self.logger.addHandler(console_handler)

    @property
    def file_fmt(self):
        return '[%(asctime)s] %(filename)s -> line:%(lineno)d [%(levelname)s]: %(message)s'

    @property
    def console_fmt(self):
        return '%(log_color)s[%(asctime)s] %(filename)s -> line:%(lineno)d [%(levelname)s]: %(message)s'


log = Log().logger
if __name__ == '__main__':
    log.info('Hello World')
