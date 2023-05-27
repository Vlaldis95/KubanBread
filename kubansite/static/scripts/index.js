const menuBurger = document.querySelector('.menu-burger');
const menuBurgerSpans = menuBurger.querySelectorAll('.menu-burger__item');
const headerMenu = document.querySelector('.header__nav');
const anchors = document.querySelectorAll('a[href*="#"]');


function toggleHeaderMenu() {
  headerMenu.classList.toggle('header__nav_opened');
  menuBurgerSpans.forEach(function(item) {
    item.classList.toggle('menu-burger__item_active');
  });
}

menuBurger.addEventListener('click', toggleHeaderMenu);

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
      window.location.href = anchorHref;
    }

  });
});
