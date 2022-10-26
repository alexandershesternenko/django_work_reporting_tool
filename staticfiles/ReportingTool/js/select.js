let selItems = JSON.parse(sessionStorage.getItem("SelItem")) || [];

$(function() {
  if (selItems) {
    selItems.forEach(obj => {
      const [k, v] = Object.entries(obj)[0]
      $("#" + k).val(v)
    })
  }
  $('.myselect').on("change", function() {
    selItems = $('.myselect').map(function() {
      return { [this.id]: this.value }
    }).get();
      sessionStorage.setItem("SelItem", JSON.stringify(selItems))
    
  });
});
