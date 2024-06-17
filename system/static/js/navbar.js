
function dropdownfunc() {
  document.getElementById("dropdownContent").classList.toggle("show");
}

// Закрыть раскрывающийся список, если пользователь щелкнет за его пределами.
window.onclick = function(e) {
  if (!e.target.matches('.dropbtn')) {
  let dropDownContent = document.getElementById("dropdownContent");
    if (dropDownContent.classList.contains('show')) {
      dropDownContent.classList.remove('show');
    }
  }
}