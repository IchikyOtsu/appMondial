let dataPython;
let dataDisplay;

function retrieveData(event){
    event.preventDefault()
    let userData = {};
    form = document.querySelector("form")
    userData["nom"] = form.nom.value;
    userData["tel"] = form.tel.value;
    userData["nbPers"] = form.nbPers.value;
    userData["nbPmr"] = form.nbPmr.value;
    userData["nbBb"] = form.nbBb.value;
    userData["dateHeure"] = form.dateHeure.value;
    userData["typeCuisine"] = form.tc.value;
    dataPython = userData
    console.log(dataPython)
    eel.mainGUI()
    console.log(dataDisplay)
    return userData
}

async function affichage(){
    dataDisplay = await eel.importJSON()();
    console.log(dataDisplay);
    let listReservations = dataDisplay["reservation_manager"]["reservations"];
    let tbody = ""
    listReservations.forEach(function(reservation){
        keys = Object.keys(reservation);
        let ligne = "<tr>"
        values = Object.values(reservation);
        values.forEach(function(elem){
            let td = "<td>" + elem + "</td>";
            ligne+=td;
        });
        ligne += "</tr>"
        tbody += ligne;
        document.querySelector("tbody").innerHTML = tbody;
    })
}


function init(){
    document.querySelector("form").addEventListener("submit",retrieveData);
    document.querySelector("form").addEventListener("submit",affichage);
    affichage();
}



eel.expose(exportPython)
function exportPython(){
    return dataPython;
}

let idTabActuel = "reservation";

function _gebi(id){ return document.getElementById(id)}


document.addEventListener("DOMContentLoaded", initTabs);


function initTabs() { console.log('in initTabs')
    _gebi('aff_'+idTabActuel).style.display = "block";
    _gebi(idTabActuel).classList.add("active");
}


function changerTab(tabButton) {  console.log('in changerTab ',tabButton);
    // cache le tab actuel
    _gebi('aff_'+idTabActuel).style.display = "none";
    _gebi(idTabActuel).classList.remove("active");
    // affiche le tab demandé
    _gebi('aff_'+tabButton.id).style.display = "block";
    _gebi(tabButton.id).classList.add("active");
    // mémorise le nouveau tab actuel
    idTabActuel = tabButton.id;
    affichage();
}