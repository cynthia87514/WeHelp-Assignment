document.addEventListener("DOMContentLoaded", function(){
    var signoutLink = document.getElementById("signout");
    signoutLink.addEventListener("click", function(){
        window.location.href = "/signout";
    })
})

// 檢查留言表單是否有任何空的輸入
document.querySelector(".messageForm").addEventListener("submit", function(event){
    var input = document.querySelector(".messageForm input");
    if (input.value.trim() === ""){
        event.preventDefault(); // 防止表單提交
        alert("請輸入留言");
        return;
    }
});