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

// 確定是否要刪除留言
document.addEventListener("DOMContentLoaded", function(){
    var deleteForms = document.querySelectorAll(".deleteForm");
    deleteForms.forEach(function(form){
        form.addEventListener("submit", function(event){
            if (!confirm("確定要刪除嗎？")){
                event.preventDefault();
            }
        });
    });
});