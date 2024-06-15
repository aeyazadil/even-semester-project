let instName = document.getElementById("inst-name");
let instType = document.getElementById("inst-type");
let branch = document.getElementById("branch");
var scrollToTopBtn = document.getElementById("scrollToTopBtn");
var rootElement = document.documentElement;
let category = document.getElementById("category");
let YEAR = document.getElementById("fiee");
let ROUND = document.getElementById("fie");
let count = false;
const arr = ["--Select--" , "ALL", "Indian Institute of Technology" , "National Institute of Technology" , "Indian Institute of Information Technology" , "Government Funded Technical Institutions"]
const no = ["--Select--" , "1" , "2" , "3" , "4" , "5" , "6"]
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
            // instName.options[i] = new Option(nit[i]);
            instName.add(new Option(nit[i]));
        }
        count = true;
    }
    else if(input === "Indian Institute of Technology"){
        for (const i in iit) {
            // instName.options[i] = new Option(iit[i]);
            instName.add(new Option(iit[i]));

        }
        count = true;
    }
    else if(input === "Indian Institute of Information Technology"){
        for (const i in iiit) {
            // instName.options[i] = new Option(iiit[i]);
            instName.add(new Option(iiit[i]));

        }
        count = true;
    }
    else if(input === "Government Funded Technical Institutions"){
        for (const i in gfti) {
            // instName.options[i] = new Option(gfti[i]);
            instName.add(new Option(gfti[i]));

        }
        count = true;
    }
    else if(input === "ALL"){
        for (const i in alth) {
            // instName.options[i] = new Option(alth[i]);
            instName.add(new Option(alth[i]));

        }
        count = true;
    }
})