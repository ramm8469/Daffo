console.log()
console.log("===================================================")
console.log("Map-Reduce-Filter")
console.log("===================================================")
console.log()


// Map() Demo

// What you have
var officers = [
    { id: 20, name: 'Captain Piett' },
    { id: 24, name: 'General Veers' },
    { id: 56, name: 'Admiral Ozzel' },
    { id: 88, name: 'Commander Jerjerrod' }
  ];
  // What you need
  //[20, 24, 56, 88]



// we can use map to get that..
var officersIds = [];
// officers.forEach(function (officer) {
//     officersIds.push(officer.id);
//   });
officersIds = officers.map( officer => officer.id)

console.log(officersIds)

// Another example on map
// square of a number
console.log("=====Another Demo on the map() method in JS ===")
var myNum = [1,2,3,4,5,6,7,8,9]
var myData = myNum.map ( x => x*x)
var mynewData = myNum.map((x,y) => (x*2+y))
console.log(myData)
console.log(mynewData)

console.log("Question Asked On Map")

// question on map
// fibonnacci Series...
var data = [1,2,3,4,5,6,7,8,9].map(
    (x,y) => x+y
)

// Printing the result
console.log(data)
console.log("=================================")

// Reduce Demo
// i'm confused in while understanding reduce()
console.log("=================Reduce================")

 var nums = [1,2,3,4,5,6,7,8]
 var ress = nums.reduce((d,sum) =>  sum + d)
 console.log(ress)

// Filter Demo
// Filter is a predefined function, used to filter out 
// some elements from the array of elements

var nums = [1,2,3,4,5,6,7,8,9,10]
 var even = nums.filter((ele) => {
     if(ele%2 == 0){
         return ele
     }
     else{
         console.log("false0")
     }
 })
 console.log(even)

 // question on context
var obj1 = {
    first : "john",
    last : "doe",
    first_name : () => {console.log(this.first)},
    last_name : function(){
        console.log(this.last)
    }
}


// console.log("Context question")
// obj1.first_name()
// obj1.last_name()

// object question
obj1 = {
    name : "john"
}
obj2 = {
    name:"john"
}

obj3 = obj1

console.log(obj1 === obj3)
console.log(obj1 === obj2) 
console.log(obj1 == obj3)
console.log(obj1 == obj2)
