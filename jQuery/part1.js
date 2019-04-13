// $('h1').click(function(){
//   console.log('There was a click')
// })
//
// $('li').click(function(){
//   console.log('There was a click')
// })

// $('h1').click(function(){
//   $(this).text("I was changed");
// })

$("input").eq(0).keypress(function(){
  $("h2").toggleClass("turnblue");
})

//grabs the events
// $("input").eq(0).keypress(function(event){
//   console.log(event);
// })

$("input").eq(0).keypress(function(event){
  if (event===13) {
    $("h2").toggleClass('turnblue')
  }
})

//on()
// $("h1").on("mouseover",function(){
//   $(this).toggleClass("turnblue");
// })
// $("h1").on("mouseout",function(){
//   $(this).toggleClass("turnblue");
// })

$("h1").on("mouseenter",function(){
  $(this).toggleClass("turnblue");
})

//animation
$("input").eq(1).on("click",function(){
  $(".container").fadeOut(300);
})
