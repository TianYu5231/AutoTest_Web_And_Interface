# coding=utf-8
# @Author: yutian
# @Version: Python 3.7
# @File: conftest.py
# @Date: 2022/5/22 20:02
# @SoftWare: PyCharm
import pytest
from selenium import webdriver

from utils.logger import log

driver = None


@pytest.fixture(scope='session')
def drivers():
    """启动浏览器驱动"""
    global driver
    if driver is None:
        driver = webdriver.Chrome()
    yield driver
    log.info('退出浏览器')
    driver.quit()

