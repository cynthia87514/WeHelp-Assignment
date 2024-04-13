def func(*data):
    middle_names = {}
    for i in data:
        if len(i) == 2 or len(i) == 3:
            middle_name = i[1]
            middle_names[middle_name] = middle_names.get(middle_name, 0) + 1 # 將中間名添加到字典中。若中間名已在字典中存在，則將其出現次數加 1；若中間名尚未在字典中存在，則將其出現次數設置為 1。
        elif len(i) == 4 or len(i) == 5:
            middle_name = i[2]
            middle_names[middle_name] = middle_names.get(middle_name, 0) + 1
        else:
            continue
    n = 0
    for i in middle_names:
        if middle_names[i] == 1:
            n += 1
            for j in data:
                if len(j) == 2 or len(j) == 3:
                    if j[1] == i:
                        print(j)
                        break
                if len(j) == 4 or len(j) == 5:
                    if j[2] == i:
                        print(j)
                        break
    if n == 0:
        print("沒有")

func("彭大牆", "陳王明雅", "吳明") # print 彭大牆
func("郭靜雅", "王立強", "郭林靜宜", "郭立恆", "林花花") # print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花") # print 沒有
func("郭宣雅", "夏曼藍波安", "郭宣恆") # print 夏曼藍波安
