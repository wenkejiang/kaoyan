# -*- coding: utf-8 -*-
"""
@Time ： 2022/4/17 12:07 下午
@Auth ： 姜文科
@File ：util.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
import os

import yaml

basePath = os.path.dirname(os.path.abspath(__file__))


def read_school_yaml(file, name=None):
    # 读取学校yaml
    yamlPath = basePath + "/{}.yaml".format(file)
    f = open(yamlPath, 'r', encoding='utf-8')
    data = yaml.load(f, Loader=yaml.FullLoader)
    if name:
        return data[name]
    else:
        return data


def wirte_result_yaml(name, value):
    # 写入yaml文件
    yamlPath = basePath + "/result.yaml"
    stream = open(yamlPath, 'r', encoding='utf-8')
    data = yaml.load(stream, Loader=yaml.FullLoader)
    data[name] = value
    with open(yamlPath, 'w') as yaml_file:
        yaml_file.write(yaml.dump(data, default_flow_style=False))


if __name__ == '__main__':
    wirte_result_yaml("QDDX", "1234517")
    read_school_yaml("school")
