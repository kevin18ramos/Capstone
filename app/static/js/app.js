const validateEmail = function(email) {
    var formData = new FormData();
    formData.append('email', email)
    $.ajaxSetup({
        headers: {
            "X-CSRFToken": document.querySelector('[name=csrfmiddlewaretoken]').value,
        }
    });
    $.ajax({
        url: '/validate/',
        type: 'POST',
        dataType: 'json',
        cache: false,
        processData: false,
        contentType: false,
        data: formData,
        error: function (xhr) {
            console.error(xhr.statusText);
        },
        success: function (res) {
            $('.error').text(res.msg);
        }
    });
};

const subscribeUser = function(email, name) {
    var formData = new FormData();
    formData.append('email', email);
    formData.append('name', name);
    $.ajaxSetup({
        headers: {
            "X-CSRFToken": document.querySelector('[name=csrfmiddlewaretoken]').value,
        }
    });
    $.ajax({
        url: '/newsletter/',
        type: 'POST',
        dataType: 'json',
        cache: false,
        processData: false,
        contentType: false,
        data: formData,
        error: function (xhr) {
            console.error(xhr.statusText);
        },
        success: function (res) {
            $('.success').text(res.msg);
            $('#userEmail').val(' ');
            $('#userName').val(' ');
        }
    });
};

(function ($) {
    $('#submit').on('click', () => {
        event.preventDefault();
        const userEmail = $('#userEmail').val();
        const userName = $('#userName').val();
        if (userEmail && userName) {
            subscribeUser(userEmail, userName);
        }
    });

    $('#userEmail').on('change', (event) => {
        event.preventDefault();
        const email = event.target.value;
        validateEmail(email);
    });
})(jQuery);














const example_image_upload_handler = (blobInfo, progress) => new Promise((resolve, reject) => {
    const xhr = new XMLHttpRequest();
    xhr.withCredentials = false;
    xhr.open('POST', 'postAcceptor.php');
  
    xhr.upload.onprogress = (e) => {
      progress(e.loaded / e.total * 100);
    };
  
    xhr.onload = () => {
      if (xhr.status === 403) {
        reject({ message: 'HTTP Error: ' + xhr.status, remove: true });
        return;
      }
  
      if (xhr.status < 200 || xhr.status >= 300) {
        reject('HTTP Error: ' + xhr.status);
        return;
      }
  
      const json = JSON.parse(xhr.responseText);
  
      if (!json || typeof json.location != 'string') {
        reject('Invalid JSON: ' + xhr.responseText);
        return;
      }
  
      resolve(json.location);
    };
  
    xhr.onerror = () => {
      reject('Image upload failed due to a XHR Transport error. Code: ' + xhr.status);
    };
  
    const formData = new FormData();
    formData.append('file', blobInfo.blob(), blobInfo.filename());
  
    xhr.send(formData);
  });
  
  tinymce.init({
    selector: 'textarea',  // change this value according to your HTML
    images_upload_handler: example_image_upload_handler
  });