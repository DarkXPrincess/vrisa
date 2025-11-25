//TRANSITIONS 1--------------------------------------------------------------------------
function iniciarAnimacionMensajes(mensajes, elementoId, intervalo = 4000) {
  let mensajesPendientes = [...mensajes];
  const mensajeDiv = document.getElementById(elementoId);

  function mostrarMensajeAleatorio() {
    if (mensajesPendientes.length === 0) {
      mensajesPendientes = [...mensajes];
    }

    const indice = Math.floor(Math.random() * mensajesPendientes.length);
    const mensaje = mensajesPendientes[indice];
    mensajesPendientes.splice(indice, 1);

    mensajeDiv.classList.add("oculto");

    setTimeout(() => {
      mensajeDiv.textContent = mensaje;
      mensajeDiv.classList.remove("oculto");
    }, 700);

    setTimeout(mostrarMensajeAleatorio, intervalo);
  }

  mostrarMensajeAleatorio();
}

// FRAME WELCOME MODAL
iniciarAnimacionMensajes(
  [
    "Welcome to Blueprint HUBs",

    "Start building with us",

    "Innovation begins here",

    "Let’s build smart",

    "Efficiency meets design",

    "Your blueprint, our mission",

    "Glad to have you here!",

    "Quality starts now",

    "Welcome to precision",

    "Together, we build better",
  ],
  "mensajewelcomemodal"
);

// FRAME PROJECTS MODAL
iniciarAnimacionMensajes(
  [
    "Our projects are built on precision",

    "Innovation guides every project we create",

    "We deliver plans tailored to every regulation",

    "Each project reflects our commitment to quality",

    "Efficiency powers our project workflow",

    "Our projects connect teams through smart collaboration",

    "Blueprint HUBs turns ideas into execution-ready plans",

    "Every project, expertly managed and digitally tracked",

    "We craft solutions, not just plans",

    "Our projects are made to build the future",
  ],
  "mensajeprojectsmodal"
);

// FRAME SERVICE MODAL
iniciarAnimacionMensajes(
  [
    "Service designed for results",

    "Reliable service. Consistent delivery",

    "We simplify service through automation",

    "Service backed by precision and expertise",

    "Efficiency is at the core of our service",

    "Service that adapts to your needs",

    "Built-in support for every step",

    "More than service — it’s a partnership",

    "Digital service. Human commitment",

    "Our service keeps your project moving",
  ],
  "mensajeservicesmodal"
);

// FRAME CONTACT MODAL
iniciarAnimacionMensajes(
  [
    "LET’S TALK!",

    "Stay connected, stay informed",

    "Your contact, our commitment",

    "Direct lines to real support",

    "Communication made easy",

    "One message away from progress",

    "We’re always within reach",

    "Let’s build through connection",

    "Clear contacts. Seamless collaboration",

    "Reach out. We’re here to help",

    "Every contact matters",
  ],
  "mensajecontactmodal"
);

// FRAME COMMENT MODAL
iniciarAnimacionMensajes(
  [
    "Do you have comments or suggestions?",

    "Your feedback helps us grow",

    "Got ideas? We’re listening",

    "Help us improve — share your thoughts!",

    "Tell us what you think!",

    "Suggestions welcome anytime",

    "We value your opinion",

    "Let’s make this better together",

    "Your voice matters to us",

    "What can we do better?",

    "Drop a comment — we read them all.",
  ],
  "mensajecommentmodal"
);

// FRAME MENU MODAL
iniciarAnimacionMensajes(
  [
    "Discover how precision and efficiency are part of our DNA.",
    "Welcome to NEWBLUEPRINT: where every plan tells a story of quality.",
    "Innovation starts here. Get inspired by our approach.",
    "We simplify complex projects from the very first plan.",
    "Explore projects that turn ideas into built realities.",
    "Our plans, your next big achievement.",
    "Every project is an opportunity to build excellence.",
    "See how we optimize time and results in every plan delivered.",
    "We automate processes so your project moves forward without limits.",
    "Discover our services designed for manufacturers, contractors, and architects.",
    "Services built to meet regulations, optimize workflows, and create impact.",
    "From drawings to digital project management—see what we can do for you.",
    "Have a project in mind? Let’s talk!",
    "We’re ready to collaborate with you. Message us today.",
    "Ready to take the next step? Get in touch with us.",
    "Personalized attention for projects that deserve extraordinary results.",
    "Your feedback helps us build better, together.",
    "Leave your comments and be part of the industry’s evolution.",
    "Your experience with NEWBLUEPRINT matters. Tell us what you think.",
    "We want to grow with your input. What’s your opinion of our service?",
  ],
  "mensajemenumodal"
);

// FRAME LOGIN MODAL
iniciarAnimacionMensajes(
  [
    "Logging you in...",
    "Authenticating your account...",
    "Checking credentials...",
    "Please wait while we log you in...",
    "Verifying your identity...",
    "Welcome back!",
    "Accessing your dashboard...",
    "Logging into your account...",
    "Security check in progress...",
    "Hang tight, logging in...",
  ],
  "mensajeloginmodal"
);



