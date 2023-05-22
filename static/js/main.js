 "uase strict";

const selectionArea = document.querySelector("#select-area"),
fileInput = document.querySelector(".file-input");
// 2nd 
let preview= document.getElementById("file-preview");

// 4th
let removeImage=document.getElementById("remove-img");
// part2 -- delete hone k bad normal box nhi aa raha tha gayab hogya
removeImage.style.display="none";

removeImage.addEventListener("click",()=>{
    fileInput.value=null;
    preview.src=null;
    preview.style.display="none";
    removeImage.style.display="none";
    // part1 -- delete hone k bad normal box nhi aa raha tha gayab hogya  
    selectionArea.style.display=null;
})

// first..... this after completing the html ans css part 
// this help to choice a image if we click the select JPG box
selectionArea.addEventListener("click",()=>{
    fileInput.click();
});

// 3rd
fileInput.onchange=({
    target
})=>{
    let file = target.files[0];
    if(file.type=="image/jpeg" || file.type=="image/png"){
        let image_url=URL.createObjectURL(file);
        preview.src =image_url;
        //3rd.01
        // this i for taking image within box
        selectionArea.style.display ="none";
        // part3 -- delete hone k bad normal box nhi aa raha tha gayab hogya
        removeImage.style.display=null;
        preview.style.display=null;
        
    }
    else{
        alert("Please select a jpg file");
        fileInput.value = null;
    }
}