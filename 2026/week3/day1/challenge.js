const planets = [
    { name: "Mercury", color: "gray", moons: 0 },
    { name: "Venus", color: "orange", moons: 0 },
    { name: "Earth", color: "blue", moons: 1 },
    { name: "Mars", color: "red", moons: 2 },
    { name: "Jupiter", color: "brown", moons: 4 },
    { name: "Saturn", color: "gold", moons: 3 },
    { name: "Uranus", color: "lightblue", moons: 2 },
    { name: "Neptune", color: "darkblue", moons: 2 }
];

const section = document.querySelector(".listPlanets");

for (let planet of planets) {
    let planetDiv = document.createElement("div");
    planetDiv.classList.add("planet");
    planetDiv.style.backgroundColor = planet.color;
    planetDiv.textContent = planet.name;

    for (let i = 0; i < planet.moons; i++) {
        let moon = document.createElement("div");
        moon.classList.add("moon");

        moon.style.top = (20 + i * 15) + "px";
        moon.style.left = (20 + i * 20) + "px";

        planetDiv.appendChild(moon);
    }

    section.appendChild(planetDiv);
}