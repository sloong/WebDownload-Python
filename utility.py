import urllib.request 
import re
import os, sys


def get_page_data(url,encode="utf-8"):
    """获取页面数据
    Args：
        url：页面地址
        encode：编码
    Returns：
        页面数据，
    """
    response = urllib.request.urlopen(url)
    url_data = response.read().decode(encode)
    return url_data


# 下载文件
def download_img(url,save_folder):
    filename = url.split('/')[-1]
    save_filename = save_folder + '\\' + filename
    if os.path.isfile(save_filename):
        # 检查文件大小，如果是0那么认为是有问题的文件
        if os.path.getsize(save_filename) < 10 :
            print("文件无效，删除："+save_filename)
            os.remove(save_filename)
        else:
            return
    try:
        urllib.request.urlretrieve(url, save_filename  , None)
        print("download succeed:" + save_filename )
    except Exception as e:
        print('Error:', e)
    

# 获取页面所有图片链接
# restr为解析图片的正则表达式
# 返回图片链接列表
def get_all_img_url(page_data,restr=r'<img.*src="(.+?)"'):
    img_res = re.findall(restr,page_data)
    img_tmp = []
    [img_tmp.append(i) for i in img_res if i not in img_tmp]
    return img_tmp


def get_page_title(page_data,regular=r'<title>(.*)</title>'):
    result = re.findall(regular,page_data)
    if result and result[0]:
        return result[0]
    else:
        return "Untitled"

def download_page_img(page_url,save_folder):
    tab_text = get_page_data(page_url)
    img_tmp = get_all_img_url(tab_text)
    for img in img_tmp :
            if not re.match(r'^/',img):
                download_img(img,save_folder)


def create_save_folder(page_title,folder):
    save_folder = folder + page_title
    if not os.path.exists(save_folder):
        # os.system("mkdir " + save_folder)
        os.mkdir(save_folder)
    return save_folder

def get_sub_page_from_index(page_data,base_url,regular):
    """获取索引页面中的所有子页面
    Args:
        page_data: 页面数据。可以使用get_page_data获取
        regular:正则表达式字符串。
    Returns:
        匹配的结果集
    """
    reg = 
    result = re.findall(reg, page_data)
    temp = []
    for item in result:
        item = base_url + item
        temp.append(item)

    return temp




def get_next_index_page(cur_page_data,regular):
    """
    获取翻页的地址
    """
    result = re.findall(regular, cur_page_data)
    if result and '#' not in result:
        return cur_page_data + result[0]
    else:
        return ""
