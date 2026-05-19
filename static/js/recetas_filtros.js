document.addEventListener("DOMContentLoaded", () => {
  const dropdown = document.getElementById("dropdownList");
  const wrapper  = document.getElementById("alergiasDropdown");
  const alergiasText = document.getElementById("alergiasText");

  // Si no existen los elementos en esta página, salir sin errores
  if (!dropdown || !wrapper || !alergiasText) {
    // No es un fallo crítico: puede que este script se cargue en páginas sin el dropdown
    return;
  }

  // Toggle del dropdown (usa type="button" en el HTML si está dentro de un form)
  function toggleDropdown() {
    dropdown.style.display = dropdown.style.display === "block" ? "none" : "block";
  }

  // Actualiza el texto con las opciones seleccionadas
  function updateSelected() {
    const checkboxes = dropdown.querySelectorAll('input[type="checkbox"]');
    const selected = [];
    checkboxes.forEach(cb => {
      if (cb.checked) selected.push(cb.value);
    });
    alergiasText.innerText = selected.length ? selected.join(", ") : "Alergias";
  }

  // Abrir/cerrar al pulsar el contenedor principal
  wrapper.addEventListener("click", (e) => {
    // Evitar que el click en el dropdown burbujee y cierre inmediatamente
    e.stopPropagation();
    toggleDropdown();
  });

  // Si el usuario hace click dentro del dropdown, no cerrarlo (por ejemplo al marcar checkboxes)
  dropdown.addEventListener("click", (e) => {
    e.stopPropagation();
  });

  // Escuchar cambios en los checkboxes (delegación)
  dropdown.addEventListener("change", (e) => {
    if (e.target && e.target.matches('input[type="checkbox"]')) {
      updateSelected();
    }
  });

  // Click global: si se hace click fuera del wrapper, cerrar el dropdown
  document.addEventListener("click", () => {
    dropdown.style.display = "none";
  });

  // Inicializar texto (por si hay checks preseleccionados)
  updateSelected();
});