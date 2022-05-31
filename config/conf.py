# coding=utf-8
# @Author: yutian
# @Version: Python 3.7
# @File: conf.py
# @Date: 2022/5/22 10:09
# @SoftWare: PyCharm
import os.path

from utils.times import t_strftime


class ConfigManager(object):
    # 项目根目录
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # 失败截图目录
    @property
    def screen_path(self):
        """截图目录"""
        screen_dir = os.path.join(self.BASE_DIR, 'screen_capture')
        if not os.path.exists(screen_dir):
            os.makedirs(screen_dir)
        screen_file = os.path.join(screen_dir, '{}.png'.format(t_strftime()))
        return screen_file

    # 报告/日志
    @property
    def log_file(self):
        """
        日志文件
        :return:
        """
        log_dirs = os.path.join(self.BASE_DIR, 'Reports', t_strftime())
        if not os.path.exists(log_dirs):
            os.makedirs(log_dirs)
        return os.path.join(log_dirs, '{}.log'.format(t_strftime())), log_dirs

    @property
    def ini_file(self):
        """
        获取config.ini文件
        :return:
        """
        _ini_file = os.path.join(self.BASE_DIR, 'config', 'config.ini')
        if not os.path.exists(_ini_file):
            raise FileNotFoundError('配置文件 {} 不存在!'.format(_ini_file))
        return _ini_file


cm = ConfigManager()
if __name__ == '__main__':
    print(cm.BASE_DIR)
    print(cm.ini_file)
