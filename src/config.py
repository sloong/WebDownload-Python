'''
Author: Chuanbin Wang - wcb@sloong.com
Date: 1970-01-01 08:00:00
LastEditTime: 2021-02-07 10:43:55
LastEditors: Chuanbin Wang
FilePath: /crawler/src/config.py
Copyright 2015-2020 Sloong.com. All Rights Reserved
Description: 配置管理。
主要功能，跳过列表，强制列表，页面编码，规则列表，模式等
'''


class Configuation:
     def __init__(self, baseurl):
        # 跳过列表，在检测超链接的时候，尝试匹配，匹配成功直接忽略掉。
        self.block_List = []
        # 强制刷新列表，即每次都强制重新读取
        self.force_List = []
        self.encoding = 'utf8'
        self.baseurl = baseurl
        self.rules = []


    def set_block_list(block_list):
        self.block_List = block_list

    def set_force_list(force_list):
        self.force_List = force_list

    def set_encoding(encoding):
        self.encoding = encoding
    
    def RegisteRule(self, t: RuleEnum, rule: str):
        self.rules[t] = rule
