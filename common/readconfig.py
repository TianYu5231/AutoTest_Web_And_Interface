# coding=utf-8
# @Author: yutian
# @Version: Python 3.7
# @File: readconfig.py
# @Date: 2022/5/22 11:10
# @SoftWare: PyCharm
import configparser

from config.conf import cm


class ReadConfig(object):

    def __init__(self):
        self.config = configparser.RawConfigParser()
        self.config.read(cm.ini_file, encoding='utf-8')

    def _get(self, section, option):
        return self.config.get(section, option)

    def _set(self, section, option, value):
        self.config.set(section, option, value)
        with open(cm.ini_file, 'w') as f:
            self.config.write(f)

    @property
    def url(self):
        return self._get('HOST', 'url')


read_ini = ReadConfig()
