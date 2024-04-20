from urllib.request import urlopen
import json
import re
import csv

# 爬取網頁連結中的資料----------------------------------------------------------------------------------------------------

with urlopen('https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1') as response1:
    spot_content = response1.read().decode('utf-8')
    parsed_data1 = json.loads(spot_content)
    results = parsed_data1["data"]["results"]

with urlopen('https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-2') as response2:
    mrt_address = response2.read().decode('utf-8')
    parsed_data2 = json.loads(mrt_address)
    data = parsed_data2["data"]

# 將連結中資料我需要的部分擷取出來-----------------------------------------------------------------------------------------

mrt_list_unmerged = []
for m in results:
    for n in data:
        mrt_dict = {}
        if m["SERIAL_NO"] == n["SERIAL_NO"]: # 從 檔案2 中取出對應的 "SERIAL_NO"，以得到景點所對應的捷運站名
            mrt_dict["StationName"] = n["MRT"]
            mrt_dict["SpotTitles"] = m["stitle"]
            mrt_list_unmerged.append(mrt_dict)

mrt_dict_merged = {} # 創建一個空字典，用於儲存合併後的資料
for d in mrt_list_unmerged: # 遍歷 / 迭代 mrt_list_unmerged 列表中的每一個字典
    key = d["StationName"] # 抓取該捷運站名稱
    value = d["SpotTitles"] # 抓取該景點名稱
    if key in mrt_dict_merged: # 檢查該捷運站名稱是否已在 mrt_dict_merged 列表中
        mrt_dict_merged[key]["SpotTitles"].append(value) # 若已存在，將該景點名稱加到對應捷運站名的字典中的 "SpotTitles" 鍵對應的列表中
    else: # 若該捷運站名稱不在 mrt_dict_merged 中，則執行以下程式碼
        mrt_dict_merged[key] = {"StationName": key, "SpotTitles": [value]} # 創建一個新的鍵值對，以 "StationName" 和 "SpotTitles" 作為鍵，分別對應該捷運站名和一個包含該景點名稱的列表
mrt_list = list(mrt_dict_merged.values())
for item in mrt_list:
    item["SpotTitles"] = ",".join(item["SpotTitles"])

keys = [entry["StationName"] for entry in mrt_list]
values = [entry['SpotTitles'].split(',') for entry in mrt_list] # 將 "SpotTitles" 對應的 value 一一分開

# 將 Python 資料輸出成 csv 檔案-----------------------------------------------------------------------------------------

with open("mrt.csv", "w", newline="") as csvfile: # 加入參數 newline = ""，避免輸出時每行間多空一行
    writer = csv.writer(csvfile)
    for k, v in zip(keys, values):
        writer.writerow([k] + v)