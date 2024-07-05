
function dropdownfunc() {
  document.getElementById("dropdownContent").classList.toggle("show");
}

// Закрыть раскрывающийся список, если пользователь щелкнет за его пределами.
window.onclick = function(e) {
  if (!e.target.matches('.dropbtn')) {
  let dropdownContent = document.getElementById("dropdownContent");
    if (dropdownContent.classList.contains('show')) {
      dropdownContent.classList.remove('show');
    }
  }
}

function filterdropdownfunc() {
  document.getElementById("filterDropdownContent").classList.toggle("show");
}

