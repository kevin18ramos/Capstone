'use strict';

// all iniial elments
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

    // plus inc variable value by 1
    increment++;

    // show the inc varble value on quanty element
    // on clicked inc button sibling.
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



const totalCalc = function () {


  const tax = 0.05;
  let subtotal = 0;
  let totalTax = 0;
  let total = 0;

  
  for (let i = 0; i < quantityElem.length; i++) {

    subtotal += Number(quantityElem[i].textContent) * Number(priceElem[i].textContent);

  }


  subtotalElem.textContent = subtotal.toFixed(2);


  totalTax = subtotal * tax;


  taxElem.textContent = totalTax.toFixed(2);

  
  total = subtotal + totalTax;

  totalElem.textContent = total.toFixed(2);
  payAmountBtn.textContent = total.toFixed(2);

}