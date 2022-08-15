let add_button = document.getElementsByClassName("add-to-basket-button")

for (i = 0; i < add_button.length; i++) {
  add_button[i].addEventListener("click", function(){
    let itemId = this.dataset.product
    let addItem = this.dataset.action

    console.log('item Id:', itemId, 'Action:', addItem)

    if (user == 'AnonymousUser'){
      console.log('You are not logged in')
    } else {
      console.log('You are logged in as', user)
    }
    
});
}