const hamburger = document.querySelector(".hamburger");
const navMenu = document.querySelector(".nav-menu");


hamburger.addEventListener("click", () => {
    hamburger.classList.toggle("active");
    navMenu.classList.toggle("active");
})

document.querySelectorAll(".nav-link").forEach(n => n.addEventListener("click", () => {
    hamburger.classList.remove("active");
    navMenu.classList.remove("active");
}))

const icon = document.querySelector(".icon");
const search = document.querySelector(".search");
const clearSearch = document.querySelector(".clear");

icon.onclick = function() {
    search.classList.toggle("active");
}

clearSearch.onclick = function() {
    document.getElementById('mysearch').value = '';
    search.classList.remove("active");
}