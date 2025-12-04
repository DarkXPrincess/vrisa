// ------------------------------- INVOCATION IN HTML----------------------------------------------
// In the scripts in html create:  <script src="ubication / IMAGES_TRANSITION.js"></script>

// ------------------------------- USE IN CSS----------------------------------------------
// .styleicon {
//  opacity: 0;
//  transition: opacity 1.5s ease-in-out;
//  object-fit: cover;  
//  }
//-------------------------------------------------------------------------------------------
//ICON NAV IMAGE ANIMATION-----------------------

const imagenes = [
    //CARGA DE LOS LOGOS CORRESPONDIENTES:
    'ICONS/Logo_BP_cVar2.png',
    'ICONS/Logo_BP_cVar3.png',
    'ICONS/Logo_BP_cVar4.png',
    'ICONS/Logo_BP_cVar5.png',
  ];
  
  let imagenesMostradas = [];
  
  function mostrarImagen() {
    if (imagenesMostradas.length === imagenes.length) {
      imagenesMostradas = [];
    }
  
    let indiceAleatorio;
    do {
      indiceAleatorio = Math.floor(Math.random() * imagenes.length);
    } while (imagenesMostradas.includes(indiceAleatorio));
  
    imagenesMostradas.push(indiceAleatorio);
    const imagenElement = document.getElementById('styleicon');
    imagenElement.style.opacity = 0;
    setTimeout(() => {
      imagenElement.src = imagenes[indiceAleatorio];
      imagenElement.style.opacity = 1;
      // time icon faded(desvanecido) change
    }, 500);
  }
  // time duration icon change
  setInterval(mostrarImagen, 10000);
  mostrarImagen();

//ICON NAV IMAGE END ANIMATION-----------------------