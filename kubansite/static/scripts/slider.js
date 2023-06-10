import ItcSimpleSlider from './simple-adaptive-slider.min.js';

const sliderContainer = document.querySelector('.product__slider-container');
const sliderList = document.querySelectorAll('.product__slider-item');
const sliderButtons = document.querySelectorAll('.slider__control');

if(sliderList.length > 1) {
  document.addEventListener('DOMContentLoaded', () => {
    // инициализация слайдера
    const slider = new ItcSimpleSlider('.itcss', {
      loop: true,
      autoplay: false,
      interval: 5000,
      swipe: true,
    });

    sliderContainer.querySelector('.slider__control_prev').addEventListener('click', () => slider.prev());
    sliderContainer.querySelector('.slider__control_next').addEventListener('click', () => slider.next());

  });
} else {
  sliderButtons.forEach(button => button.remove());
}
