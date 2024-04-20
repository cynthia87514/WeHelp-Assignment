// 按下 hamburger 和 cross 時產生的回應
document.addEventListener('DOMContentLoaded',function(){
    var picture = document.getElementById('picture');
    var list = document.getElementById('list');
    var cross = document.getElementById('cross');
    
    picture.addEventListener('click',function(){
        list.classList.add('show');
    });

    cross.addEventListener('click', function(){
        list.classList.remove('show');
    });
});

// 利用 fetch 進行連線並取得資料
document.addEventListener("DOMContentLoaded", function() {
    fetch('https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1')
    .then(response => {
        if (!response.ok) {
            throw new Error("網路回應不正確");
        }
        return response.json();
    })
    .then(data => {
        // 在此處理從 URL 取得的資料
        console.log(data); // data 的類別為 object
        const resultsContent = data.data.results;

        for (let n = 0 ; n < 13 ; n++){
            var picturesURLs = resultsContent[n].filelist;
            var picturesurls = picturesURLs.toLowerCase(); // 將字串換成小寫
            var picturesIndex = picturesurls.indexOf(".jpg"); // 找到第一個 ".jpg" 出現的位置
            var pictures = picturesURLs.substring(0, picturesIndex + 4); // 使用 substring 方法從字串開頭到第一個 ".jpg" 的位置來取得想要的資料，加上 4 是因為 ".jpg" 有 4 個字元

            var spots = resultsContent[n].stitle;

            if (n<3){
                var elementId = "small" + (n+1);

                var img = document.createElement("img");
                img.src = pictures;
                img.setAttribute("width", "80px");
                img.setAttribute("height", "50px");
                var element = document.getElementById(elementId);
                element.appendChild(img);

                var spot = document.createElement("div");
                var node = document.createTextNode(spots);
                spot.appendChild(node); 
                spot.setAttribute("class", "promotion");
                var element = document.getElementById(elementId);
                element.appendChild(spot);
            }
            else{
                var elementIdBig = "big" + (n-2);
                var element = document.getElementById(elementIdBig);
                element.style.backgroundImage = "url(" + pictures + ")";

                var elementIdTitleBox = "titleBox" + (n-2);
                var spot = document.createElement("div");
                if(spots.length>7){
                    spots = spots.substring(0,7)+"...";
                }
                
                var node = document.createTextNode(spots);
                spot.appendChild(node);
                spot.setAttribute("class", "title");
                var element = document.getElementById(elementIdTitleBox);
                element.appendChild(spot);
            }
        }
    })
    .catch(error => {
        console.error("取得資料時出現問題:", error);
    });
});
