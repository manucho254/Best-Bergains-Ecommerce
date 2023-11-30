let link = document.querySelector("nav-link");

link.addEventListener("click", (event) => {
  document
    .querySelectorAll("nav-link")
    .forEach((link) => link.classList.remove("active"));
});