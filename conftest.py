# coding=utf-8
# @Author: yutian
# @Version: Python 3.7
# @File: conftest.py
# @Date: 2022/5/22 09:42
# @SoftWare: PyCharm
import allure
import pytest
from selenium import webdriver

from utils.logger import log

driver = None


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    out = yield
    report = out.get_result()

    if report.when == 'call':
        log.info('测试报告: {}'.format(report))
        log.info('步骤: {}'.format(report.when))
        log.info('node_id: {}'.format(report.nodeid))
        log.info('运行结果: {}'.format(report.outcome))

    if report.when == 'call' and report.failed:
        if hasattr(driver, 'get_screenshot_as_png'):
            with allure.step('添加失败截图'):
                log.info('添加失败截图')
                allure.attach(driver.get_screenshot_as_png(), '失败截图', allure.attachment_type.PNG)


@pytest.fixture(scope='session')
def browser():
    """启动浏览器驱动"""
    global driver
    if driver is None:
        driver = webdriver.Chrome()
    yield driver
    log.info('退出浏览器')
    driver.quit()

