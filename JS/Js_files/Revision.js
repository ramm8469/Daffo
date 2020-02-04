console.log("This is a Revision File")

// scoping demo
function foo(){
    var a = 6
    function bar(){
        var a = 5
        function test(){
            a = 7
            console.log("test >>>"+a)
        }
        test()
        console.log("bar >>> "+a)
    }
    bar()
    console.log("foo >>> "+a)
}

//foo()


// context demo

// regular object method
var john = {
    name:"John doe",
    full_name:function(){
        console.log(this.name)
    }
}

// john.full_name()

// regular funtion
function data(){
   let a = "my"
    console.log(this.a)
}

// data()

// console.log("0" === true)
// console.log("1" === true)
// console.log(+'34'+'10')
// document.write(typeof typeof(24.49))

// console.log("first");
// setTimeout(function(){
//     console.log("second"),-1000
// })

// console.log("third")


var person = {
    name:"jack",
    prop:{
        name:"daniel",
        getName:function(){
            return this.name
        }
    }
}

// var name = person.prop.getName
// console.log(name)


// var name = person.prop.getName.bind(person)
// console.log(name)


// const arr  =[10,12,15,21]

// for(let i = 0;i<arr.length;i++){
//     setTimeout(function(){
//         console.log("index"+i+" element "+arr[i])
//     },3000)
    
// }


// promises in js
// promises in js are nothing but just a real life
// promise, where if promise is commited then it is
// accepted else it is rejected

// in js- promise, we use resolve and reject
// whenever something is accepted it goes to resolve
// else goes to reject statement

// it is accessed as follows
// resolve is accessed via then method
// and reject is accessed via catch method

// now let's do this in a practical manner

// creating a new promises
// var p = new Promise((resolve,reject) => {
//     let a = 1+1
//     // if we change a = 1+2, we get Failed else we get Success
//     if(a == 2){
//         resolve("Success")
//     }
//     else{
//         reject("Failed")
//     }
// }
// )

// now executing the promise
// p.then((message) => {
//     console.log("This is from then : "+message)
// })






// p.catch((message) => {
//     console.log("This is from catch : "+ message)
// } )

// question 1

// Promise.resolve(5)
// .then(
//     function(res){
//         console.log(res)
    
//     setTimeout(
//         function(){
//             return 8
//         }
//         )
//     }
// )
// .then(
//     function(res){
//         console.log(res)
//     }
// )


// question 2
// Promise.reject(5)
//     .then(
//         function(res){
//             console.log(res)
//             return 6
//         }
//     )
//     .catch(
//         function(err){
//             console.log(err)
//         }
//     )
//     .then(
//         function(res){
//             console.log(res)
//             return 6
//         }

//     )
//     .catch(
//         function(err){
//             console.log(err)
//         }
//     )


// question 3
// Promise.all(
//     [
//         Promise.resolve(5),
//         Promise.reject(66),
//         Promise.resolve(2),
//         Promise.reject(77)
        
//     ]
// )
// .then(console.log)
// .catch(console.log)

// Call back hell demo

// function foo(){
//     console.log(1)
//     setTimeout(
//         () => {
//             console.log(2),
//             setTimeout(
//                 () => {
//                     console.log(3)
//                     setTimeout(
//                         () => {
//                             console.log(4)
//                         },
//                         console.log(5),
//                         1500
//                     )
//                 },
//                 console.log(6),
//                 1500
//             )
//         },
//         console.log(7),
//         1500
//     )
//     console.log(8)
// }

// calling the foo

// foo()


// Classes in Js

class Animal{
    constructor(eye,leg){
        this.eye = eye
        this.leg = leg
    }

    // trying  to overload the constructor 
    // constructor(eye,leg,wings){
    //     this.eye = eye
    //     this.leg = leg
    //     this.wings = wings
    // }

    // constructor overloading is not possible in js
   
    // Defining methods in class
    see(){
        console.log("The animal can see with it's "+this.eye+" eyes")
    }

    walk(){
        console.log("The animal can walk with it's "+this.leg+" legs")
    }

}

// creating objects of animal class
 var cat =  new Animal(2,4)
 cat.see()
 cat.walk()

 var butterfly = new Animal(4,6)

 butterfly.see()
 butterfly.walk()

//  // creating object of animal class to check constructor overloading
//  var ins = new Animal(2,6,2)

//  ins.walk()
//  ins.see()


 // Inheritance in JS

 class Insects extends Animal{
    

    constructor(eye,leg,wings){
        super(eye,leg)
        this.wings = wings
    }

    fly(){
        console.log("The insect can fly with it's "+this.wings+" wings")            

    }

    // checking method overloading in js
    fly(direction){
        console.log("The insect can fly with it's "+this.wings+" wings"+" in "+direction+" direction")            
        
    }

    // method overloading is not possible in js, as the most last 
    // method overwrite all the previous method with the same name


    // checking the method overriding in js
    see(){
        console.log("The insects can see better than any other animals")
    }

    // Method overriding is possible in js
 }
 console.log()

 // creating object of the child class(insect class)
//  var titli = new Insects(4,6,2)
//  titli.see() // this see() method from insect class is overrided inherited from the Animal Class
//  titli.walk()
//  titli.fly()
//  titli.fly("north")


 // Prototypal Inheritance or Prototyping in JS

 let animal = {
    eats: true,
    run: function(){
        console.log("Animals can run")
    }
  };
  let rabbit = {
    jumps: true,
    // trying to override the run method
    run:function(){
        console.log("Rabbit can run faster")
    }
  };
  
  rabbit.__proto__ = animal;

  console.log(animal.eats)
  console.log(rabbit.eats)
  console.log(rabbit.jumps)
  console.log(animal.run())
  console.log(rabbit.run())


 