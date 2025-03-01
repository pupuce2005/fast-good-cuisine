// Récupérer l'élément modal, l'input et le bouton de fermeture
var modal = document.getElementById("modal");
var input = document.getElementById("nameInput");
var span = document.getElementsByClassName("close")[0];



// Ouvrir le modal quand l'input est cliqué
input.onclick = function () {
    modal.style.display = "block";
}

// Fermer le modal lorsque l'utilisateur clique sur le bouton de fermeture
span.onclick = function () {
    modal.style.display = "none";
}

// Fermer le modal si l'utilisateur clique en dehors du contenu du modal
window.onclick = function (event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

// Fonction pour sélectionner un ingrédient dans la liste
function selectIngredient(element, ingredientName) {
    // Mettre à jour l'input avec le nom de l'ingrédient sélectionné
    input.value = ingredientName;

    // Fermer le modal après sélection
    modal.style.display = "none";

    // Optionnel : Mettre en évidence l'élément sélectionné
    var allItems = document.querySelectorAll('li');
    allItems.forEach(item => item.classList.remove('selected'));
    element.classList.add('selected');
}