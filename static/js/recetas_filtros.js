function toggleDropdown() {
    const dropdown = document.getElementById("dropdownList");
    dropdown.style.display = dropdown.style.display === "block" ? "none" : "block";
}

function updateSelected() {
    const checkboxes = document.querySelectorAll('#dropdownList input[type="checkbox"]');
    const selected = [];

    checkboxes.forEach(cb => {
        if (cb.checked) selected.push(cb.value);
    });

    document.getElementById("alergiasText").innerText =
        selected.length ? selected.join(", ") : "Alergias";
}

document.addEventListener("click", function(e) {
    const box = document.getElementById("alergiasDropdown");
    if (!box.contains(e.target)) {
        document.getElementById("dropdownList").style.display = "none";
    }
});

