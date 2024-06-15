let instName = document.getElementById("inst-name");
let instType = document.getElementById("inst-type");
let branch = document.getElementById("branch");
var scrollToTopBtn = document.getElementById("scrollToTopBtn");
var rootElement = document.documentElement;
let category = document.getElementById("category");
let YEAR = document.getElementById("fiee");
let ROUND = document.getElementById("fie");
const cate  =[ "--Select" , "OPEN" ,  "EWS" , "OBC-NCL" , "SC" , "ST",]
let count = false;
const arr = ["--Select--" , "Indian Institute of Technology" , "National Institute of Technology" , "Indian Institute of Information Technology" , "Government Funded Technical Institutions"]
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
            instName.children[0].remove();
        } 
        catch (error) {
            break;
        } 
    }
    for (const i in nit) {
        instName.add(new Option(nit[i]));
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