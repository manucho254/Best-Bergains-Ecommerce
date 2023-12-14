let products_url = `${window.location.protocol}//${window.location.host}/products`;
const addToCartButton = document.getElementById("add-to-cart-button");
const shoppingCartTotal = document.getElementById("shopping-cart-total");
const quantityValue = document.getElementById("quantity-value");
const cartList = document.getElementById("cart-items");
const checkoutList = document.getElementById("checkout-items");
const cartSummary = document.getElementById("cart-summary");

// set cart in sessionStorage to empty array if it does not exist
if (!sessionStorage.getItem("cart")) {
  sessionStorage.setItem("cart", JSON.stringify([]));
}

// functionality for add to art button
if (addToCartButton) {
  addToCartButton.addEventListener("click", function () {
    const productIdElement = document.getElementById("product-id");
    const productNameElement = document.getElementById("product-name");
    const productPriceElement = document.getElementById("product-price");
    const productImageElement = document.getElementById("product-img");

    if (
      productIdElement &&
      productNameElement &&
      productPriceElement &&
      productImageElement
    ) {
      const productId = `${productIdElement.value}`;
      const productName = productNameElement.textContent;
      const productPrice = parseFloat(productPriceElement.textContent);
      const productImage = `${productImageElement.src}`;
      addItemToCart(productId, productName, productPrice, productImage);
    }
  });
}

function getCartItems() {
  /** Return an empty array or an array with all items in cart */
  const storedItems = sessionStorage.getItem("cart");
  return storedItems ? JSON.parse(storedItems) : [];
}

const cartItems = getCartItems();

function saveCartItems(cartItems) {
  /** Save cart items in sessionStorage */
  sessionStorage.setItem("cart", JSON.stringify(cartItems));
}

function renderCart() {
  /** Render items in storage on cart page  */
  cartList.innerHTML = "";

  if (cartItems.length == 0) {
    const noItems = document.createElement("li");

    noItems.innerHTML = `
	    <div class="d-flex flex-column gap-5 justify-content-center align-items-center">
			<h3> No items in the cart </h3>
			<a href="${products_url}"
				class="btn active text-light">Shop now
			<a>
		</div>`;
    cartList.appendChild(noItems);
    cartSummary.style.display = "none";
  }

  const totalPrice = cartItems.reduce(
    (total, item) => total + item.price * item.quantity,
    0
  );
  const cartTotalPrice = document.getElementById("cart-total");
  cartTotalPrice.classList.add("fw-bold");
  cartTotalPrice.innerText = `$ ${totalPrice.toFixed(2)}`;

  cartItems.forEach((item) => {
    const listItem = document.createElement("li");
    const cartNumItems = document.getElementById("cart-num-items");

    cartNumItems.innerText = `Cart: (${cartItems.length})`;
    listItem.className = "cart-item";
    listItem.innerHTML = `<div class="d-flex gap-4 w-100 text-dark">
	<img class="img-fluid w-25" src="${item.image}">
	<div class="d-flex flex-column gap-3">
	    <a class="text-dark" href="${products_url}/${item.id}" class="w-100">
		    <span>${item.name}</span>
		</a>
	    <span>$${(item.price * item.quantity).toFixed(2)}</span>
		<div class="d-flex gap-2">
			<button onclick="decreaseQuantity('${item.id}')">-</button>
			<span>Quantity: ${item.quantity}</span>
			<button onclick="increaseQuantity('${item.id}')">+</button>
		</div>
		<a class="text-danger text-decoration-underline"
		    onclick="removeItemFromCart('${item.id}')">Remove</a>
	</div>
	</div>`;
    cartList.appendChild(listItem);
  });
}

function addItemToCart(productId, productName, productPrice, productImage) {
  const existingCartItem = cartItems.find((item) => item.id === productId);

  if (existingCartItem) {
    existingCartItem.quantity += 1;
  } else {
    const cartItem = {
      id: productId,
      name: productName,
      price: productPrice,
      image: productImage,
      quantity: 1,
    };
    cartItems.push(cartItem);
  }
  saveCartItems(cartItems);
  getCartNumItems();
  addToCartAlert();
}

function removeItemFromCart(productId) {
  /** Remove item from cart by using the item id
   */
  const mapItems = cartItems
    .map((item) => {
      if (item.id !== productId) {
        return item;
      }
    })
    .filter((prod) => prod);

  saveCartItems(mapItems);
  window.location.reload();
}

function increaseQuantity(productId) {
  /** Increase the quantity of an item in cart  */
  const existingCartItem = cartItems.find((item) => item.id === productId);

  if (existingCartItem) {
    existingCartItem.quantity += 1;
    renderCart();
  }
}

function decreaseQuantity(productId) {
  /** Decrease the quantity of an item in cart  */
  const existingCartItem = cartItems.find((item) => item.id === productId);

  if (existingCartItem && existingCartItem.quantity > 1) {
    existingCartItem.quantity -= 1;
    renderCart();
  }
}

function getCartNumItems() {
  /** display the current number of items currently in the cart  */
  if (shoppingCartTotal) {
    shoppingCartTotal.innerText = `(${cartItems.length})`;
  }
}

function addToCartAlert() {
  /** Display alert when we add product to cart */
  const cartAlert = document.getElementById("cart-alert");

  cartAlert.classList.add("alert-box");
  cartAlert.innerHTML = `<span>Item added successfully to cart.</span>`;

  // remove alert box from dom
  setTimeout(function () {
    cartAlert.style.display = "none";
  }, 5000);
}

function renderCheckout() {
  /** Render data from storage in checkout page  */
  checkoutList.innerHTML = "";

  const totalPrice = cartItems.reduce(
    (total, item) => total + item.price * item.quantity,
    0
  );
  const cartTotalPrice = document.getElementById("cart-total");
  cartTotalPrice.classList.add("fw-bold");
  cartTotalPrice.innerText = `$ ${totalPrice.toFixed(2)}`;

  cartItems.forEach((item) => {
    const listItem = document.createElement("li");

    listItem.className = "cart-item";
    listItem.innerHTML = `<div class="d-flex gap-4 w-100 text-dark">
		<img class="img-fluid w-25" src="${item.image}">
		<div class="d-flex justify-content-between gap-3 w-100">
			<a class="text-dark" href="${products_url}/${item.id}" class="w-75">
				<span>${item.quantity}  x  ${item.name}</span>
			</a>
			<span>$${(item.price * item.quantity).toFixed(2)}</span>
		</div>
		</div>`;
    checkoutList.appendChild(listItem);
  });
}

if (cartList) {
  renderCart();
}
if (checkoutList) {
  renderCheckout();
}
getCartNumItems();
