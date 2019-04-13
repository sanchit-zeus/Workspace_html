
var stu=[];
var z=prompt("Would you like to start roster Web App? (y/n)");
while (z="y") {
  var x=prompt("Please Select an Action?(add,remove,display,exit)");

  switch (x) {
    case "add":
      var name=prompt("Enter the name:")
      stu.push(name);
      break;

      case "display":
        console.log(stu);
      break;

      case "remove":
        var rem=prompt("Enter the element to remove:")
          var index=stu.indexof(rem);
          stu.splice(index,1);
        break;

      case "exit":
        exit();
        alert("Thanks for using the web app. Refresh to start over.")
        break;
    default:prompt("Invalid Input")
  }
}
