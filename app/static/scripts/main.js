let site_url = `${window.location.protocol}//${window.location.host}/products`;
const search = document.querySelector(".search-form");
const categories = document.querySelectorAll(".category"); // all categories in search page
const selectCategories = document.querySelectorAll(".select-category");
const navLinks = document.querySelectorAll("nav ul li a");
let category = "";
let query = "";

if (search) {
  search.addEventListener("submit", (event) => {
    event.preventDefault();
    const value = event.target.query.value;
    window.sessionStorage.setItem("query", value);
    query = window.sessionStorage.getItem("query");
    category = window.sessionStorage.getItem("category");

    if (category && !query) {
      site_url += `?category=${category}`;
    } else if (query === null || query.length === 0) {
      site_url += "";
    } else if (category && query) {
      site_url += `?query=${query}&category=${category}`;
    } else {
      site_url += `?query=${query}`;
    }

    window.location.href = site_url;
  });
}

// visual change when changing categories
function activeCategory() {
  categories.forEach((cat) => {
    if (cat.id === window.sessionStorage.getItem("category")) {
      cat.classList.add("category-active");
    } else {
      // removing active from all
      cat.classList.remove("category-active");
    }
  });
}

// search for a product by category
function searchByCategory() {
  query = window.sessionStorage.getItem("query");

  categories.forEach((cat) => {
    cat.onclick = function () {
      const category = cat.id;

      window.sessionStorage.setItem("category", category);

      if (query.length > 0) {
        site_url += `?query=${query}&category=${category}`;
      } else {
        site_url += `?category=${category}`;
      }
      activeCategory();
      window.location.href = site_url;
    };
  });
}
activeCategory();

// remove category from search filters
function clearFilter() {
  window.sessionStorage.removeItem("category");
  query = window.sessionStorage.getItem("query");

  if (query.length > 0) {
    site_url = `?query=${query}`;
  } else {
    site_url = `${site_url}`;
  }

  window.location.href = site_url;
}

// set the category we need when saving a product
selectCategories.forEach((cat) => {
  cat.onclick = function (e) {
    cat.setAttribute("selected", "selected");
  };
});
