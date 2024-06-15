let instName = document.getElementById("inst-name");
let instType = document.getElementById("inst-type");
let branch = document.getElementById("branch");
let category = document.getElementById("category");
let YEAR = document.getElementById("fiee");
let count = false;
const arr = ["--Select--" ,  "Indian Institute of Technology" , "National Institute of Technology" , "Indian Institute of Information Technology" , "Government Funded Technical Institutions"]
YEAR.addEventListener("change" , () =>{
    while(1){
        try {
            instType.children[0].remove();
        } 
        catch (error) {
            break;
        } 
    }
    for (const i in arr) {
        instType.add(new Option(arr[i]));
    }
})
instType.addEventListener("change" , (event) =>{
    const input = event.target.value;
    if(count){
        while(1){
            try {
                instName.children[0].remove();
            } 
            catch (error) {
                break;
            } 
        }
    }
    if(input === "National Institute of Technology"){
        for (const i in nit) {
            instName.add(new Option(nit[i]));
        }
        count = true;
    }
    else if(input === "Indian Institute of Technology"){
        for (const i in iit) {
            instName.add(new Option(iit[i]));

        }
        count = true;
    }
    else if(input === "Indian Institute of Information Technology"){
        for (const i in iiit) {
            instName.add(new Option(iiit[i]));

        }
        count = true;
    }
    else if(input === "Government Funded Technical Institutions"){
        for (const i in gfti) {
            instName.add(new Option(gfti[i]));

        }
        count = true;
    }
    else if(input === "ALL"){
        for (const i in alth) {
            instName.add(new Option(alth[i]));
        }
        count = true;
    }
})