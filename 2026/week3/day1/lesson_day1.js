function drinkCoffee() {
    console.log("The user drinks coffee in the morning");
}

drinkCoffee();



function userInfo(userName, userAge = 20) {
    console.log("My name is " + userName + ", my age is " + userAge);
}

userInfo("Sarah"); //My name is Sarah, my age is 20
userInfo("Ben", 40); //My name is Ben, my age is 40



//global variable 
let eyeColor = "blue";

function userMoreInfo(userName, userAge) {
    console.log("My name is " + userName + ", my age is " + userAge + ", I have " + eyeColor + " eyes");
}

userMoreInfo("Sarah", 22); //My name is Sarah, my age is 22, I have blue eyes
console.log(eyeColor); // blue

function favoriteColor() {
    console.log("My favorite color is " + eyeColor);
}

favoriteColor(); //My favorite color is blue




// 1. Create a structured HTML file linked to a JS file

// 2. Write a Javascript function that takes a parameter: myAge

function ageCalc(myAge) {


// 3. In the function, console.log the age of my mum and my dad.My mum is twice my age, and my dad is 1.2 the age of my mum.

const mum = myAge * 2
const dad = mum * 1.2

console.log("Mum is " + mum + " years old, and dad is " + dad + " years old")

}

// 4. Call the function.

ageCalc(36);
ageCalc(66);
ageCalc(10)




function userInfo(userName, userAge) {
    if (userName === "Sarah") {
        let result = "Hey " + userName;
        return result;
    } else {
        return "You are not the right person";
    }
}

let girlInfo = userInfo("Sarah", 22);
console.log(girlInfo); //Hey Sarah




// For each of the questions, find 2 WAYS of accessing :

// 1. The div DOM node?

const div2 = document.body.firstElementChild;

console.log(div1)
console.log(div2)

// 2. The ul DOM node?

const ul1 = document.body.children[1];
const ul2 = div1.nextElementSimbling;

console.log(ul1)
console.log(ul2)

// 3. The second li (with Pete)?

const pete1 = ul1.lastElementChild;
let pete2 = document.body.children[1].children[1];

console.log(pete1)
console.log(pete2)