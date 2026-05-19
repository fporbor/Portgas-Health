document.addEventListener('DOMContentLoaded', function () {

  const TRACK_BG   = '#2a2a33';
  const TRACK_FILL = '#ff5c1a';

  function applyFill(slider) {
    const pct = ((+slider.value - +slider.min) / (+slider.max - +slider.min)) * 100;
    // Seteamos el background directamente sobre el input — funciona en todos los navegadores
    slider.style.background =
      `linear-gradient(to right, ${TRACK_FILL} 0%, ${TRACK_FILL} ${pct}%, ${TRACK_BG} ${pct}%, ${TRACK_BG} 100%)`;
  }

  function bindRange(minId, maxId, minValId, maxValId, unit) {
    const minInput = document.getElementById(minId);
    const maxInput = document.getElementById(maxId);
    const minSpan  = document.getElementById(minValId);
    const maxSpan  = document.getElementById(maxValId);

    if (!minInput || !maxInput) return;

    function update() {
      if (+minInput.value > +maxInput.value) minInput.value = maxInput.value;
      minSpan.textContent = minInput.value + '\u00a0' + unit;
      maxSpan.textContent = maxInput.value + '\u00a0' + unit;
      applyFill(minInput);
      applyFill(maxInput);
    }

    applyFill(minInput);
    applyFill(maxInput);
    update();

    minInput.addEventListener('input', update);
    maxInput.addEventListener('input', update);
  }

  bindRange('calMin', 'calMax', 'calMinValue', 'calMaxValue', 'kcal');
  bindRange('proMin', 'proMax', 'proMinValue', 'proMaxValue', 'g');
});