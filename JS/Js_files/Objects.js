ans = confirm("Are you waked up ? ")
document.write(ans)

john = {
    full_name: "John Doe",
   dob : 1998,
    age : function(dob){
        return 2020 - this.dob
    }

}

console.log(john.full_name)
console.log(john.age)
console.log(john.age(1996))
console.log(john.age(john.dob))
console.log(john)
