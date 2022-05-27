/*!
* Start Bootstrap - Shop Homepage v5.0.5 (https://startbootstrap.com/template/shop-homepage)
* Copyright 2013-2022 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-shop-homepage/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project
function addCart(num) {
     let numberCart = document.getElementById("spanCart").innerHTML
     document.getElementById("spanCart").innerHTM=""
     document.getElementById("spanCart").innerHTML= numberCart + num
    
}

function setCart(num){
    document.getElementById("spanCart").innerHTML=num
}

