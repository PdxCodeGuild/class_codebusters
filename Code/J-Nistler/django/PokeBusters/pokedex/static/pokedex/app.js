// NAVSLIDE FOR MOBILE NAVIGATION
const navSlide = () => {
  // Grab HTML elements
  const navBurger = document.querySelector(".nav-burger");
  const nav = document.querySelector(".nav-links");
  const navLinks = document.querySelectorAll(".nav-links li");
  // TOGGLE NAV
  // Listen for click on the nav-burger element
  navBurger.addEventListener("click", () => {
    // Toggle the transformation
    nav.classList.toggle("nav-active");

    // ANIMATE LINKS
    navLinks.forEach((link, index) => {
      // If the animation has already occured, remove it so it can play again on re-open
      if (link.style.animation) {
        link.style.animation = "";
      }
      // Play animation with slight delay based on number of elements
      else {
        link.style.animation = `navLinkFade 0.5s ease forwards ${
          index / 7 + 0.3
        }s`;
      }
    });
  });
};

// Call Function
navSlide();
