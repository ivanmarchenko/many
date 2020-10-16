// подсчет всех checkbox .js-checkbox во время загрузки страницы
window.onload = function onstart() {
  try {
    numb_all.innerHTML = document.querySelectorAll("input.js-checkbox").length;
  }
  catch { }
};

// https://medium.com/@stasonmars/%D0%BF%D0%B5%D1%80%D0%B5%D1%85%D0%BE%D0%B4%D0%B8%D0%BC-%D1%81-jquery-%D0%BD%D0%B0-%D1%87%D0%B8%D1%81%D1%82%D1%8B%D0%B8%CC%86-javascript-e2b3c2c6ab4
// отслеживание нажатия checkbox
function checkboxClick() {
  try {
    // каждый раз при нажатии checkbox подсчитываю все нажатые checkbox
    var selectedCheckBoxes = document.querySelectorAll("input.js-checkbox:checked").length;
    // записываем в спан numb_of
    numb_of.innerHTML = selectedCheckBoxes;
    // кнопка "удалить выбранные"
    var delete_checked = document.getElementById("delete_checked");
    // кнопка "удалить все" - отключил
    // var delete_all = document.getElementById("delete_all");
    if (selectedCheckBoxes == 0) {
      // деактивируем "выбрать все"
      delete_checked.disabled = true;
      // деактивируем и скрываем "выбрать все"
      // delete_all.disabled = true;
      // delete_all.style.visibility = "hidden";
    }
    else {
      // активируем "удалить все"
      delete_checked.disabled = false;
    }

    // отключение/включение checkbox группового выбора при изменению остальных checkbox 
    var allCheckBoxes = document.querySelectorAll("input.js-checkbox").length;
    var checked_all = document.getElementById("js-checkbox-main");
    if (selectedCheckBoxes != allCheckBoxes) {
    // if (selectedCheckBoxes != allCheckBoxes && checked_all.checked == true) {
      // отменяем "выбрать все"
      checked_all.checked = false;
      // деактивируем и скрываем "выбрать все"
      // delete_all.disabled = true;
      // delete_all.style.visibility = "hidden";
    }
    if (selectedCheckBoxes == allCheckBoxes) {
      // чекаем checkbox "выбрать все"
      checked_all.checked = true;
      // активируем и показываем "выбрать все"
      // delete_all.disabled = false;
      // delete_all.style.visibility = "visible";
    }
  }
  catch { }
};

// работа с checkbox групповым
function checkedAll(source) {
  // кнопка "удалить выбранные"
  var delete_checked = document.getElementById("delete_checked");
  // кнопка "удалить все" - отключил
  // var delete_all = document.getElementById("delete_all");
  try {
    // checkbox "выбрать все"
    var checked_all = document.getElementById('js-checkbox-main');
    // все checkbox
    var CheckBoxes = document.getElementsByClassName("js-checkbox");
    // изменяем checked всех checkbox
    for (var i = 0, n = CheckBoxes.length; i < n; i++) {
      CheckBoxes[i].checked = source.checked;
    }
    if (checked_all.checked == true) {
      // если "выбрать все" то "выбрано N из N"
      numb_of.innerHTML = CheckBoxes.length;
      // активируем "удалить все"
      delete_checked.disabled = false;
      // активируем и показываем "выбрать все"
      // delete_all.disabled = false;
      // delete_all.style.visibility = "visible";
    }
    else {
      numb_of.innerHTML = "0";
      // деактивируем "выбрать все"
      delete_checked.disabled = true;
      // деактивируем и скрываем "выбрать все"
      // delete_all.disabled = true;
      // delete_all.style.visibility = "hidden";
    }
  }
  catch { }
};