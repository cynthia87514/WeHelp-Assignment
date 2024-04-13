function func(...data){
    let middleNames = {};
    for (let i of data){
        let middleName = "";
        if (i.length === 2 || i.length === 3){
            middleName = i[1];
        }
        else if (i.length === 4 || i.length === 5){
            middleName = i[2];
        }
        else{
            continue;
        }
        middleNames[middleName] = (middleNames[middleName] || 0) + 1;
        //console.log(middleNames)
    }
    let n = 0;
    for (let middleName in middleNames){
        if (middleNames[middleName] === 1){
            n++;
            for (let j of data){
                if ((j.length === 2 || j.length === 3) && j[1] === middleName){
                    console.log(j);
                    break;
                }
                if ((j.length === 4 || j.length === 5) && j[2] === middleName){
                    console.log(j);
                    break;
                }
            }
        }
    }
    if (n === 0){
        console.log("沒有");
    }
}

func("彭大牆", "陳王明雅", "吳明"); // print 彭大牆
func("郭靜雅", "王立強", "郭林靜宜", "郭立恆", "林花花"); // print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花"); // print 沒有
func("郭宣雅", "夏曼藍波安", "郭宣恆"); // print 夏曼藍波安