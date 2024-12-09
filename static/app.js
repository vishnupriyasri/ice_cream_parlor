const BASE_URL = 'http://127.0.0.1:5000';

document.getElementById('user-form').addEventListener('submit', function (e) {
    e.preventDefault();
    let userName = document.getElementById('user-name').value;
    let userEmail = document.getElementById('user-email').value;
    
    fetch(`${BASE_URL}/add_user`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            name: userName,
            email: userEmail
        })
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message || data.error);
    })
    .catch(error => {
        console.error('Error:', error);
    });
});

function getFlavors() {
    fetch(`${BASE_URL}/get_flavors`)
        .then(response => response.json())
        .then(flavors => {
            const flavorsList = document.getElementById('flavors-list');
            flavorsList.innerHTML = '';
            flavors.forEach(flavor => {
                let flavorElement = document.createElement('div');
                flavorElement.innerHTML = `${flavor.name} - ${flavor.description}`;
                flavorsList.appendChild(flavorElement);
            });
        })
        .catch(error => console.error('Error fetching flavors:', error));
}

function addToCart() {
    let userId = document.getElementById('user-id').value;
    let flavorId = document.getElementById('flavor-id').value;
    
    fetch(`${BASE_URL}/add_to_cart`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            user_id: userId,
            flavor_id: flavorId
        })
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
    })
    .catch(error => console.error('Error:', error));
}

function viewCart() {
    let userId = document.getElementById('user-id').value;
    
    fetch(`${BASE_URL}/get_cart?user_id=${userId}`)
        .then(response => response.json())
        .then(cartItems => {
            const cartItemsList = document.getElementById('cart-items');
            cartItemsList.innerHTML = '';
            cartItems.forEach(item => {
                let cartItemElement = document.createElement('li');
                cartItemElement.innerHTML = item.flavor_name;
                cartItemsList.appendChild(cartItemElement);
            });
        })
        .catch(error => console.error('Error fetching cart items:', error));
}

function addSuggestion() {
    let userId = document.getElementById('user-id').value;
    let suggestion = document.getElementById('suggestion-text').value;
    
    fetch(`${BASE_URL}/add_suggestion`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            user_id: userId,
            suggestion: suggestion
        })
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
    })
    .catch(error => console.error('Error:', error));
}

getFlavors();
