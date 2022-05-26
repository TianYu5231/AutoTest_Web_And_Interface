# coding=utf-8
# @Author: yutian
# @Version: Python 3.7
# @File: webpage.py
# @Date: 2022/5/22 14:25
# @SoftWare: PyCharm
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utils.logger import log
from utils.times import sleep


class WebPage(object):
    """web基类"""

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 20
        self.wait = WebDriverWait(self.driver, self.timeout)

    def get_url(self, url):
        """打开网页url"""
        self.driver.maximize_window()
        try:
            self.driver.get(url)
            self.driver.implicitly_wait(10)
            log.info('打开网页: {}'.format(url))
        except TimeoutError:
            raise TimeoutError('打开{}超时，请检查网络或者网址'.format(url))

    @staticmethod
    def element_split(locator):
        try:
            by, value = locator.split('=')
            if by == 'id':
                by = By.ID
            elif by == 'class':
                by = By.CLASS_NAME
            elif by == 'name':
                by = By.NAME
            elif by == 'tag_name':
                by = By.TAG_NAME
            elif by == 'link_text':
                by = By.LINK_TEXT
            elif by == 'xpath':
                by = By.XPATH
            elif by == 'css':
                by = By.CSS_SELECTOR
            return by, value
        except Exception as e:
            log.error('{}不存在，eg: id=i. {}'.format(locator, e))

    def find_element(self, locator):
        """查找单个元素"""
        by, value = self.element_split(locator)
        return self.driver.find_element(by=by, value=value)

    def find_elements(self, locator):
        """查找多个元素"""
        by, value = self.element_split(locator)
        return self.driver.find_elements(by=by, value=value)

    def input_text(self, locator, txt):
        """输入"""
        sleep(0.5)
        element = self.find_element(locator)
        element.clear()
        element.send_keys(txt)
        log.info('输入文本: {}'.format(txt))

    def to_click(self, locator):
        """点击"""
        self.find_element(locator).click()
        sleep(0.5)
        log.info('点击元素: {}'.format(locator))

    def get_element_txt(self, locator):
        """获取当前文本"""
        txt = self.find_element(locator).text
        log.info('获取文本: {}'.format(txt))
        return txt

    @property
    def get_page_source(self):
        """获取页面源码"""
        log.info('获取页面源码')
        return self.driver.page_source()

    def refresh(self):
        """刷新页面"""
        log.info('刷新页面')
        self.driver.refresh()
        self.driver.implicitly_wait(10)

    def double_click(self, locator):
        """鼠标双击"""
        ele = self.find_element(locator)
        ActionChains(self.driver).double_click(ele).perform()

    def title_is(self, txt):
        """判断title"""
        return EC.title_is(txt)(self.driver)

    def title_contains(self, txt):
        """是否包含title"""
        return EC.title_contains(txt)(self.driver)

    def alert_is_present(self):
        """判断弹窗存在"""
        return EC.alert_is_present()(self.driver)

    def get_current_win_handle(self):
        """获取当前handle句柄"""
        return self.driver.current_handle()

    def switch_to_window_by_title(self, title):
        """根据title切换窗口"""
        for handle in self.driver.window_handles:
            if self.driver.title == title:
                self.driver.switch_to.window(handle)


