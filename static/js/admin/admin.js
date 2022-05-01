function ShowModal(id)
{
  var modal = document.getElementById(id);
  modal.style.display = "block";

  // Get the <span> element that closes the modal
var span = document.getElementsByClassName("close " + id)[0];

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
}
