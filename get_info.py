# -*- coding: utf-8 -*-
"""
@Time ： 2022/4/17 11:41 上午
@Auth ： 姜文科
@File ：get_info.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
import random
import re
import time

from itchat_util import do_dingding
from myrequest import BasicSpider
from util import read_school_yaml, wirte_result_yaml


def getheaders():
    user_agent_list = [
        'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1464.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.16 Safari/537.36',
        'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.3319.102 Safari/537.36',
        'Mozilla/5.0 (X11; CrOS i686 3912.101.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36',
        'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:17.0) Gecko/20100101 Firefox/17.0.6',
        'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1468.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36',
        'Mozilla/5.0 (X11; CrOS i686 3912.101.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36']
    UserAgent = random.choice(user_agent_list)
    return UserAgent


def get_info():
    end = []
    school_info = read_school_yaml("school")
    for info in school_info:
        time.sleep(2)
        hearders = {
            "User-Agent": getheaders()
        }
        response = BasicSpider().downloader(url=info, method="GET", header=hearders)
        pattern = r"调剂"
        matchObj = re.findall(pattern, response)
        print("{matchObj}".format(matchObj=matchObj))
        length = len(matchObj)
        result = read_school_yaml("result", info)
        if length != result:
            end.append(info)
            wirte_result_yaml(info, length)
            print("查询中。。。。。请等待")
    print(end)
    if len(end) == 0:
        do_dingding("没有更新！！！")
    else:
        do_dingding(end)


if __name__ == '__main__':
    get_info()
