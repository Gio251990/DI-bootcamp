const people = ["Greg", "Mary", "Devon", "James"];

people.shift();


people[people.indexOf("James")] = "Jason";


people.push("IlTuoNome");


console.log(people.indexOf("Mary")); // Output: 0


const copy = people.slice(1, -1);
console.log(copy);


console.log(people.indexOf("Foo"));



let last = people[people.length - 1];


for (let person of people) {
    console.log(person);
}

for (let person of people) {
    console.log(person);
    if (person === "Devon") {
        break;
    }
}



const colors = ["Blue", "Red", "Green", "Yellow", "Purple"];
const suffixes = ["st", "nd", "rd", "th", "th"];

for (let i = 0; i < colors.length; i++) {
    
    console.log(`My #${i + 1} choice is ${colors[i]}`);

}


let number;
do {

    number = Number(prompt("Please enter a number:"));
} while (number < 10);

console.log("Great! The number is 10 or bigger.");



const building = {
    numberOfFloors: 4,
    numberOfAptByFloor: {
        firstFloor: 3,
        secondFloor: 4,
        thirdFloor: 9,
        fourthFloor: 2,
    },
    nameOfTenants: ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent: {
        sarah: [3, 990],
        dan: [4, 1000],
        david: [1, 500],
    },
}


console.log(building.numberOfFloors);


console.log(building.numberOfAptByFloor.firstFloor + building.numberOfAptByFloor.thirdFloor);


let secondTenant = building.nameOfTenants[1];
console.log(`${secondTenant} has ${building.numberOfRoomsAndRent.dan[0]} rooms.`);


let sarahAndDavidRent = building.numberOfRoomsAndRent.sarah[1] + building.numberOfRoomsAndRent.david[1];
if (sarahAndDavidRent > building.numberOfRoomsAndRent.dan[1]) {
    building.numberOfRoomsAndRent.dan[1] = 1200;
}




const family = { father: "John", mother: "Jane", son: "Jack" };


for (let key in family) {
    console.log(key);
}


for (let key in family) {
    console.log(family[key]);
}



const details = { my: 'name', is: 'Rudolf', the: 'reindeer' };
let sentence = "";

for (let key in details) {
    sentence += `${key} ${details[key]} `;
}
console.log(sentence.trim());




const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
let acronym = [];

for (let name of names) {
    acronym.push(name[0]);
}


console.log(acronym.sort().join(""));