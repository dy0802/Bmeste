const galleryContainer = document.querySelector('.gallery-container');
const galleryControlsContainer = document.querySelector('.gallery-controls');
const galleryControls = ['previous', 'next'];
const galleryDivs = document.querySelectorAll('.gallery-item');
const galleryPhotos = document.querySelectorAll('.gallery-photo');

class Carousel {
  constructor(container, divs, photos, controls) {
    this.carouselContainer = container;
    this.carouselControls = controls;
    this.carouselDiv = [...divs];
    this.carouselPhoto = [...photos]
  }

  // Update css classes for gallery
  updateGallery() {
    this.carouselDiv.forEach(el => {
      el.classList.remove('gallery-item-1');
      el.classList.remove('gallery-item-2');
      el.classList.remove('gallery-item-3');
      el.classList.remove('gallery-item-4');
      el.classList.remove('gallery-item-5');
    
    });

    this.carouselDiv.slice(0, 5).forEach((el, i) => {
      el.classList.add(`gallery-item-${i+1}`);
    });

    this.carouselPhoto.forEach(el => {
      el.classList.remove('gallery-photo-1');
      el.classList.remove('gallery-photo-2');
      el.classList.remove('gallery-photo-3');
      el.classList.remove('gallery-photo-4');
      el.classList.remove('gallery-photo-5');  
    });
    this.carouselPhoto.slice(0, 5).forEach((el, i) => {
      el.classList.add(`gallery-photo-${i+1}`);
    });    
  }

  // Update the current order of the carouselArray and gallery
  setCurrentState(direction) {

    if (direction.className == 'gallery-controls-previous') {
      this.carouselDiv.unshift(this.carouselDiv.pop());
      this.carouselPhoto.unshift(this.carouselPhoto.pop());
    } else {
      this.carouselDiv.push(this.carouselDiv.shift());
      this.carouselPhoto.push(this.carouselPhoto.shift());
    }
    
    this.updateGallery();
  }

  // Construct the carousel controls
  setControls() {
    this.carouselControls.forEach(control => {
      galleryControlsContainer.appendChild(document.createElement('button')).className = `gallery-controls-${control}`;

      document.querySelector(`.gallery-controls-${control}`).innerText = control;
    });
  }
 
  // Add a click event listener to trigger setCurrentState method to rearrange carousel
  useControls() {
    const triggers = [...galleryControlsContainer.childNodes];

    triggers.forEach(control => {
      control.addEventListener('click', e => {
        e.preventDefault();
        this.setCurrentState(control);
      });
    });
  }
}

const exampleCarousel = new Carousel(galleryContainer, galleryDivs, galleryPhotos, galleryControls);

exampleCarousel.setControls();
exampleCarousel.useControls();
