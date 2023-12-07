let dataPython;
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
    return userData
}

function init(){
    document.querySelector("form").addEventListener("submit",retrieveData)
}

eel.expose(exportPython)
function exportPython(){
    return dataPython;
}