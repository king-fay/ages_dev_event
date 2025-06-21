async function chargerProduits() {
    
    const categorie = document.getElementById("cat_num").innerText;
    const response = await fetch(`/produits?categorie=${encodeURIComponent(categorie)}`);
    var produits = await response.json();
    
    let contenu = "";
    produits.forEach(produit => {
        contenu += `<a href="#" onclick="ouvrirReservation('${produit[0]}','${produit[2]}')">
            <div class="m-4 p-4 bg-white rounded-lg shadow-lg cursor-pointer w-64" onclick="ouvrirReservation('${produit[0]}','${produit[2]}')">
                <img src="static/images/${produit[2]}" class="rounded-lg object-cover h-40 w-full" alt="${produit[0]}">
                    <h3 class="text-lg font-bold mt-2">${produit[0]}</h3>
                    <p class="text-sm text-gray-500">${produit[1]}</p>
             </div>
             </a>`
        });
        document.getElementById("productList").innerHTML = contenu;
    }

chargerProduits();

    function ouvrirReservation(nom, noms) {
        document.getElementById("selectedProduct").innerText = nom;
        document.getElementById("images").innerText = noms;
        document.getElementById("reservationModal").classList.remove("hidden");
        
    }

    function fermer() {
        document.getElementById("reservationModal").classList.add("hidden");
    };

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


function envoyer() {
      // 1. Récupérer les valeurs des inputs
      let images = document.getElementById("images").innerText;
      let noms = document.getElementById("selectedProduct").innerText;
      const nom = document.getElementById("nom").value;
      const email = document.getElementById("email").value;
      const numero = document.getElementById("numero").value;
      const indicatif = document.getElementById("indicatif").value;
        
      // 2. Envoyer à Flask avec fetch()
      fetch('/envoyer', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            noms : noms,
          nom: nom,
          email: email,
          indicatif: indicatif,
          numero: numero,
          images: images,
        })
      })
      .then(response => response.json())
      .then(data => {
        console.log(data)
      })
      .catch(error => console.error("Erreur :", error));

      fermer();
    };