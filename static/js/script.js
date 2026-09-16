$(document).ready(function() {
  // Bind click event for expandable boxes.
  $('.box-header').on('click', function() {
    $(this).next('.box-content').slideToggle();
  });
});

// Function called when an OK button is clicked.
function submitForm(functionCall, button) {
  var commandBox = $(button).closest('.command-box');
  var valuesList = [];

  // This will grab inputs *and* selects
  commandBox.find('input, select').each(function() {
    var $el = $(this);

    // text inputs:
    if ($el.is('input[type="text"]')) {
      valuesList.push( $el.val() );

    // checked radios:
    } else if ($el.is('input[type="radio"]:checked')) {
      valuesList.push( $el.val() );

    // any <select>:
    } else if ($el.is('select')) {
      valuesList.push( $el.val() );
    }
  });

  // Prepare the payload with the function call string and the list of input values.
  var payload = {
    functionCall: functionCall,
    data: valuesList
  };

  // Send the payload to the Flask backend via AJAX.
  $.ajax({
    url: '/submit',
    method: 'POST',
    contentType: 'application/json',
    data: JSON.stringify(payload),
    success: function(response) {
      console.log('python returned: ', response);
      // Display the result in a simple message box (alert)
      alert(response.result);
    },
    error: function(err) {
      console.error('Submission failed. This is the error returned :', err);
    }
  });
}
