console.log("dfghj")

// var player1=prompt("player one: Enter your name, you will be blue");
// var player1color="rgb(86,151,255)";
//
// var player2=prompt("player Two: Enter your name, you will be red");
// var player1color="rgb(237,45,73)";
//
// var game_on=true;
// var table=$("table tr");
//
// function reportWin(rowNum,ColNum){
//   console.log("You won starting at this row,col");
//   console.log(rowNum);
//   console.log(rowNum);
// }
//
// function changeColor(rowIndex,colIndex,color){
//   return table.eq(rowIndex).find("td").eq("colIndex").find("button").css("background-color");
// }
//
// function returnColor(rowIndex,colIndex,color){
//   return table.eq(rowIndex).find("td").eq("colIndex").find("button").css("background-color");
// }
//
// function checkBottom(colIndex){
//   var colorReport=returnColor(5,colIndex);
//   for (var row = 5; row > -1; i--) {
//     colorReport=returnColor(row,colIndex);
//     if(colorReport==="rgb(128,128,128)"){
//       return row;
//     }
//   }
// }
//
// function colorMatchCheck(one,two,three,four){
//   return(one===two&&one===three&&one===four&&one!=="rgb(128,128,128)"&&one!==undefined)
// }
//
// //checks for horizontal wins
// function horizontalWinCheck() {
//   for (var row = 0; row < 6; row++) {
//     for (var col = 0; col< 4; col++) {
//       if(colorMatchCheck(returnColor(row,col),returnColor(row,col+1),returnColor(row,col+2)))
//       console.log("horiz");
//       reportWin(row,col);
//       return true;
//     // }else {
//     //   continue;
//     }
//   }
// }
//
// //checks fo vertical wins
// function verticalWinCheck() {
//   for (var row = 0; row < 7; col++) {
//     for (var col = 0; col< 3; row++) {
//       if(colorMatchCheck(returnColor(row,col),returnColor(row+1,col),returnColor(row+2,col)))
//       console.log("vertical");
//       reportWin(row,col);
//       return true;
//     // }else {
//     //   continue;
//     // }
//   }
// }
//
// //checks for diognal wins
// function diognalWinCheck() {
//   for (var col = 0; col <5 ; col++) {
//     for (var row = 0; row< 7; row++) {
//       if(colorMatchCheck(returnColor(row,col),returnColor(row+1,col+1),returnColor(row+2,col+2)))
//       console.log("diag");
//       reportWin(row,col);
//       return true;
//     }else if colorMatchCheck(returnColor(row,col),returnColor(row-1,col+1),returnColor(row-2,col+2))) {
//       console.log("diag");
//       reportWin(row,col);
//       return true;
//
//     }else {
//       continue;
//     }
//   }
// }
//
// var currentPlayer=1;
// var currentName=player1;
// var currentColor=player1Color;
//
// $("h3").text(player1+"it is your turn, pick a column to drop in!")
// $(".board button").on("click",function(){
//   var col=$(this).closest('td').index();
//   var buttomAvail =checkBottom(col);
//   changeColor(bottomAvail,col,currentColor);
//   if(horizontalWinCheck()||verticalWinCheck()||diognalWinCheck()){
//     $("h1").text(currentName+"You have won!")
//     $("h3").fadeout("fast");
//     $("h2").fadeout("fast");
//   }
//   currentPlayer=currentPlayer*-1;
//   if (currentPlayer===1) {
//     currentName=player1;
//     $("h3").text(currentName+" it is your turn")
//     currentColor=player1color;
//   }else {
//     currentName=player2;
//     $("h3").text(currentName+ "it is your turn")
//     currentColor=player2Color;
//   }
// )}
