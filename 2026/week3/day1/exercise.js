function displayNumbersDivisible(divisor = 23) {
    let sum = 0;

    for (let i = 0; i <= 500; i++) {
        if (i % divisor === 0) {
            console.log(i);
            sum += i;
        }
    }

    console.log("Sum:", sum);
}

displayNumbersDivisible();



const stock = {
    banana: 6,
    apple: 0,
    pear: 12,
    orange: 32,
    blueberry: 1
};

const prices = {
    banana: 4,
    apple: 2,
    pear: 1,
    orange: 1.5,
    blueberry: 10
};

const shoppingList = ["banana", "orange", "apple"];

function myBill() {
    let total = 0;

    for (let item of shoppingList) {
        if (item in stock && stock[item] > 0) {
            total += prices[item];
            stock[item]--;
        }
    }

    return total;
}

console.log("Total:", myBill());




function changeEnough(itemPrice, amountOfChange) {
    let [quarters, dimes, nickels, pennies] = amountOfChange;

    let total = (quarters * 0.25) +
        (dimes * 0.10) +
        (nickels * 0.05) +
        (pennies * 0.01);

    return total >= itemPrice;
}

console.log(changeEnough(4.25, [25, 20, 5, 0]));
console.log(changeEnough(14.11, [2, 100, 0, 0]));




function hotelCost(nights) {
    return nights * 140;
}

function planeRideCost(destination) {
    destination = destination.toLowerCase();

    if (destination === "london") return 183;
    if (destination === "paris") return 220;
    return 300;
}

function rentalCarCost(days) {
    let cost = days * 40;
    if (days > 10) cost *= 0.95;
    return cost;
}

function totalVacationCost() {
    let nights = Number(prompt("How many nights?"));
    let destination = prompt("Destination?");
    let days = Number(prompt("How many days car rental?"));

    let hotel = hotelCost(nights);
    let plane = planeRideCost(destination);
    let car = rentalCarCost(days);

    console.log(`Car: ${car}, Hotel: ${hotel}, Plane: ${plane}`);
    return hotel + plane + car;
}

totalVacationCost();



let div = document.getElementById("container");
console.log(div);

document.querySelectorAll(".list")[0].children[1].textContent = "Richard";

document.querySelectorAll(".list")[1].children[1].remove();

let lists = document.querySelectorAll(".list");
for (let ul of lists) {
    ul.children[0].textContent = "Giovanni";
}

for (let ul of lists) {
    ul.classList.add("student_list");
}
lists[0].classList.add("university", "attendance");

div.style.backgroundColor = "lightblue";
div.style.padding = "10px";

lists[1].children[2].style.display = "none";

lists[0].children[1].style.border = "1px solid black";

document.body.style.fontSize = "20px";

if (div.style.backgroundColor === "lightblue") {
    alert("Hello Giovanni and David");
}




let nav = document.getElementById("navBar");
nav.setAttribute("id", "socialNetworkNavigation");

let ul = nav.querySelector("ul");

let li = document.createElement("li");
let text = document.createTextNode("Logout");
li.appendChild(text);
ul.appendChild(li);

console.log(ul.firstElementChild.textContent);
console.log(ul.lastElementChild.textContent);




const allBooks = [
    {
        title: "Harry Potter",
        author: "J.K. Rowling",
        image: "https://via.placeholder.com/100",
        alreadyRead: true
    },
    {
        title: "The Hobbit",
        author: "J.R.R. Tolkien",
        image: "https://via.placeholder.com/100",
        alreadyRead: false
    }
];

let section = document.querySelector(".listBooks");

for (let book of allBooks) {
    let div = document.createElement("div");

    let text = document.createElement("p");
    text.textContent = `${book.title} written by ${book.author}`;

    let img = document.createElement("img");
    img.src = book.image;
    img.style.width = "100px";

    if (book.alreadyRead) {
        text.style.color = "red";
    }

    div.appendChild(text);
    div.appendChild(img);
    section.appendChild(div);
}





