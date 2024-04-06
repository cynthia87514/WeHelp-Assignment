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