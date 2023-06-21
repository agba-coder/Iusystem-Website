// Get the button and the navbar elements
var button = document.getElementById("menu-toggle");
var navbar = document.getElementById("navbar");

// Add an event listener to the button to toggle the navbar visibility when clicked
button.addEventListener("click", function() {
    navbar.classList.toggle("hidden");
});
