document.addEventListener('DOMContentLoaded', function() {
    let elems;

    elems = document.querySelectorAll('select');
    let selectInstances = M.FormSelect.init(elems, {});

    elems = document.querySelectorAll('.datepicker');
    let datepickerInstances = M.Datepicker.init(elems, {
        showClearBtn: true
    });
  });
