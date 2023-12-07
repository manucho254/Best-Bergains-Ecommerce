const addToCartButton = document.getElementById("add-to-cart-button");

addToCartButton.addEventListener("click", function () {
	    const productIdElement = document.getElementById("product-id");
	    const productNameElement = document.getElementById("product-name");
	    const productPriceElement = document.getElementById("product-price");

	    if (productIdElement && productNameElement && productPriceElement) {
		            const productId = parseInt(productIdElement.value, 10);
		            const productName = productNameElement.textContent;
		            const productPrice = parseFloat(productPriceElement.textContent);
		            addItemToCart(productId, productName, productPrice);
		        }
});

function getCartItems() {
	    const storedItems = sessionStorage.getItem("cart");
	    return storedItems ? JSON.parse(storedItems) : [];
}

function saveCartItems(cartItems) {
	    sessionStorage.setItem("cart", JSON.stringify(cartItems));
}

const cartItems = getCartItems();

function renderCart() {
	const cartList = document.getElementById("cart-items");
	const totalPriceElement = document.getElementById("total-price");

	cartList.innerHTML = "";
	const totalPrice = cartItems.reduce((total, item) => total + item.price * item.quantity, 0);
	totalPriceElement.textContent = totalPrice.toFixed(2);

	cartItems.forEach(item => {
		const listItem = document.createElement("li");
	        listItem.className = "cart-item";
	        listItem.innerHTML = `<span>${item.name}</span><span>$${(item.price * item.quantity).toFixed(2)}</span>
			<button onclick="decreaseQuantity(${item.id})">-</button>
	                <span>Quantity: ${item.quantity}</span>
	                <button onclick="increaseQuantity(${item.id})">+</button>`;
		cartList.appendChild(listItem);
	});
	saveCartItems(cartItems);
}

function addItemToCart(productId, productName, productPrice) {
	const existingCartItem = cartItems.find(item => item.id === productId);

	if (existingCartItem) {
		existingCartItem.quantity += 1;
	} else {
		const cartItem = {
			id: productId,
		        name: productName,
		        price: productPrice,
		        quantity: 1,
		};
		cartItems.push(cartItem);
	}
	renderCart();
}
function increaseQuantity(productId) {
	    const existingCartItem = cartItems.find(item => item.id === productId);

	    if (existingCartItem) {
		            existingCartItem.quantity += 1;
		            renderCart();
		        }
}

function decreaseQuantity(productId) {
	    const existingCartItem = cartItems.find(item => item.id === productId);

	    if (existingCartItem && existingCartItem.quantity > 1) {
		            existingCartItem.quantity -= 1;
		            renderCart();
		        }
}
renderCart();
