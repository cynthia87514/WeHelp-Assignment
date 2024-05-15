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

// 若查詢會員為空的輸入，發送提醒；若非空的輸入，使用 fetch 函式向後端發送 GET 請求
document.getElementById("queryMemberButton").addEventListener("click", async function(){
    const username = document.getElementById("queryMember").value;
    if (username === ""){
        alert("請輸入欲查詢的帳號名稱");
        return;
    }else{
        try{
            const response = await fetch(`/api/member?username=${username}`);
            const data = await response.json();
            const result = document.getElementById("queryResultSuccess");

            if (data.data !== null){
                result.textContent = `${data.data.name} (${data.data.username})`;
                const previewData = {
                    "data": {
                        "id": data.data.id,
                        "name": data.data.name,
                        "username": data.data.username
                    }
                };
                console.log(JSON.stringify(previewData));
            }else{
                result.textContent = "無此會員";
            }
        }catch(error){
            console.error("Error querying member:", error);
        }
    }
});

// 若更新姓名為空的輸入，發送提醒；若非空的輸入，使用 fetch 函式向後端發送 PATCH 請求
document.getElementById("updateButton").addEventListener("click", async function(){
    const update = document.getElementById("update").value;
    const result = document.getElementById("updateResult");
    if (update === ""){
        alert("請輸入欲更新的姓名");
        return;
    }else{
        try{
            const response = await fetch(`/api/member`,{
                method: "PATCH",
                headers:{
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ name: update })
            });
            const data = await response.json();
            if (response.ok){
                result.textContent = "更新成功";
                const signinsystem = document.querySelector(".signinsystem");
                signinsystem.textContent = `${update}，歡迎登入系統`;
            }else{
                alert("無法更新姓名");
            }
        }catch(error){
            console.error("更新名稱時發生錯誤:", error);
            alert("更新名稱時發生錯誤");
        }
    }
    
});


