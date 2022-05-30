# coding=utf-8
# @Author: yutian
# @Version: Python 3.7
# @File: readyaml.py
# @Date: 2022/5/30 22:24
# @SoftWare: PyCharm
import os.path

import yaml


class ReadYaml(object):
    def __init__(self):
        # 初始化db_common.yml文件的路径
        self.yaml_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                                      'config', 'db_common.yml')

    def load_yml(self):
        """加载yml配置文件"""
        with open(self.yaml_path, 'r', encoding='utf-8') as yo:
            data = yaml.load(yo, Loader=yaml.FullLoader)
        return data


read_yaml = ReadYaml()
if __name__ == '__main__':
    print(read_yaml.load_yml()['learnJDBC'])
