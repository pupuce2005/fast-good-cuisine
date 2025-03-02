document.addEventListener("DOMContentLoaded", function () {
    const selectAllCheckbox = document.getElementById("select-all");
    const checkboxes = document.querySelectorAll(".ingredient-checkbox");

    // Quand on coche/décoche la case "Tout cocher"
    selectAllCheckbox.addEventListener("change", function () {
        checkboxes.forEach(checkbox => {
            checkbox.checked = selectAllCheckbox.checked;
        });
    });

    // Si on coche/décoche une case, vérifier si toutes sont cochées ou non
    checkboxes.forEach(checkbox => {
        checkbox.addEventListener("change", function () {
            selectAllCheckbox.checked = [...checkboxes].every(cb => cb.checked);
        });
    });
});