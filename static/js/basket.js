let add_button = document.getElementsByClassName("add-to-basket-button")

for (i = 0; i < add_button.length; i++) {
  add_button[i].addEventListener("click", function(){
    let item_id = this.dataset.product
    let add_item = this.dataset.action
    alert(item_id)
});
}