const value = document.querySelector("#value");
const ratings_input = document.querySelector("#ratings");
value.textContent = ratings_input.value;
ratings_input.addEventListener("input", (event) => {
    value.textContent = event.target.value;
});


function previewFile() {
    // Récupérer l'élément input et l'élément img pour l'aperçu
    const input = document.getElementById('image');
    const preview = document.getElementById('preview-image');

    // Vérifier si un fichier a été sélectionné
    if (input.files && input.files[0]) {
        const reader = new FileReader();

        // Lorsque le fichier est lu, mettre à jour l'image affichée
        reader.onload = function (e) {
            const img = new Image();
            img.src = e.target.result;

            img.onload = function () {
                // Créer un canvas pour redimensionner l'image
                const canvas = document.createElement('canvas');
                const ctx = canvas.getContext('2d');

                // Définir la taille du carré
                const size = Math.min(img.width, img.height);
                canvas.width = size;
                canvas.height = size;

                // Dessiner l'image sur le canvas en la centrant et en la redimensionnant
                ctx.drawImage(img,
                    (img.width - size) / 2,
                    (img.height - size) / 2,
                    size, size,
                    0, 0,
                    size, size
                );

                // Mettre à jour l'attribut src de l'image avec l'image redimensionnée
                preview.src = canvas.toDataURL();
            };
        };

        // Lire le fichier en tant qu'URL de données
        reader.readAsDataURL(input.files[0]);
        submitBtn.style.display = 'block';
    }

}