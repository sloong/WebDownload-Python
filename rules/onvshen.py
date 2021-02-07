'''
Author: Chuanbin Wang - wcb@sloong.com
Date: 1970-01-01 08:00:00
LastEditTime: 2021-01-28 20:28:46
LastEditors: Chuanbin Wang
FilePath: /crawler/src/rules/onvshen.py
Copyright 2015-2020 Sloong.com. All Rights Reserved
Description: 
'''

baseurl = 'http://www.situge.ooo/archiver/'  # 需要爬数据的网址
domain = 'http://www.situge.ooo'

connect='//div[@id="photo_list"]'
title_rule = '//"div[@id="albumTitle"]//h1/text()'
encode = 'gb2312'
skip_url_rule = '//div[@id="end"]//a/@href'
super_link_rule= r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')",
target_rule= r"(https://pan.baidu.com/.+)提取码:.?(\w{4})",

# 强制访问的地址列表,在保存已访问过的地址时,会首先检查该参数,如果符合则不保存到文件中,而是保存在一个临时变量中.退出后不保存.
force_urls = [
    'fid-211.html'
]

# 限制列表,在进行循环时将会跳过此列表
block_list = [
    
]
