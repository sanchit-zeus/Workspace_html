window.addEventListener('load',bindElements);

function bindElements(){
var headOne=document.getElementById("one");
var headTwo=document.getElementById("two")
var headThree=document.getElementById("three")

headOne.addEventListener('mouseover',function(){
  headOne.textContent="Mouse Currently Over";
  headOne.style.color="red";
})

headOne.addEventListener('mouseout',function(){
  headOne.textContent="Hover Over Me";
  headOne.style.color="black";
})

headTwo.addEventListener('click',function(){
  headTwo.textContent="Clicked";
  headTwo.style.color="red";
})
}
