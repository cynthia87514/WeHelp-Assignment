document.addEventListener("DOMContentLoaded",function(){
    var submit = document.getElementById("submit");

    submit.addEventListener("click", function(event){
        var checkbox = document.getElementById("checkbox");
        if (!checkbox.checked){
            alert("Please check the checkbox first");
            event.preventDefault(); // 阻止表單提交
            window.location.href = "/"; // 導回到登入頁面
        }
    })
});


/*
document.addEventListener("DOMContentLoaded", function() {
    var submit = document.getElementById("submit");
    var usernameInput = document.getElementById("username");
    var passwordInput = document.getElementById("password");

    // 獲取 URL 查詢參數
    const urlParams = new URLSearchParams(window.location.search);
    const username = urlParams.get('username');
    const password = urlParams.get('password');
    if (username && password) {
        // 將 URL 查詢參數中的值填入對應的輸入框
        usernameInput.value = username;
        passwordInput.value = password;
    }

    submit.addEventListener("click", function(event) {
        var checkbox = document.getElementById("checkbox");
        if (!checkbox.checked) {
            alert("Please check the checkbox first");
            event.preventDefault(); // 阻止表單提交
            window.location.href = "/?username=" + usernameInput.value + "&password=" + passwordInput.value; // 導回到登入頁面並傳遞帳號密碼
        }
    });
});

*/