function findAndPrint(messages, currentStation){
    let result = "";
    let dist = -1;
    const stationValues = { //以 const 宣告，為定量
        "Songshan": 0, "Nanjing Sanmin": 1, "Taipei Arena": 2, "Nanjing Fuxing": 3,
        "Songjiang Nanjing": 4, "Zhongshan": 5, "Beimen": 6, "Ximen": 7, "Xiaonanmen": 8,
        "Chiang Kai-Shek Memorial Hall": 9, "Guting": 10, "Taipower Building": 11,
        "Gongguan": 12, "Wanlong": 13, "Jingmei": 14, "Dapinglin": 15, "Qizhang": 16,
        "Xiaobitan": 16.5, "Xindian City Hall": 17, "Xindian": 18
    };

    for (let friend in messages){
        let valueFriend = -1;
        let message = messages[friend];
        for (let station in stationValues){
            if (message.includes(station)){
                valueFriend = stationValues[station];
                break;
            }
        }
        let valueMe = stationValues[currentStation];

        if (dist === -1 || dist > Math.abs(valueMe - valueFriend) + (valueMe - valueFriend === 0.5 ? 1 : 0)){
            result = friend;
            dist = Math.abs(valueMe - valueFriend) + (valueMe - valueFriend === 0.5 ? 1 : 0); //條件運算子
        }
    }
    console.log(result);
}

const messages={
    "Bob":"I'm at Ximen MRT station.",
    "Mary":"I have a drink near Jingmei MRT station.",
    "Copper":"I just saw a concert at Taipei Arena.",
    "Leslie":"I'm at home near Xiaobitan station.",
    "Vivian":"I'm at Xindian station waiting for you."
};

findAndPrint(messages, "Wanlong"); // print Mary
findAndPrint(messages, "Songshan"); // print Copper
findAndPrint(messages, "Qizhang"); // print Leslie
findAndPrint(messages, "Ximen"); // print Bob
findAndPrint(messages, "Xindian City Hall"); // print Vivian