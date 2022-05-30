# coding=utf-8
# @Author: yutian
# @Version: Python 3.7
# @File: Requests.py
# @Date: 2022/5/30 21:35
# @SoftWare: PyCharm
import requests

from utils.logger import log


class Request(object):
    """封装requests"""
    def get(self, url, **kwargs):
        params = kwargs.get('params')
        headers = kwargs.get('headers')
        try:
            result = requests.get(url, params=params, headers=headers)
            return result.json()
        except Exception as e:
            log.error('url={}, get请求错误: {}'.format(url, e))

    def post(self, url, **kwargs):
        params = kwargs.get('params')
        data = kwargs.get('data')
        json = kwargs.get('json')
        try:
            result = requests.post(url, params=params, data=data, json=json)
            return result.json()
        except Exception as e:
            log.error('url={}, post请求错误: {}'.format(url, e))


request = Request()
if __name__ == '__main__':
    res = request.get('http://127.0.0.1:8000/')
    print(res['message'])
