class Animal {

    // default class variables
    // eye = 2
    // leg = 4

    // constructor(){
            // a Class mya only have one constructor
    // }

    // writing custom constructor for the objects
    constructor(eye,leg){
        this.eye = eye
        this.leg =  leg
    }

    // writing methods for getting the values

    see(){
        console.log(
            "The Animal can watch with it's "+this.eye+" eyes"

        )
    
    
    }

    run(){
        console.log(
            "The Animal can run with it's "+this.leg+" legs"
        )
    }
    
}

// creating objects of the classes

var myObj = new Animal(2,4)

myObj.see()

myObj.run()


// Inheritance in Js

// creating the child class
class Cat extends Animal{

    constructor(eye,leg,sound){
        super(eye,leg) // super inherit the parent constructor
        this.sound = sound
    }


    // overriding the old methods
    see(){
        console.log(
            "The Cat can watch with it's "+this.eye+" eyes"

        )
    
    
    }

    run(){
        console.log(
            "The Cat can run with it's "+this.leg+" legs"
        )
    }

    // creating new methods for the cat class, itself...


    speaks(){
        console.log(
            "The Cat speaks "+this.sound+" sound"
        )
    }


}


// creating the object of the child class [cat class]

var kitty = new Cat(2,4,"meeeeaw")

console.log("================================================================")
kitty.see()
kitty.run()
kitty.speaks()
