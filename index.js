console.log('ok');
var xmlhttp = new XMLHttpRequest();
var url = "myTutorials.txt";
xmlhttp.onreadystatechange = function() {
    if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
        //var myArr = JSON.parse(xmlhttp.responseText);
        console.log(xmlhttp.responseText);
    }
};
console.log(JSON.stringify({"yoikijenengku":"oke ae"}));
//xmlhttp.open("GET", 'http://localhost:9999/api/users/3', true);
xmlhttp.open("POST", 'http://localhost:9876/api/', true);
xmlhttp.send();