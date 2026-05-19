document.addEventListener('shown.bs.collapse', function () {
  initRanges();
});

function initRanges() {
  const calMin    = document.getElementById('calMin');
  const calMax    = document.getElementById('calMax');
  const calMinVal = document.getElementById('calMinValue');
  const calMaxVal = document.getElementById('calMaxValue');
  const proMin    = document.getElementById('proMin');
  const proMax    = document.getElementById('proMax');
  const proMinVal = document.getElementById('proMinValue');
  const proMaxVal = document.getElementById('proMaxValue');

  function updateCal() {
    if (+calMin.value > +calMax.value) calMin.value = calMax.value;
    calMinVal.textContent = calMin.value + ' kcal';
    calMaxVal.textContent = calMax.value + ' kcal';
  }
  function updatePro() {
    if (+proMin.value > +proMax.value) proMin.value = proMax.value;
    proMinVal.textContent = proMin.value + ' g';
    proMaxVal.textContent = proMax.value + ' g';
  }

  calMin.addEventListener('input', updateCal);
  calMax.addEventListener('input', updateCal);
  proMin.addEventListener('input', updatePro);
  proMax.addEventListener('input', updatePro);
}

