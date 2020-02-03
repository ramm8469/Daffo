console.log("Here Illustrating the Sets DataStructure in JS")

/*
A Set is a special type collection –
 “set of values” (without keys), 
where each value may occur only once.
*/

// creating a new set

var mySet = new Set()


// printing the empty set
console.log(mySet)

// adding elements to the set using add(ele) methods
mySet.add(1)
mySet.add(2)
mySet.add(1)
mySet.add(3)
mySet.add(1)
mySet.add(4)
mySet.add(1)
mySet.add(5)


// printing the set with the data in it
console.log(mySet)

// getting the value from the set
for (let data of mySet){
    console.log(data)
}

// deleting a value from the set
console.log(mySet.delete(5)) // returns true if value is present and deleted, else false

// getting the size/length of the set
console.log(mySet.size)
console.log(mySet)



