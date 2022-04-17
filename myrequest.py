# -*- coding: utf-8 -*-
"""
@Time ： 2022/4/17 3:55 下午
@Auth ： 姜文科
@File ：myrequest.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/16 14:34
# @Author  : JiangWenKe
# @Site    :
# @File    : request.py
# @Software: PyCharm
import cchardet
import urllib3
from retrying import retry

from requests import request, RequestException


class BasicSpider(object):

    @retry(stop_max_attempt_number=2, retry_on_result=lambda x: x is None, wait_fixed=2000)
    def downloader(self, url, method=None, header=None, timeout=None, binary=False, **kwargs):
        print(f'请求的URL: {url}')
        # 默认超时
        _maxTimeout = timeout if timeout else 5
        # 自定义Ua
        # 默认请求方法
        _method = "GET" if not method else method
        try:
            urllib3.disable_warnings()
            response = request(method=_method, url=url, headers=header, timeout=_maxTimeout, verify=False, **kwargs)
            encoding = cchardet.detect(response.content)['encoding']
            if response.status_code == 200:
                return response.content if binary else response.content.decode(encoding)
            elif 200 < response.status_code < 400:
                print(f"请求URL: {response.url}")
            print('抓取 %s 时获取无效状态代码 %s', url, response.status_code)
        except RequestException as e:
            print(f'抓取时发生错误 {url}, Msg: {e}')


if __name__ == '__main__':
    basic = BasicSpider()
    print(basic.downloader("https://www.baidu.com/"))
