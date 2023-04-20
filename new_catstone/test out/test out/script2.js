new Vue({
    el: "#app",
    data: {
      products: [
        {
          image: "https://via.placeholder.com/200x150",
          name: "PRODUCT ITEM NUMBER 1",
          description: "Description for product item number 1",
          price: 5.99,
          quantity: 2
        },
        {
          image: "https://via.placeholder.com/200x150",
          name: "PRODUCT ITEM NUMBER 2",
          description: "Description for product item number 1",
          price: 9.99,
          quantity: 1
        }
      ],
      tax: 5,
      promotions: [
        {
          code: "SUMMER",
          discount: "50%"
        },
        {
          code: "AUTUMN",
          discount: "40%"
        },
        {
          code: "WINTER",
          discount: "30%"
        }
      ],
      promoCode: "",
      discount: 0
    },
    computed: {
      itemCount: function() {
        var count = 0;
  
        for (var i = 0; i < this.products.length; i++) {
          count += parseInt(this.products[i].quantity) || 0;
        }
  
        return count;
      },
      subTotal: function() {
        var subTotal = 0;
  
        for (var i = 0; i < this.products.length; i++) {
          subTotal += this.products[i].quantity * this.products[i].price;
        }
  
        return subTotal;
      },
      discountPrice: function() {
        return this.subTotal * this.discount / 100;
      },
      totalPrice: function() {
        return this.subTotal - this.discountPrice + this.tax;
      }
    },
    filters: {
      currencyFormatted: function(value) {
        return Number(value).toLocaleString("en-US", {
          style: "currency",
          currency: "USD"
        });
      }
    },
    methods: {
      updateQuantity: function(index, event) {
        var product = this.products[index];
        var value = event.target.value;
        var valueInt = parseInt(value);
  
        // Minimum quantity is 1, maximum quantity is 100, can left blank to input easily
        if (value === "") {
          product.quantity = value;
        } else if (valueInt > 0 && valueInt < 100) {
          product.quantity = valueInt;
        }
  
        this.$set(this.products, index, product);
      },
      checkQuantity: function(index, event) {
        // Update quantity to 1 if it is empty
        if (event.target.value === "") {
          var product = this.products[index];
          product.quantity = 1;
          this.$set(this.products, index, product);
        }
      },
      removeItem: function(index) {
        this.products.splice(index, 1);
      },
      checkPromoCode: function() {
        for (var i = 0; i < this.promotions.length; i++) {
          if (this.promoCode === this.promotions[i].code) {
            this.discount = parseFloat(
              this.promotions[i].discount.replace("%", "")
            );
            return;
          }
        }
  
        alert("Sorry, the Promotional code you entered is not valid!");
      }
    }
  });
  