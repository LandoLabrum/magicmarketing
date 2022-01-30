jQuery(function ($) {
  var $bodyEl = $('body'),
    $sidedrawerEl = $('#sidedrawer');


  function showSidedrawer() {
    // show overlay
    var options = {
      onclose: function () {
        $sidedrawerEl
          .removeClass('active')
          .appendTo(document.body);
      }
    };

    var $overlayEl = $(mui.overlay('on', options));

    // show element
    $sidedrawerEl.appendTo($overlayEl);
    setTimeout(function () {
      $sidedrawerEl.addClass('active');
    }, 20);
  }


  function hideSidedrawer() {
    $bodyEl.toggleClass('hide-sidedrawer');
  }


  $('.js-show-sidedrawer').on('click', showSidedrawer);
  $('.js-hide-sidedrawer').on('click', hideSidedrawer);
  var $titleEls = $('strong', $sidedrawerEl);

  $titleEls
    .next()
    .hide();

  $titleEls.on('click', function () {
    $(this).next().slideToggle(200);
  });

  $('.remove').on('click', function () {
    $(this).closest(".mui-panel").fadeOut(1000);
});
});

document.addEventListener('DOMContentLoaded', function () {

  $('.err').hide();
  const isNumericInput = (event) => {
      const key = event.keyCode;
      return ((key >= 48 && key <= 57) || // Allow number line
          (key >= 96 && key <= 105) // Allow number pad
      );
  };

  const isModifierKey = (event) => {
      const key = event.keyCode;
      return (event.shiftKey === true || key === 35 || key === 36) || // Allow Shift, Home, End
          (key === 8 || key === 9 || key === 13 || key === 46) || // Allow Backspace, Tab, Enter, Delete
          (key > 36 && key < 41) || // Allow left, up, right, down
          (
              // Allow Ctrl/Command + A,C,V,X,Z
              (event.ctrlKey === true || event.metaKey === true) &&
              (key === 65 || key === 67 || key === 86 || key === 88 || key === 90)
          )
  };

  const enforceFormat = (event) => {
      // Input must be of a valid number format or a modifier key, and not longer than ten digits
      if (!isNumericInput(event) && !isModifierKey(event)) {
          event.preventDefault();
      }
  };

  const formatToPhone = (event) => {
      if (isModifierKey(event)) { return; }

      const input = event.target.value.replace(/\D/g, '').substring(0, 10); // First ten digits of input only
      const areaCode = input.substring(0, 3);
      const middle = input.substring(3, 6);
      const last = input.substring(6, 10);

      if (input.length > 6) { event.target.value = `(${areaCode}) ${middle} - ${last}`; }
      else if (input.length > 3) { event.target.value = `(${areaCode}) ${middle}`; }
      else if (input.length > 0) { event.target.value = `(${areaCode}`; }
  };

  const inputElement = document.getElementById('phoneNumber');
  if (inputElement !== null) {
      inputElement.addEventListener('keyup', formatToPhone);
      inputElement.addEventListener('keydown', enforceFormat);
  }
});