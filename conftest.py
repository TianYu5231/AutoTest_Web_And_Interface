# coding=utf-8
# @Author: yutian
# @Version: Python 3.7
# @File: conftest.py
# @Date: 2022/5/22 09:42
# @SoftWare: PyCharm
import os.path

import allure
import pytest

from config.conf import cm
from utils.logger import log

driver = None


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    out = yield
    report = out.get_result()

    if report.when == 'call':
        log.info('测试报告: {}'.format(report))
        log.info('步骤: {}'.format(report.when))
        log.info('node_id: {}'.format(report.nodeid))
        if report.failed:
            log.error('运行结果: {}'.format(report.outcome))
        else:
            log.info('运行结果: {}'.format(report.outcome))

    if report.when == 'call' and report.failed:
        if hasattr(driver, 'get_screenshot_as_png'):
            with allure.step('添加失败截图'):
                log.info('添加失败截图')
                allure.attach(driver.get_screenshot_as_png(), '失败截图', allure.attachment_type.PNG)


def pytest_configure(config):
    """修改html报告路径"""
    if config.getoption('--html'):
        report_path = cm.log_file[1]
        config.option.htmlpath = os.path.join(report_path, config.getoption('--html'))


@pytest.fixture(scope='session')
def screen():
    print('测试')