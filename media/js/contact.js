  $(function() {
    $('.error').hide();
    $(".button").click(function() {
      // validate and process form here
      
      $('.error').hide();
  	  var name = $("input#id_name").val();
  		if (name == "") {
        $("label#id_name_error").show();
        $("input#id_name").focus();
        return false;
      }
  		var email = $("input#id_email").val();
  		if (email == "") {
        $("label#id_email_error").show();
        $("input#id_email").focus();
        return false;
      }
  		var message = $("input#id_message").val();
  		if (phone == "") {
        $("label#id_message_error").show();
        $("input#id_message").focus();
        return false;
      }
      
      var dataString = 'id_name='+ name + '&id_email=' + email + '&id_message=' + message;
      //alert (dataString);return false;
      $.ajax({
        type: "POST",
        url: "/process_contact_form",
        data: dataString,
        success: function() {
          $('#contact_form').html("<div id='message'></div>");
          $('#message').html("<h2>Contact Form Submitted!</h2>")
          .append("<p>Thanks... I'll try to respond as soon as I can!.</p>")
          .hide()
          //.fadeIn(1500, function() {
          //  $('#message').append("<img id='checkmark' src='images/check.png' />");
          //});
        }
      });
      return false;
    });
  });
