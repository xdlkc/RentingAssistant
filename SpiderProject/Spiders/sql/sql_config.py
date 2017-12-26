# coding=utf-8
__author__ = 'lkc'
import psycopg2
from ..tools.print_log import *


def config():

    config = {
        'host': 'localhost',
        'user': 'postgres',
        'password': 'wimness',
        'dbname': 'postgres',
        'port': 54321
    }
    return config


def connect_db():
    return psycopg2.connect(**config())


def init_table(judge_table_sql, create_table_sql, create_index_sql):
    """
    检测->建表->建索引
    :param judge_table_sql:
    :param create_table_sql:
    :param create_index_sql:
    :return:
    """
    conn = connect_db()
    cur = conn.cursor()
    try:
        cur.execute(judge_table_sql)
        print cur.fetchone()
        if cur.fetchone() is None:
            cur.execute(create_table_sql)
            cur.execute(create_index_sql)
        conn.commit()
    except Exception as e:
        get_error_logger().error(e)
    finally:
        cur.close()
        conn.close()


def insert_table(insert_sql):
    """
    向表中插入数据
    :param insert_sql:
    :return:
    """
    conn = connect_db()
    cur = conn.cursor()
    try:
        cur.execute(insert_sql)
        conn.commit()
    except Exception as e:
        get_error_logger().error(e)
    finally:
        cur.close()
        conn.close()
