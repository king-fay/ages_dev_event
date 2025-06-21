async function chargerProduits() {
    const categorie = document.getElementById("categorie").innerText;
    const response = await fetch("/produits?categorie=${categorie}");
    const produits = await response.json();

    let contenu = "";
    produits.forEach(produit => {
        contenu += `
            <div class="m-4 p-4 bg-white rounded-lg shadow-lg cursor-pointer w-64" onclick="ouvrirReservation('${produit.nom}')">
                <img src="static/images/${produit[2]}" class="rounded-lg object-cover h-40 w-full" alt="${produit.nom}">
                    <h3 class="text-lg font-bold mt-2">${produit[0]}</h3>
                    <p class="text-sm text-gray-500">${produit[1]}</p>
             </div>
             `;
        });

        document.getElementById("productList").innerHTML = contenu;
    }

    function ouvrirReservation(nom) {
        document.getElementById("selectedProduct").innerText = nom;
        document.getElementById("reservationModal").classList.remove("hidden");
    }

    document.getElementById("closeModal").addEventListener("click", () => {
        document.getElementById("reservationModal").classList.add("hidden");
    });

chargerProduits();

document.getElementById("indicatif").addEventListener("change", () => {
    const indicatif = document.getElementById("indicatif").value;
    document.getElementById("numero").value = indicatif + " ";
});

document.getElementById("numero").addEventListener("input", () => {
    const regex = /^[0-9\s]*$/;
    const champ = document.getElementById("numero");

    if (!regex.test(champ.value)) {
        champ.classList.add("border-red-500");
    } else {
        champ.classList.remove("border-red-500");
    }
});


