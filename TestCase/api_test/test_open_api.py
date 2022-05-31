# coding=utf-8
# @Author: yutian
# @Version: Python 3.7
# @File: test_open_api.py
# @Date: 2022/5/31 22:41
# @SoftWare: PyCharm
import pytest

from API.open_api import get_sentences


class TestOpenApi(object):
    def test_sentences(self):
        result = get_sentences()
        assert result['code'] == 200
        assert result['message'] == '成功!'


if __name__ == '__main__':
    pytest.main(['test_open_api.py'])
