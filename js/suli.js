$(document).ready(function(){
var li_box='';
var sy_box='';
var check=false;




  $('.wrapper').on("click", "#su", function(){
    if (check == true){
      $('.overlay-container').fadeIn();
    }else{
    $('.wrapper').append(input_box).fadeIn();
    check = true;
    }
  });

$('.wrapper').on("click", "#exit-button", function(){
  $('.overlay-container').fadeOut();
});
})