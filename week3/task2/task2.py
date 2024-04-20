# 抓取 PTT lottery 版的網頁原始碼 (HTML)
import urllib.request as req
import bs4
import csv

def get_data(url):
    dict_list = []  # 創建一個空列表來存放每篇文章的字典

    # 建立一個 Request 物件，附加 Request Headers 的資訊 > 讓自己看起來比較像一般使用者
    request = req.Request(url, headers={
        "Cookie": "over18=1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")

    # 解析原始碼
    root = bs4.BeautifulSoup(data, "html.parser")  # 讓 BeautifulSoup 協助我們解析 HTML 格式文件

    # 取得每篇文章的標題、讚/噓數和發布時間
    titles = root.find_all("div", class_="title")  # 尋找所有 class = "title" 的 div 標籤
    counts = root.find_all("div", class_="nrec")  # 尋找所有 class = "nrec" 的 div 標籤

    for title, count in zip(titles, counts): # zip 可以將多個迭代器相對應位置打包成元組，並返回一個迭代器
        dict = {}  # 創建一個新的字典，用於存放當前文章的資訊

        # 取得文章標題
        if title.a: # 如果標題包含 a 標籤 (沒有被刪除)，則印出結果
            dict["ArticleTitle"] = title.a.string
        else:
            dict["ArticleTitle"] = ""

        # 取得讚/噓數
        if count.span: # 如果標題包含 span 標籤 (沒有被刪除)，則印出結果
            dict["Like/DislikeCount"] = count.span.string
        else:
            dict["Like/DislikeCount"] = ""

        # 取得發布時間
        if title.a: # 如果標題包含 a 標籤 (沒有被刪除)，則印出結果
            content_url = "https://www.ptt.cc" + title.a["href"] # 要先點進文章標題 (內文)，才能取得發布時間
            # 同樣建立一個 Request 物件，附加 Request Headers 的資訊 > 讓自己看起來比較像一般使用者
            request_time = req.Request(content_url, headers={
                "Cookie": "over18=1",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
            })
            # 打開網頁並解析其原始碼
            with req.urlopen(request_time) as response_time:
                content = response_time.read().decode("utf-8")
            article = bs4.BeautifulSoup(content, "html.parser")
            # 尋找所有 class = "article-meta-value" 的 span 標籤
            times = article.find_all("span", class_="article-meta-value")
            # 「發布時間」為排序第四位的 class = "article-meta-value" 的 span 標籤
            if len(times) >= 4:
                dict["PublishTime"] = times[3].text
            else:
                dict["PublishTime"] = ""
        else:
            dict["PublishTime"] = ""

        dict_list.append(dict)  # 將當前文章的字典加入到列表中

    # 抓取上一頁的連結
    last_link = root.find("a", string="‹ 上頁")  # 找到內文是 ‹ 上頁 的 a 標籤
    if last_link:
        return "https://www.ptt.cc" + last_link["href"], dict_list  # 抓取其 "href" 屬性，並回傳連結和列表
    else:
        return None, dict_list  # 若找不到上一頁的連結，則回傳 None 和列表


# 主程序：抓取多個頁面的標題
pageURL = "https://www.ptt.cc/bbs/Lottery/index.html"  # 第一頁的網址 (是固定的)
all_articles = [] # 創建一個空列表來存放所有頁面的文章資訊

for a in range(3): # 總共抓取 3 頁的標題
    pageURL, articles = get_data(pageURL)
    all_articles.extend(articles)  # 將當前頁面的文章資訊加入到列表中，extend 是取出 object 的所有 element/iterator 扔進 list 裡，append 則直接把 object 塞進 list 裡面

#print(all_articles)

with open("article.csv", "w", newline="") as csvfile: # 加入參數 newline = ""，避免輸出時每行間多空一行
    fieldnames = ["ArticleTitle", "Like/DislikeCount", "PublishTime"] # 定義欄位(標題)
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames) # 將 dictionary 寫入 CSV 檔 / 建立 writer 物件
    writer.writeheader() # 寫入第一列的欄位名稱(標題)
    for row in all_articles: # 須為一個列表資料
        writer.writerow(row)