// ------------------------------- TRANSITIONS 2 ----------------------------------------------------------
// USO: <h1 id="mensaje1" class="mensaje"></h1> EN HTML
//--------------------------
//IMPORTACION DE js en html:

// <script src="FUNTIONJS/FUNTION_TRANSITION.JS"></script>
//--------------------------
//EN CSS USAMOS:
//  .cursor{
//    display: inline-block;
//    background-color: rgba(255, 255, 255, 0);
//    animation: blink 0.6 step(2,start) infinite;
//  }

//  @keyframes blink{
//    50%{
//        opacity: 0;
//      }
//   }
//--------------------------------------------------------------------------------------
function createTypingEffect(texts, elementId, typingSpeed = 100, erasingSpeed = 50, delayBetweenTexts = 1500) {
  let shuffledTexts = shuffleArray([...texts]); // copia y mezcla
  let currentTextIndex = 0;
  let charIndex = 0;
  const textElement = document.getElementById(elementId);

  function shuffleArray(array) {
    for (let i = array.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [array[i], array[j]] = [array[j], array[i]];
    }
    return array;
  }

  function typeText() {
    if (!textElement) return;

    if (charIndex < shuffledTexts[currentTextIndex].length) {
      textElement.textContent += shuffledTexts[currentTextIndex].charAt(charIndex);
      charIndex++;
      setTimeout(typeText, typingSpeed);
    } else {
      setTimeout(eraseText, delayBetweenTexts);
    }
  }

  function eraseText() {
    if (!textElement) return;

    if (charIndex > 0) {
      textElement.textContent = shuffledTexts[currentTextIndex].substring(0, charIndex - 1);
      charIndex--;
      setTimeout(eraseText, erasingSpeed);
    } else {
      currentTextIndex++;
      if (currentTextIndex >= shuffledTexts.length) {
        shuffledTexts = shuffleArray([...texts]);
        currentTextIndex = 0;
      }
      setTimeout(typeText, typingSpeed);
    }
  }

  typeText();
}


// FRAME WELCOME
createTypingEffect(
  ["Welcome to Blueprint HUBs",

    "Start building with us",

    "Innovation begins here",

    "Let’s build smart",

    "Efficiency meets design",

    "Your blueprint, our mission",

    "Glad to have you here!",

    "Quality starts now",

    "Welcome to precision",

    "Together, we build better",
  ],
  "mensajewelcomeframe"
);

// FRAME PROJECTS
createTypingEffect(
  ["Our projects are built on precision",

    "Innovation guides every project we create",

    "We deliver plans tailored to every regulation",

    "Each project reflects our commitment to quality",

    "Efficiency powers our project workflow",

    "Our projects connect teams through smart collaboration",

    "Blueprint HUBs turns ideas into execution-ready plans",

    "Every project, expertly managed and digitally tracked",

    "We craft solutions, not just plans",

    "Our projects are made to build the future",
  ],
  "mensajeprojectsframe"
);

// FRAME SERVICE
createTypingEffect(
  ["Service designed for results",

    "Reliable service. Consistent delivery",

    "We simplify service through automation",

    "Service backed by precision and expertise",

    "Efficiency is at the core of our service",

    "Service that adapts to your needs",

    "Built-in support for every step",

    "More than service — it’s a partnership",

    "Digital service. Human commitment",

    "Our service keeps your project moving",
  ],
  "mensajeserviceframe"
);

// FRAME CONTACT
createTypingEffect(
  ["LET’S TALK!",

    "Stay connected, stay informed",

    "Your contact, our commitment",

    "Direct lines to real support",

    "Communication made easy",

    "One message away from progress",

    "We’re always within reach",

    "Let’s build through connection",

    "Clear contacts. Seamless collaboration",

    "Reach out. We’re here to help",

    "Every contact matters",
  ],
  "mensajecontactframe"
);

// FRAME COMMENT
createTypingEffect(
  ["Do you have comments or suggestions?",

    "Your feedback helps us grow",

    "Got ideas? We’re listening",

    "Help us improve — share your thoughts!",

    "Tell us what you think!",

    "Suggestions welcome anytime",

    "We value your opinion",

    "Let’s make this better together",

    "Your voice matters to us",

    "What can we do better?",

    "Drop a comment — we read them all.",
  ],
  "mensajecommentframe"
);


// createTypingEffect(
//   ["¡Bienvenido!", "Explora nuevas ideas", "Desarrolla tu proyecto"],
//   "text2",
//   120,
//   60,
//   2000
// );


//FUNCION DE RUEDA PARA ACCIONAR EL CARROUSEL (NO ELIMINAR)
const carousel = document.getElementById("carouselExample");
  let scrollThrottle;

  if (carousel) {
    carousel.addEventListener("wheel", (e) => {
      e.preventDefault();
      clearTimeout(scrollThrottle);

      scrollThrottle = setTimeout(() => {
        const isScrollDown = e.deltaY > 0;
        const bsCarousel = bootstrap.Carousel.getInstance(carousel) || new bootstrap.Carousel(carousel);

        if (isScrollDown) {
          bsCarousel.next();
        } else {
          bsCarousel.prev();
        }
      }, 100);
    }, { passive: false });
  }