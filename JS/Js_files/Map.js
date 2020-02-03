/* Map in Js is very similar to objects in js
The basic difference in Object and Map is that map 
can have key of any type, even map can contain 
object as a key, whereas Object does not have this 
feature
*/

// Creating a map 
var myMap = new Map()

console.log(Map)


// adding keyed data to the map
myMap.set("Name","John Doe")
myMap.set("Age",23)

// getting the size of the map
console.log("Size of the Map : "+myMap.size)

console.log(myMap)

// getting the value from the map
console.log(myMap.get("Name"))
console.log(myMap.get("Age"))

// deleting value from the map
console.log(myMap)

myMap.delete("Name")
myMap.delete("Age")

console.log(myMap)

// now checking the size of the map
console.log("Size of the Map : "+myMap.size)



console.log("Using object as map's key")
console.log("\n")
console.log("===================")
console.log("\n")

// creating an object
john = {
    full_name  : "John  Doe",
    age:24,
    address : "Mountain View, California"
}

console.log(john)

myMap.set(john,"Object")

console.log(myMap)

// trying to extract the object value from the 
// key as of a map

console.log(myMap.get(john.full_name))

// we get an undefined variable's value here

// now trying to add object value to the map

myMap.set(john.full_name_new,"New John Name")

// and getting that value
console.log(john.full_name_new)

// adding some content to the map
myMap.set("Country","India")
myMap.set("State","Haryana")
myMap.set("Location","Sector 30")

console.log(myMap)
// Iteration over Map keys,values and key-value pairs

// Over the keys

for(let key of myMap.keys()){
    console.log("The Key is  :"+key)
}


// Iterating over the values
for(let val of myMap.values()){
    console.log("The Value is : "+val)
}


// Iterating over Key-Value Pairs

for(let data of myMap){
    console.log("The data is : "+data)
}


// Using the for each built in feature of map to read the data

myMap.forEach((value,key,myMap)) => {
    console.log("The key is : "+key+" and the value is  :"+val);
}
