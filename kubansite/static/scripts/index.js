(()=>{"use strict";var e=document.querySelector(".menu-burger"),t=e.querySelectorAll(".menu-burger__item"),r=document.querySelector(".header__nav"),c=document.querySelectorAll('a[href*="#"]');function n(){r.classList.toggle("header__nav_opened"),t.forEach((function(e){e.classList.toggle("menu-burger__item_active")}))}e.addEventListener("click",n),c.forEach((function(e){e.addEventListener("click",(function(e){n()}))}))})();


// const menuBurger = document.querySelector('.menu-burger');
// const menuBurgerSpans = menuBurger.querySelectorAll('.menu-burger__item');
// const headerMenu = document.querySelector('.header__nav');
// const anchors = document.querySelectorAll('a[href*="#"]');


// function toggleHeaderMenu() {
//   headerMenu.classList.toggle('header__nav_opened');
//   menuBurgerSpans.forEach(function(item) {
//     item.classList.toggle('menu-burger__item_active');
//   });
// }

// menuBurger.addEventListener('click', toggleHeaderMenu);

// // перемещение к элементам сайта
// anchors.forEach(anchor => {
//   anchor.addEventListener('click', (e) => {
//     e.preventDefault();
//     const anchorHref = anchor.getAttribute('href');
//     const index = anchorHref.lastIndexOf("#");

//     const blockId = anchorHref.substr(index+1);
//     const elementBlockId = document.getElementById(blockId);

//     toggleHeaderMenu();

//   });
// });
