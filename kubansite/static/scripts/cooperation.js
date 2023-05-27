import FormValidator from './FormValidator.js';

const menuBurger = document.querySelector('.menu-burger');
const menuBurgerSpans = menuBurger.querySelectorAll('.menu-burger__item');
const headerMenu = document.querySelector('.header__nav');
const anchors = document.querySelectorAll('a[href*="#"]');

const selectChanel = document.querySelector('.popup__select_type_chanel');
const selectTax = document.querySelector('.popup__select-wrapper_type_tax');

function toggleHeaderMenu() {
  headerMenu.classList.toggle('header__nav_opened');
  menuBurgerSpans.forEach(function(item) {
    item.classList.toggle('menu-burger__item_active');
  });
}

menuBurger.addEventListener('click', toggleHeaderMenu);

// запуск валидации всех форм
Array.from(document.forms).forEach(item => {
  const formValid = new FormValidator({
    formSelector: '.popup__form',
    inputSelector: '.popup__input',
    submitButtonSelector: '.popup__button',
    inactiveButtonClass: 'popup__button_disabled',
    inputErrorClass: 'popup__input_type_error',
    errorClass: 'popup__error_visible'
    },
    item
    );
    //включение валидации
    formValid.enableValidation();
 });

// добавлени поля выбора налога НДС
selectChanel.addEventListener('input', (e) => {
  e.target.value === 'Физ.лицо'
  ? selectTax.classList.remove('popup__select-wrapper_closed')
  : selectTax.classList.add('popup__select-wrapper_closed');
});

// перемещение к элементам сайта
anchors.forEach(anchor => {
  anchor.addEventListener('click', (e) => {
    e.preventDefault();
    const anchorHref = anchor.getAttribute('href');
    const index = anchorHref.lastIndexOf("#");

    const blockId = anchorHref.substr(index+1);
    const elementBlockId = document.getElementById(blockId);

    toggleHeaderMenu();

    if(elementBlockId) {
      elementBlockId.scrollIntoView({
        behavior: "smooth",
        block: "start",
        inline: "nearest"});
    } else {
      window.location.href = anchorHref
    }

  });
});
