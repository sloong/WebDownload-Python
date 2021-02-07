'''
Author: Chuanbin Wang - wcb@sloong.com
Date: 1970-01-01 08:00:00
LastEditTime: 2021-02-07 10:43:34
LastEditors: Chuanbin Wang
FilePath: /crawler/src/crawl.py
Copyright 2015-2020 Sloong.com. All Rights Reserved
Description: Find target elements in all page.
User must set the rule for searching.
'''
import requests
import re
import queue
from lxml import html, etree
from threading import Timer
import os.path
from os import path
import pickle


class Crawler:
    def __init__(self):
        self.download_urls = queue.Queue()
        self.work_urls = queue.Queue()
        self.all_urls = []
        self.cached_urls = []
        self.running = True
    # 工作流程

    def Start(self, start_url):
        if not self.restore():
            self.work_urls.put(start_url)

        Timer(10, self.save).start()

        # 开始循环处理链接列表
        # 每个页面都先获取页面内容然后匹配所以的超链接信息，并检查是不是保存过
        # 如果没保存添加到列表中。
        # 同时获取页面所有文本信息，然后进行目标匹配，获取地址信息
        while not self.work_urls.empty():
            url = self.work_urls.get()
            # 处理相对页面，如果不是以http开头则认为是相对页面
            if not url.startswith("http"):
                url = self.baseurl + url
            print('开始处理新页面:<<<' + url)
            # 处理外站链接，不是以baseurl开头的认为外站链接
            if not url.startswith(self.baseurl):
                print('非当前站点,跳过')
                continue
            page = self.get_page_text(url)
            urls = self.get_page_urls(page)
            skip = self.get_skip_url(page)
            for u in urls:
                self.process_page(page)

            all_download = self.get_pan_urls(page)
            for u in all_download:
                title = self.get_title(page)
                self.download_urls.put(u)
                print('找到网盘地址信息>>' + title + u[0] + u[1])

            print('<<<页面处理完成')

        print('处理完成')
        self.runing = False

    def process_page(self, content):
        if u in skip:
            continue

        block = False
        for b in self.block_List:
            if u.find(b) != -1:
                block = True
                break
        if block:
            continue

        force = False
        for b in self.force_List:
            if u.find(b) != -1:
                force = True
                break

        if u not in self.all_urls and u not in self.cached_urls:
            print('找到新的页面:' + u)
            self.work_urls.put(u)
            if force:
                self.cached_urls.append(u)
            else:
                self.all_urls.append(u)

    def save(self):
        all_urls_file = open('out\\all_urls.bin', 'wb')
        s = pickle.dumps(self.all_urls)
        all_urls_file.write(s)
        all_urls_file.close()

        work_urls_file = open('out\\work_urls.bin', 'wb')
        work_urls_file.write(pickle.dumps(
            [item for item in qdumper(self.work_urls)]))
        work_urls_file.close()

        download_urls_file = open('out\\result.txt', 'a')
        while not self.download_urls.empty():
            u = self.download_urls.get()
            download_urls_file.write('{},验证码:{}\r\n'.format(u[0], u[1]))

        download_urls_file.close()

        if self.running:
            Timer(10, self.save).start()

    def restore(self):
        if path.exists('out\\all_urls.bin') and path.exists('out\\work_urls.bin'):
            f = open('out\\all_urls.bin', 'rb')
            self.all_urls = pickle.loads(f.read())
            f.close()

            f = open('out\\work_urls.bin', 'rb')
            for i in pickle.loads(f.read()):
                self.work_urls.put(i)
            f.close()
            return True
        else:
            return False

    # 获取页面文本
    def get_page_text(self, url):
        return requests.Session().get(url).text

    # 获取页面里所有超链接
    def get_page_urls(self, page):
        return re.findall(self.rules[RuleEnum.SuperLink], page)

    # 根据规则，获取页面里的主要内容区的内容
    def get_page_content(self, page):
        return re.findall(self.rules[RuleEnum.Content], page)

    # 根据规则，获取页面中网盘下载信息
    def get_pan_urls(self, page):
        return re.findall(self.rules[RuleEnum.PanDownload], page)

    # 根据规则，获取页面标题
    def get_title(self, page):
        try:
            tree = html.fromstring(page)
            return tree.xpath(self.rules[RuleEnum.Title])[0]
        except:
            tree = html.fromstring(bytes(bytearray(page, self.encoding)))
            return tree.xpath(self.rules[RuleEnum.Title])[0]

    # 根据规则，获取页面里需要跳过的超链接
    def get_skip_url(self, page):
        tree = html.fromstring(bytes(bytearray(page, self.encoding)))
        return tree.xpath(self.rules[RuleEnum.SkipURL])


def qdumper(q):
    try:
        yield q.get(False)
    except queue.Empty:
        pass
