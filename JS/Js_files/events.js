// function myFunction(){
//     document.getElementById("demo").innerHTML="Paragraph Changed";
// }

function myFunction() {
    document.getElementById("demo").innerHTML = "Paragraph changed.";
  }

function greet(){
    document.getElementById("greet").innerHTML="Welcome User to The JS Demo ";
}

var x
var y = null
console.log(typeof(x))
console.log(typeof(y))
var xx = 'infinity'
var yy = "Infinity"
console.log(typeof(xx)+" - "+ typeof(yy))
var z = Symbol('a')
var zz = Symbol('a')
console.log(typeof(z)+" - "+typeof(zz))// Symbol - Symbol
console.log(z == zz) // false
var ram = Symbol("ram")
str = "hello World"
console.log(str[0])
console.log(ram)