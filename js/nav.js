//Code by Mark-Olvier Poulin
//This code is for all the animation you see in the navigation bar as well as the navigation of the home page
//var for logo animation
var time_on=0;
var time_out=0;
var count=0;
var active=false;
$(document).ready(function(){
var lastScrollTop = 0;
//scrolling animations

window.addEventListener("scroll", function(){

  var st = window.pageYOffset || document.documentElement.scrollTop;
  var header = document.getElementById('header');
  var logo_text = document.getElementById('nav-logo-text');
  var	ypos = window.pageYOffset;

  if (ypos > 250 ){


    if (st > lastScrollTop){
        //downscroll
        header.style.margin="-70px 0";
      }
      else {
        // upscroll
        header.style.margin="0";
       }
  }
  
  if(ypos > 150){
     header.style.backgroundColor="white";
     header.style.boxShadow="0 1px 13px rgba(0, 0, 0, 0.45)";

    }
  if(ypos <=150){
       header.style.backgroundColor="transparent";
       header.style.boxShadow="none"; 
  }

  lastScrollTop = st <= 0 ? 0 : st; // For Mobile
}, false);

})