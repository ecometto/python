
cadena1dig="SB1_ROI_SB1-SCE-1_20240605T100918.inp"
cadena2dig="SB1_ROI_SB1-SCE-34_20240605T100918.inp"
cadenas = [cadena1dig, cadena2dig]

const regexActual = "SB1_ROI_[a-zA-Z0-9-]{10}_[0-9]{8}T[0-9]{6}.inp";
const regexNueval = "SB1_ROI_[a-zA-Z0-9-]{9,10}_[0-9]{8}T[0-9]{6}.inp";

console.log("\n\n ***********************************");
console.log("PARA LA REGEX ANTERIOR: ");
for(cadena of cadenas){
    match = cadena.match(regexActual)
    if (match) {
        console.log("* Se encontró: " + match[0]);
    } else {
        console.log(`* No se encontró ${cadena}`);
    }
}

console.log("\n");
console.log("PARA LA NUEVA REGEX: ");
for(cadena of cadenas){
    match = cadena.match(regexNueval)
    if (match) {
        console.log("* Se encontró: " + match[0]);
    } else {
        console.log(`* No se encontró ${cadena}`);
    }
}
