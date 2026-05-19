document.addEventListener('DOMContentLoaded', function () {

  function bindRange(minId, maxId, minValId, maxValId, unit) {
    const minInput = document.getElementById(minId);
    const maxInput = document.getElementById(maxId);
    const minSpan  = document.getElementById(minValId);
    const maxSpan  = document.getElementById(maxValId);

    if (!minInput || !maxInput) return;

    function update() {
      if (+minInput.value > +maxInput.value) minInput.value = maxInput.value;
      minSpan.textContent = minInput.value + ' ' + unit;
      maxSpan.textContent = maxInput.value + ' ' + unit;
    }

    minInput.addEventListener('input', update);
    maxInput.addEventListener('input', update);
  }

  bindRange('calMin', 'calMax', 'calMinValue', 'calMaxValue', 'kcal');
  bindRange('proMin', 'proMax', 'proMinValue', 'proMaxValue', 'g');

});
