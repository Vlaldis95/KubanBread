import FormValidator from './FormValidator.js';

// ====================== константы =====================================================
const formNewCard = document.forms['contact_form'];

const formValidators = {};
// ======================================================================================

// ====================== функции =======================================================

// функция добавления новой карточки
// function submitFormNewCard(e) {
//   e.preventDefault();
//   formNewCard.reset();
// }

// ======================================================================================

// ================ циклы ===============================================================

// вывод массива карточек на страницу

// запуск валидации всех форм
Array.from(document.forms).forEach(item => {
  const formValid = new FormValidator({
    formSelector: '.form',
    inputSelector: '.form__input',
    submitButtonSelector: '.form__submit',
    inactiveButtonClass: 'form__submit_disabled',
    inputErrorClass: 'form__input_type_error',
    errorClass: 'form__input-error_visible'
    }, item);
    //добавление данных о валидируемой форме
    const formName = item.getAttribute('name');
    formValidators[formName] = formValid;
    //включение валидации
    formValid.enableValidation();
 });

// ======================================================================================

// ================ слушатели событий ===================================================

// добавление новой карточки
// formNewCard.addEventListener('submit', submitFormNewCard);
// ======================================================================================
