'''
Author: Chuanbin Wang - wcb@sloong.com
Date: 1970-01-01 08:00:00
LastEditTime: 2021-01-25 15:30:55
LastEditors: Chuanbin Wang
FilePath: /crawler/src/main.py
Copyright 2015-2020 Sloong.com. All Rights Reserved
Description: 
'''

print('__file__={0:<35} | __name__={1:<20} | __package__={2:<20}'.format(__file__,__name__,str(__package__)))

import rules.situge as rule
import crawl

worker = crawl.Crawler(rule.baseurl, rule.block_list, rule.force_urls, rule.encoding)
worker.RegisteRule(crawl.RuleEnum.Title, rule.title_rule )
worker.RegisteRule(crawl.RuleEnum.SkipURL,rule.skip_url_rule )
worker.RegisteRule(crawl.RuleEnum.SuperLink,rule.super_link_rule )
worker.RegisteRule(crawl.RuleEnum.PanDownload,rule.target_rule )
worker.Start(rule.baseurl)