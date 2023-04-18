 $( document ).ready(function() {
   
    //get data from json object
    $.getJSON(
  
      "https://codepen.io/aiadev/pen/aQoeyd.js",
      function(data) {
  
        //assign values
        $('#firstName').val(data.firstName);
        $('#lastName').val(data.lastName);
        $('#company').val(data.company);
        $('#street').val(data.address.streetAddress);
        $('#city').val(data.address.city);
        $('#state').val(data.address.state);
        $('#zipCode').val(data.address.postalCode);
        $('#homeNumber').val(data.phoneNumber[0].number);
        $('#faxNumber').val(data.phoneNumber[1].number);
        
        //loop to go through comments
        for (var key in data.Comments) {
          $('#form__comments-by').append('<label for="commentBy'+ key +'">Comment By</label><input name="commentBy'+ key +'" type="text" class="form-control" id="commentBy'+ key +'" value="'+data.Comments[key]["Comment By"]+'">');
          $('#form__comments-txt').append('<label for="comment'+ key +'">Comment</label><textarea name="comment'+ key +'" type="text" class="form-control" id="comment'+ key +'">'+data.Comments[key].Comment+'</textarea>');
        }
        
      }
    );
    
    //asign button actions
    $("#cancel").click(function() {
      alert("Edit Canceled");
    });
    
    $("#save").click(function() {
      alert("Record Updated");
    });
    
    //generate date for footer
    var currentYear = (new Date()).getFullYear();
    $('#currentYear').append(currentYear);
  
  });
  (document).ready(function() {
    //   $('#list').click(function(event){event.preventDefault();$('#products .item').addClass('list-group-item');});
    //   $('#grid').click(function(event){event.preventDefault();$('#products .item').removeClass('list-group-item');$('#products .item').addClass('grid-group-item');});
    // });// VARIABLES
    const rangeInput = document.querySelector('input[type = "range"]');
    const imageList = document.querySelector(".image-list");
    const searchInput = document.querySelector('input[type="search"]');
    const btns = document.querySelectorAll(".view-options button");
    const photosCounter = document.querySelector(".toolbar .counter span");
    const imageListItems = document.querySelectorAll(".image-list li");
    const captions = document.querySelectorAll(".image-list figcaption p:first-child");
    const myArray = [];
    let counter = 1;
    const active = "active";
    const listView = "list-view";
    const gridView = "grid-view";
    const dNone = "d-none";
    // SET VIEW
    for (const btn of btns) {
      btn.addEventListener("click", function() {
        const parent = this.parentElement;
        document.querySelector(".view-options .active").classList.remove(active);
        parent.classList.add(active);
        this.disabled = true;
        document.querySelector('.view-options [class^="show-"]:not(.active) button').disabled = false;
        if (parent.classList.contains("show-list")) {
          parent.previousElementSibling.previousElementSibling.classList.add(dNone);
          imageList.classList.remove(gridView);
          imageList.classList.add(listView);
        } else {
          parent.previousElementSibling.classList.remove(dNone);
          imageList.classList.remove(listView);
          imageList.classList.add(gridView);
        }
      });
    }
    // SET THUMBNAIL VIEW - CHANGE CSS VARIABLE
    rangeInput.addEventListener("input", function() {
      document.documentElement.style.setProperty("--minRangeValue",`${this.value}px`);
    });
    // SEARCH FUNCTIONALITY
    for (const caption of captions) {
      myArray.push({
        id: counter++,
        text: caption.textContent
      });
    }
    searchInput.addEventListener("keyup", keyupHandler);
    function keyupHandler() {
      for (const item of imageListItems) {
        item.classList.add(dNone);
      }
      const text = this.value;
      const filteredArray = myArray.filter(el => el.text.includes(text));
      if (filteredArray.length > 0) {
        for (const el of filteredArray) {
          document.querySelector(`.image-list li:nth-child(${el.id})`).classList.remove(dNone);
        }
      }
      photosCounter.textContent = filteredArray.length;
    }


    Java script:'use strict';
// all initial elements
const payAmountBtn = document.querySelector('#payAmount');
const decrementBtn = document.querySelectorAll('#decrement');
const quantityElem = document.querySelectorAll('#quantity');
const incrementBtn = document.querySelectorAll('#increment');
const priceElem = document.querySelectorAll('#price');
const subtotalElem = document.querySelector('#subtotal');
const taxElem = document.querySelector('#tax');
const totalElem = document.querySelector('#total');
for (let i = 0; i < incrementBtn.length; i++) {
  incrementBtn[i].addEventListener('click', function () {
    let increment = Number(this.previousElementSibling.textContent);
    // plus `increment` variable value by 1
    increment++;
    // show the `increment` variable value on `quantity` element
    // based on clicked `increment` button sibling.
    this.previousElementSibling.textContent = increment;
    totalCalc();
  });
  decrementBtn[i].addEventListener('click', function () {
    let decrement = Number(this.nextElementSibling.textContent);
    decrement <= 1 ? 1 : decrement--;
    this.nextElementSibling.textContent = decrement;
    totalCalc();
  });
}
// function: for calculating total amount of product price
const totalCalc = function () {
  // declare all initial variable
  const tax = 0.05;
  let subtotal = 0;
  let totalTax = 0;
  let total = 0;
  // loop: for calculating `subtotal` value from every single product
  for (let i = 0; i < quantityElem.length; i++) {
    subtotal += Number(quantityElem[i].textContent) * Number(priceElem[i].textContent);
  }
  // show the `subtotal` variable value on `subtotalElem` element
  subtotalElem.textContent = subtotal.toFixed(2);
  // calculating the `totalTax`
  totalTax = subtotal * tax;
  // show the `totalTax` on `taxElem` element
  taxElem.textContent = totalTax.toFixed(2);
  // calcualting the `total`
  total = subtotal + totalTax;
  // show the `total` variable value on `totalElem` & `payAmountBtn` element
  totalElem.textContent = total.toFixed(2);
  payAmountBtn.textContent = total.toFixed(2);
}