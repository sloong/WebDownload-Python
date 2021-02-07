import utility
import threading

def download_page(sub_url,save_folder):
    title = get_page_title(sub_url)
    print("ready to download "+ title)
    save_folder = create_save_folder(title,save_folder)
    return threading.Thread(target=download_page_img,args=(sub_url,save_folder))




if __name__ == "__main__":
    base_url = "http://tu-101.xyz"
    index_url = "http://tu-101.xyz/a/ar/index.html"
    next_page_regular = r'<a href="(.+?)">.?下一页.?</a>'
    sub_page_regular = r'<span class="stitle"> <a href="(.+?)"'
    save_folder = "D:\\pic\\"
    url = index_url
    while url != "":
        print("current url:"+url)
        page_data = utility.get_page_data(url)
        
        sub_page = utility.get_sub_page_from_index(page_data,base_url,sub_page_regular)
        t_list = []
        for page in sub_page:
            if '#' not in page:
                t = download_page(url,save_folder)
                t.start()
                t_list.append(t);

        for t in t_list:
            t.join()

        url = utility.get_next_index_page(page_data,base_url,next_page_regular)    
        

    
