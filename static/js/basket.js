 let add_button = document.getElementsByClassName("add-to-basket-button")

for (i = 0; i < add_button.length; i++) {
  add_button[i].addEventListener("click", function(){
    let itemId = this.dataset.product
    let addItem = this.dataset.action

    console.log('Item Id:', itemId, 'Action:', addItem)

    if (user == 'AnonymousUser'){
      console.log('You are not logged in')
    } else {
      updateBasketItems(itemId, addItem)
    }
});
}

// function creates a promise, sending javascript data to the backend
function updateBasketItems(itemId, addItem){
  console.log('User is authenticated, adding to basket...')

  let url = '/update-basket/'

  fetch(url, {
    method:'POST',
    headers:{
      'Content-Type':'application/json',
      'X-CSRFToken': csrftoken,
    },
    body:JSON.stringify({'itemId': itemId, 'action': addItem})
  })
  .then((response) => {
    return response.json();
  })
  .then((data) => {
    location.reload()
  });
}
