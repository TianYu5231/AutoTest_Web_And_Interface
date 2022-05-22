# coding=utf-8
# @Author: yutian
# @Version: Python 3.7
# @File: test_baidu.py
# @Date: 2022/5/22 19:42
# @SoftWare: PyCharm
import pytest

from page_objects.baidu_page import BaiduPage


class TestBaidu:
    def test_01(self):
        baidu_page = BaiduPage(driver=drivers)
        baidu_page.input_search('python')
        baidu_page.click_search()
        assert baidu_page.title_is('python')


if __name__ == '__main__':
    pytest.main(['test_baidu.py'])
