function hello(){
  console.log("Hello World!");
}

function helloYou(name){
  console.log("Hello "+name)
}

function addNum(a,b){
  console.log(a+b)
}

function helloSomeone(name="Frankie"){
  console.log("Hello "+name)
}

function formal(name="sam",title="sir"){
  return name+" "+title;
}

var stuff="Global Stuff"
var v="Global V"
function fun(stuff){
  console.log(v)
  stuff="reassign value"
  console.log(stuff)
}
fun()
console.log(stuff)
