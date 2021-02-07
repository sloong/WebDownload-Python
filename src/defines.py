'''
Author: Chuanbin Wang - wcb@sloong.com
Date: 1970-01-01 08:00:00
LastEditTime: 2021-02-07 10:29:59
LastEditors: Chuanbin Wang
FilePath: /crawler/src/defines.py
Copyright 2015-2020 Sloong.com. All Rights Reserved
Description: 
'''
from enum import Enum
class RuleEnum(Enum):
    SuperLink = 1
    PanDownload = 2
    Title = 3
    SkipURL = 4
    Content = 5
