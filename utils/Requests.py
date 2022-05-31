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
    @staticmethod
    def get(url, **kwargs):
        params = kwargs.get('params')
        headers = kwargs.get('headers')
        try:
            log.info('get请求: [{}]'.format(url))
            result = requests.get(url, params=params, headers=headers)
            log.info('返回: {}'.format(result.json()))
            return result.json()
        except Exception as e:
            log.error('url={}, get请求错误: \n {}'.format(url, e))

    @staticmethod
    def post(url, **kwargs):
        params = kwargs.get('params')
        data = kwargs.get('data')
        json = kwargs.get('json')
        try:
            log.info('post请求: [{}]'.format(url))
            result = requests.post(url, params=params, data=data, json=json)
            log.info('返回: {}'.format(result.json()))
            return result.json()
        except Exception as e:
            log.error('url={}, post请求错误: {}'.format(url, e))


request = Request()
if __name__ == '__main__':
    res = request.get('https://api.apiopen.top/api/sentences')
    print(res)
