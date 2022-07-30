let add_button = document.getElementsByClassName("add-to-basket-button")

for (i = 0; i < add_button.length; i++) {
  add_button[i].addEventListener("click", function(){
    let item_id = this.dataset.product
    let add_item = this.dataset.action
    console.log('item_id:', item_id, 'add_item:', add_item)
});
}