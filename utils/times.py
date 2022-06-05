# coding=utf-8
# @Author: yutian
# @Version: Python 3.7
# @File: times.py
# @Date: 2022/5/22 10:21
# @SoftWare: PyCharm
import time


def timestamp():
    """
    整型时间戳
    :return:
    """
    return round(time.time())


def t_strftime(fmt='%Y%m%d_%H%M%S'):
    """
    获取str格式化时间
    :param fmt: 输出时间格式
    :return: 返回格式化时间
    """
    return time.strftime(fmt, time.localtime())


def sleep(sec=1):
    time.sleep(sec)
