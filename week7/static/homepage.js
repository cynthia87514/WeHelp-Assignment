// 檢查註冊表單是否有任何空的輸入
document.querySelector(".form1").addEventListener("submit", function(event){
    var inputs = document.querySelectorAll(".form1 input");
    for (let i = 0; i < inputs.length; i++){
        if (inputs[i].value.trim() === ""){
            event.preventDefault(); // 防止表單提交
            alert("請輸入姓名、帳號或密碼");
            return;
        }
    }
});

// 檢查登入表單是否有任何空的輸入
document.querySelector(".form2").addEventListener("submit", function(event){
    var inputs = document.querySelectorAll(".form2 input");
    for (let i = 0; i < inputs.length; i++){
        if (inputs[i].value.trim() === ""){
            event.preventDefault(); // 防止表單提交
            alert("請輸入帳號或密碼");
            return;
        }
    }
});
