# coding=utf-8
# @Author: yutian
# @Version: Python 3.7
# @File: test_baidu.py
# @Date: 2022/5/22 19:42
# @SoftWare: PyCharm
import time

import pytest
from selenium import webdriver

from common.readconfig import read_ini
from page_objects.baidu_page import BaiduPage


class TestBaidu(object):
    @pytest.fixture(autouse=True)
    def open_baidu(self, drivers):
        baidu_page = BaiduPage(drivers)
        baidu_page.get_url(read_ini.url)

    def test_01(self, drivers):
        baidu_page = BaiduPage(drivers)
        baidu_page.input_search('python')
        baidu_page.click_search()
        assert baidu_page.title_exist('python')


if __name__ == '__main__':
    pytest.main(['test_baidu.py'])
