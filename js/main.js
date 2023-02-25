// Anuncios textos
let indexTextoLateral = 0;
let indexTextoInferior = 2;


setInterval(() => {
    // Anuncio lateral
    if (anuncios[indexTextoLateral]) {
        document.getElementById("textoLateral").innerHTML = anuncios[indexTextoLateral];
    }
    else {
        indexTextoLateral = 0;
        document.getElementById("textoLateral").innerHTML = anuncios[0];
    }
    indexTextoLateral = indexTextoLateral + 1;
}, 10043);

setInterval(() => {
    // Anuncio inferior
    if (anuncios[indexTextoInferior]) {
        document.getElementById("textoInferior").innerHTML = anuncios[indexTextoInferior];
    }
    else {
        indexTextoInferior = 0;
        document.getElementById("textoInferior").innerHTML = anuncios[0];
    }
    indexTextoInferior = indexTextoInferior + 1;
}, 13200)

let indexImage=1;

function getRandomInt(max) {
    return Math.floor(Math.random() * max);
}

// Anuncio multimedia
setInterval(() => {
    var img = new Image();
    img.src = `img/anuncios/${indexImage}.jpg`;

    img.onerror = function(){ // Failed to load
        indexImage = 0;
        document.getElementById("anuncioMultimedia").src = `img/anuncios/0.jpg?r=${getRandomInt(13243)}`;
    };
    img.onload = function(){ // Loaded successfully
    };
    document.getElementById("anuncioMultimedia").src = `img/anuncios/${indexImage}.jpg?r=${getRandomInt(13243)}`;
    indexImage = indexImage + 1;
}, 15000);

// Reloj
const meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
function currentTime() {
    let date = new Date();

    let day = date.getDate();
    let month = date.getMonth();
    let year = date.getFullYear();
    let hh = date.getHours();
    let mm = date.getMinutes();
    let ss = date.getSeconds();
    let session = "AM";

    if( hh === 0){
        hh = 12;
    }
    if (hh > 12){
        hh = hh - 12;
        session = "PM";
    }

    hh = (hh < 10) ? "0" + hh : hh;
    mm = (mm < 10) ? "0" + mm : mm;
    ss = (ss < 10) ? "0" + ss : ss;
        
    let time = `${day}/${meses[month]}/${year}\n${hh}:${mm}:${ss} ${session}`;

    let relojHTML = document.getElementById("reloj");

    if (relojHTML) reloj.innerText = time;

    let t = setTimeout(function(){ currentTime() }, 1000);
}

currentTime();
