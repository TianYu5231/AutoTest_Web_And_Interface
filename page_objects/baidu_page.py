# coding=utf-8
# @Author: yutian
# @Version: Python 3.7
# @File: baidu_page.py
# @Date: 2022/5/22 16:10
# @SoftWare: PyCharm
from pages.webpage import WebPage
from utils.times import sleep


class BaiduPage(WebPage):
    """百度页面类"""
    def input_search(self, content):
        """输入搜索内容"""
        self.input_text('id=kw', txt=content)
        sleep()

    def click_search(self):
        """点击搜索"""
        self.to_click('id=su')
        sleep()

    def title_exist(self, txt):
        return self.title_contains(txt)
