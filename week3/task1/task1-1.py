from urllib.request import urlopen
import json
import re
import csv

# 爬取網頁連結中的資料----------------------------------------------------------------------------------------------------

with urlopen('https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1') as response1:# 打開網頁連結
    # 讀取網頁內容
    spot_content = response1.read().decode('utf-8') # 將內容解碼成 UTF-8 格式
    parsed_data1 = json.loads(spot_content) # 解析 JSON 字符串
    results = parsed_data1["data"]["results"] # results 的型別為 list
    print(type(results))

with urlopen('https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-2') as response2:# 打開網頁連結
    # 讀取網頁內容
    mrt_address = response2.read().decode('utf-8') # 將內容解碼成 UTF-8 格式
    parsed_data2 = json.loads(mrt_address) # 解析 JSON 字符串
    data = parsed_data2["data"] # data 的型別為 list

# 將連結中資料我需要的部分擷取出來-----------------------------------------------------------------------------------------

spot_list = []
for i in results: # i 代表 results 中的每一個字典
    spot_dict = {}
    if "stitle" in i:
        spot_dict["SpotTitle"] = i["stitle"]
    if "SERIAL_NO" in i:
        target_value = i["SERIAL_NO"]
        for j in data:
            if j["SERIAL_NO"] == target_value:
                address = j["address"] # 從 檔案2 中取出 "SERIAL_NO" 相對應的完整地址
                match1 = re.search(r'\S+?(?=區)', address) # 取得空白後、"區"之前的字串
                # District = match1.group() + "區" # 將 match1 的結果返回
                spot_dict["District"] = match1.group() + "區" # 將 match1 的結果返回
    if "longitude" in i:
        spot_dict["Longitude"] = i["longitude"]
    if "latitude" in i:
        spot_dict["Latitude"] = i["latitude"]
    if "filelist" in i:
        ImageURLs = i["filelist"] # 取得所有照片的網址
        match2 = re.search(r'.*?(?=\.jpg)', ImageURLs, re.IGNORECASE) # 取得 ".jpg"(不分大小寫)之前的字串
        spot_dict["ImageURL"] = match2.group() + ".jpg" # 將 match2 的結果返回
    spot_list.append(spot_dict)

# 將 Python 資料輸出成 csv 檔案-----------------------------------------------------------------------------------------

with open("spot.csv", "w", newline="") as csvfile: # 加入參數 newline = ""，避免輸出時每行間多空一行
    fieldnames = ["SpotTitle", "District", "Longitude", "Latitude", "ImageURL"] # 定義欄位(標題)
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames) # 將 dictionary 寫入 CSV 檔 / 建立 writer 物件
    writer.writeheader() # 寫入第一列的欄位名稱(標題)
    for row in spot_list: # 須為一個列表資料
        writer.writerow(row)