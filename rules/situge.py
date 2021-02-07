'''
Author: Chuanbin Wang - wcb@sloong.com
Date: 1970-01-01 08:00:00
LastEditTime: 2021-01-25 15:49:25
LastEditors: Chuanbin Wang
FilePath: /crawler/src/rules/situge.py
Copyright 2015-2020 Sloong.com. All Rights Reserved
Description: 
'''

baseurl = 'http://www.situge.ooo/archiver/'  # 需要爬数据的网址
domain = 'http://www.situge.ooo'

connect='Test/Test/Teste'
title_rule = '//div[@id="content"]//h3/text()'
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
    'forum.php',
    'home.php',
    'fid-43.html',
    'fid-44.html',
    'fid-45.html',
    'fid-87.html',
    'fid-89.html',
    'fid-88.html',
    'fid-55.html',
    'fid-68.html',
    'fid-69.html',
    'fid-70.html',
    'fid-71.html',
    'fid-72.html',
    'fid-73.html',
    'fid-74.html',
    'fid-75.html',
    'fid-76.html',
    'fid-77.html',
    'fid-78.html',
    'fid-79.html',
    'fid-80.html',
    'fid-56.html',
    'fid-81.html',
    'fid-82.html',
    'fid-84.html',
    'fid-171.html',
    'fid-173.html',
    'fid-187.html',
    'fid-190.html',
    'fid-2.html',
    'fid-37.html',
    'fid-112.html',
    'fid-54.html',
    'fid-65.html',
    'fid-53.html',
    'fid-85.html',
    'fid-52.html',
    'fid-50.html',
    'fid-100.html',
    'fid-133.html',
    'fid-174.html',
    'fid-184.html',
    'fid-191.html',
    'fid-194.html',
    'fid-206.html',
    'fid-213.html',
    'fid-212.html',
    'fid-214.html',
    'fid-216.html',
    'fid-117.html',
    'fid-118.html',
    'fid-119.html',
    'fid-120.html',
    'fid-121.html',
    'fid-224.html',
    'fid-95.html',
    'fid-113.html',
    'fid-124.html',
    'fid-126.html',
    'fid-127.html',
    'fid-128.html',
    'fid-129.html',
    'fid-131.html',
    'fid-132.html',
    'fid-90.html',
    'fid-210.html',
    'fid-222.html',
    'fid-225.html',
    'fid-226.html',
    'fid-223.html',
    'fid-38.html',
    'fid-39.html',
    'fid-40.html',
    'fid-51.html',
    'fid-94.html',
    'fid-105.html',
    'fid-46.html'
    'http://www.discuz.net',
    'http://www.comsenz.com',
    'thread-',
]
