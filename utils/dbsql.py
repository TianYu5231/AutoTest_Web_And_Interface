# coding=utf-8
# @Author: yutian
# @Version: Python 3.7
# @File: dbsql.py
# @Date: 2022/5/30 22:06
# @SoftWare: PyCharm
import pymysql

from common.readyaml import read_yaml
from utils.logger import log


class DBMysql(object):
    """封装mysql"""
    def __init__(self, db_name):
        db_info = read_yaml.load_yml()[db_name]
        host = db_info['host']
        port = 3306
        user = db_info['user_name']
        password = db_info['password']
        database = db_info['db_name']
        try:
            self.conn = pymysql.connect(host=host, port=port, user=user,
                                        password=password, database=database)
            self.cursor = self.conn.cursor()
        except Exception as e:
            log.error('数据库连接错误: {}, \n {}'.format(db_info, e))

    def query(self, sql):
        """数据库查询功能"""
        log.info('执行sql:{}'.format(sql))
        self.cursor.execute(sql)
        query_result = self.cursor.fetchall()
        log.info('查询结果:{}'.format(query_result))
        return query_result[0]


db_domain = DBMysql('learnJDBC')
if __name__ == '__main__':
    db_domain.query('select * from students')
