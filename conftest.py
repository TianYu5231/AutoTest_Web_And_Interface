# coding=utf-8
# @Author: yutian
# @Version: Python 3.7
# @File: conftest.py
# @Date: 2022/5/22 09:42
# @SoftWare: PyCharm
import base64
import os.path

import allure
import pytest

from config.conf import cm
from utils.logger import log

driver = None


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    n_pytest_html = item.config.pluginmanager.getplugin('html')
    out = yield
    report = out.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call':
        log.info('测试报告: {}'.format(report))
        log.info('步骤: {}'.format(report.when))
        log.info('node_id: {}'.format(report.nodeid))
        if report.failed:
            log.error('运行结果: {}'.format(report.outcome))
        else:
            log.info('运行结果: {}'.format(report.outcome))

    if report.when == 'call' and report.failed:
        screen_img = _capture_screenshot()
        if screen_img:
            log.info('pytest_html添加截图')
            html_line = f'<div><img src="data:image/png;base64,{screen_img}" alt="screenshot" ' \
                        'style="width:1024px;height:768px;" onclick="window.open(this.src)" align="right"></div>'

            extra.append(n_pytest_html.extras.html(html_line))
        report.extra = extra


def pytest_configure(config):
    """修改html配置"""
    # 修改html存放路径
    if config.getoption('--html'):
        report_path = cm.log_file[1]
        config.option.htmlpath = os.path.join(report_path, config.getoption('--html'))


def _capture_screenshot():
    """失败截图保存"""
    screen_path = cm.screen_path()
    if hasattr(driver, 'get_screenshot_as_file'):
        driver.get_screenshot_as_file(screen_path)
        with allure.step('添加失败截图'):
            log.info('allure添加失败截图')
            allure.attach(screen_path, '失败截图', allure.attachment_type.PNG)
        with open(screen_path, 'rb') as f:
            img_base64 = base64.b64encode(f.read())
        return img_base64.decode()
    return None


def pytest_html_report_title(report):
    """修改测试报告html的title"""
    report.title = 'Web & API 测试报告'
