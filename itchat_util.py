# -*- coding: utf-8 -*-
"""
@Time ： 2022/4/17 2:46 下午
@Auth ： 姜文科
@File ：itchat_util.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
import requests


def do_dingding(body):
    url = "https://oapi.dingtalk.com/robot/send"

    token = {"access_token": "8badf6d616272475e606cf01b6219d8898950e5aa72a4cdbb8e5f64f46d14bcb"}  # 定义成字典去改他

    data = {
        "at": {
            # "atMobiles": [],
            "isAtAll": True
        },
        "text": {
            "content": "调剂更新学校名单:{}".format(body)
        },
        "msgtype": "text"
    }

    r = requests.post(url, params=token, json=data)  # 请求参数穿到URL里面用 params，json类型接口

    print(r.json())
