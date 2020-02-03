console.log(Number.MAX_VALUE)
console.log(Number.MIN_VALUE)
console.log(Number.NaN)
// above are different Number global Methods in Js
console.log("The above are different Java Script Global Methods")
// Number Constructor to Convert any thing to number(which can be converted to a number)

console.log("These are the Different Output Generated using the Number() Constructor")

console.log(Number(true))          // returns 1
console.log(Number(false))        // returns 0
console.log(Number("10"))          // returns 10
console.log(Number("  10"))       // returns 10
console.log(Number("10  "))       // returns 10
console.log(Number(" 10  "))       // returns 10
console.log(Number("10.33"))       // returns 10.33
console.log(Number("10.33"))       // returns NaN
console.log(Number("10 33"))     // returns NaN
console.log(Number("John"))       // returns NaN 

// For parsing a number to Integer and Float, we use the global number methods...

// For parsing something to Int
console.log("We are now parsing any number or string to integer")

console.log(parseInt("10"))         // returns 10
console.log(parseInt("10.33"))     // returns 10
console.log(parseInt("10 20 30"))  // returns 10
console.log(parseInt("10 years"))   // returns 10
console.log(parseInt("years 10"))  // returns NaN  

// For parsing Something to Float
console.log("We are now parsing any number or string to float")

console.log(parseFloat("10"))       // returns 10
console.log(parseFloat("10.33"))     // returns 10.33
console.log(parseFloat("10 20 30"))  // returns 10
console.log(parseFloat("10 years"))  // returns 10
console.log(parseFloat("years 10"))  // returns NaN 
