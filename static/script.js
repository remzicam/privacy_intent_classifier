const textGenForm = document.querySelector('.text-gen-form');

const translateText = async (text) => {
    const inferResponse = await fetch(`infer_intents?input=${text}`);
    const inferJson = await inferResponse.json();

    return inferJson.output;
};


textGenForm.addEventListener('submit', async (event) => {
  event.preventDefault();

  const textGenInput = document.getElementById('text-gen-input');
  const textGenParagraph = document.querySelector('.text-gen-output');
  textGenParagraph.innerHTML = "";
  try {
    var object= await translateText(textGenInput.value);
    
    for (const [key, value] of Object.entries(object)) { 
      textGenParagraph.innerHTML+=(`<span style='color:#0068C9;'> • ${key}</span> : <span style='color:red;'> ${value}</span><br><br>`);
    }
  } catch (err) {
    console.error(err);
  }
});

// Get the modal
var modal = document.getElementById("myModal");

// Get the button that opens the modal
var btn = document.getElementById("myBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on the button, open the modal
btn.onclick = function() {
  modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}