console.log("===================================================")
console.log("This page is to illustrate the call back hell in Js")
console.log("===================================================")
console.log()



/* Call Back hell is a loop of calling 
    one function by another function till the
    call back stack is not empty and then executing
    the instructions of a function one by one

    Call Back Hell is a loop hole in js, which complicates
    the process of async. while calling multiple function

    To overcome callback hell, we use "Promises" in JS
*/

// Call back hell demo

function foo(){
    console.log(1)
    setTimeout(
        () => {
            console.log(2),
            setTimeout(
                () => {
                    console.log(3),
                    setTimeout(
                        () => {
                            console.log(4)
                        },1500

                    )
                    console.log(6)
                },1500
            )
            console.log(7)
        },1500
        
    )
    
    console.log(8)
}

//calling the foo function

foo()