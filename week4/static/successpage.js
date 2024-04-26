document.addEventListener("DOMContentLoaded", function(){
    var signoutLink = document.getElementById("signout");

    signoutLink.addEventListener("click", function(){
        fetch("/signout").then(function(response){
            if(response.ok){
                window.location.href = "/";
            }
        })
    })
})