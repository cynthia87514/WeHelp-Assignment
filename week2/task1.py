def find_and_print(messages, current_station):
    result = ""
    dist = -1
    station_values = {
            "Songshan":0, "Nanjing Sanmin":1, "Taipei Arena":2, "Nanjing Fuxing":3,
            "Songjiang Nanjing":4, "Zhongshan":5, "Beimen":6, "Ximen":7, "Xiaonanmen":8,
            "Chiang Kai-Shek Memorial Hall":9, "Guting":10, "Taipower Building":11,
            "Gongguan":12, "Wanlong":13, "Jingmei":14, "Dapinglin":15, "Qizhang":16,
            "Xiaobitan":16.5, "Xindian City Hall":17, "Xindian":18
    }
    for i in messages:
        for j in station_values:
            if(messages[i].find(j) != -1):
                value_friend = station_values[j]
                break
        value_me = station_values[current_station]
        
        if dist == -1:
            result = i
            if (value_me - value_friend) == 0.5:
                dist = abs(value_me - value_friend) + 1
            else:
                dist = abs(value_me - value_friend)
        elif dist > abs(value_me - value_friend) and value_me - value_friend == 0.5:
            result = i
            dist = abs(value_me - value_friend) + 1
        elif dist > abs(value_me - value_friend):
            result = i
            dist = abs(value_me - value_friend)
    print(result)
            
messages={
    "Leslie":"I'm at home near Xiaobitan station.",
    "Bob":"I'm at Ximen MRT station.",
    "Mary":"I have a drink near Jingmei MRT station.",
    "Copper":"I just saw a concert at Taipei Arena.",
    "Vivian":"I'm at Xindian station waiting for you."
}

find_and_print(messages, "Wanlong") # print Mary
find_and_print(messages, "Songshan") # print Copper
find_and_print(messages, "Qizhang") # print Leslie
find_and_print(messages, "Ximen") # print Bob
find_and_print(messages, "Xindian City Hall") # print Vivian