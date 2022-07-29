let add_button = document.getElementById("add-to-basket-button")

for ( i = 0; i < updateButton.length, i++) {
  updateButton[i].addEventListener('click', function(){
    var productId = this.dataset.productId
    var action = this.dataset.action
    console.log('productId:', productId, 'Action', action)
  })
}

// add_button.addEventListener("click", amendBasket);

// function amendBasket() {
//   alert ("Hello World!");
// }
