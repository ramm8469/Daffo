console.log("Arrays Demo in JS")

// Intializing an array
fruits = ['Banaa','Apple','Carrot','Orange']

console.log(fruits)

// Pushing an element to the array with predefined methods
fruits.push("Papaya")
console.log(fruits)

// Poping out an element from the array
fruits.pop()

console.log(fruits)

// Pushing an element at the begining of the array
fruits.unshift("Papaya")

console.log(fruits)

// Pushing an element at the end of the array
fruits.shift("Papaya2")

console.log(fruits)

// reversing an array
function myreverseArrray(){
    fruits.reverse()
    document.getElementById("reverses").innerHTML = fruits
}

// sorting an array
function sortArray(){
    fruits.sort()
    document.getElementById("sort").innerHTML = fruits
}

// original array
function original(){
    document.getElementById("original").innerHTML = fruits
}

// For each loop in Js
digits = [1,2,3,4,5,6,7,8,9]
digits.forEach(i => {
    console.log(i+" ")
});