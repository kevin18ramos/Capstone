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
  