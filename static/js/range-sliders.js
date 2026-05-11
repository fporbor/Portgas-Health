document.addEventListener("DOMContentLoaded", () => {
  const calMin = document.getElementById("calMin");
  const calMax = document.getElementById("calMax");
  const calMinValue = document.getElementById("calMinValue");
  const calMaxValue = document.getElementById("calMaxValue");

  const proMin = document.getElementById("proMin");
  const proMax = document.getElementById("proMax");
  const proMinValue = document.getElementById("proMinValue");
  const proMaxValue = document.getElementById("proMaxValue");

  function updateRange(minInput, maxInput, minLabel, maxLabel) {
    minInput.addEventListener("input", () => {
      if (parseInt(minInput.value) > parseInt(maxInput.value)) {
        maxInput.value = minInput.value;
      }
      minLabel.textContent = minInput.value;
      maxLabel.textContent = maxInput.value;
    });

    maxInput.addEventListener("input", () => {
      if (parseInt(maxInput.value) < parseInt(minInput.value)) {
        minInput.value = maxInput.value;
      }
      minLabel.textContent = minInput.value;
      maxLabel.textContent = maxInput.value;
    });
  }

  updateRange(calMin, calMax, calMinValue, calMaxValue);
  updateRange(proMin, proMax, proMinValue, proMaxValue);
});

