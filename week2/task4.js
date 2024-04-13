function getNumber(index){
    var x = Math.floor(index / 3);
    var y = index % 3;
    var result = 7*x + 4*y;
    console.log(result);// your code here
}
getNumber(1); // print 4
getNumber(5); // print 15
getNumber(10); // print 25
getNumber(30); // print 70