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
    headers = {
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/101.0.4951.54 Safari/537.36 '
    }
    global driver
    if driver is None:
        driver = webdriver.Chrome()
        opt = webdriver.ChromeOptions()
        # 模拟真实用户浏览器访问
        opt.add_argument(f'--user-agent={headers}')
    yield driver
    log.info('退出浏览器')
    driver.quit()

