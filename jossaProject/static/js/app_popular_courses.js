let instName = document.getElementById("inst-name");
let instType = document.getElementById("inst-type");
let branch = document.getElementById("branch");
var scrollToTopBtn = document.getElementById("scrollToTopBtn");
var rootElement = document.documentElement;
let category = document.getElementById("category");
let YEAR = document.getElementById("fiee");
let ROUND = document.getElementById("fie");
const cate  =[ "--Select" , "OPEN" , "OPEN (PwD)" , "EWS" ,"EWS (PwD)" , "OBC-NCL" , "OBC-NCL (PwD)" , "SC" , "ST", "SC (PwD)" , "ST (PwD)"]
let count = false;
const arr = ["--Select--" ,"ALL" , "Indian Institute of Technology" , "National Institute of Technology" , "Indian Institute of Information Technology" , "Government Funded Technical Institutions"]
const no = ["--Select--" , "1" , "2" , "3" , "4" , "5" , "6"]
YEAR.addEventListener("change" , () =>{
    while(1){
        try {
            ROUND.children[0].remove();
        } 
        catch (error) {
            break;
        } 
    }
    for (const i in cate) {
        ROUND.add(new Option(cate[i]));
    }
})
ROUND.addEventListener("change" , () =>{
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
const cate1  =[ "--Select--" ,  "Gender-Neutral" , "Female-only (including Supernumerary)"]
instName.addEventListener("change" , (evt) =>{
    while(1){
        try {
            branch.children[0].remove();
        } 
        catch (error) {
            break;
        } 
    }
    let inn = evt.target.value;
    console.log(inn);
    for (const i in cate1) {
        branch.add(new Option(cate1[i]));
    }
});
function scrollToTop() {
    // Scroll to top logic
    rootElement.scrollTo({
      top: 0,
      behavior: "smooth"
    })
}
scrollToTopBtn.addEventListener("click", scrollToTop);