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
var p = new Promise((resolve,reject) => {
    let a = 1+1 
    // if we change a = 1+2, we get Failed else we get Success
    if(a == 2){
        resolve("Success")
    }
    else{
        reject("Failed")
    }
}
)

// now executing the promise
p.then((message) => {
    console.log("This is from then : "+message)
})

p.catch((message) => {
    console.log("This is from catch : "+ message)
} )