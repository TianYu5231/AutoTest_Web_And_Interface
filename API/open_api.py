# coding=utf-8
# @Author: yutian
# @Version: Python 3.7
# @File: open_api.py
# @Date: 2022/5/31 22:27
# @SoftWare: PyCharm
from utils.Requests import request

# 引用-开放平台api接口-测试
# https://api.apiopen.top/swagger/index.html
from utils.logger import log


def get_sentences():
    """
    随机获取一言名言
    :return:
    """
    result = request.get('https://api.apiopen.top/api/sentences')
    return result

