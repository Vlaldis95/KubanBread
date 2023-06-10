const filterForm = document.querySelector('.filter__form');
const filterInput = document.querySelector('.filter__input');

filterInput.addEventListener('input', () => filterForm.submit());

