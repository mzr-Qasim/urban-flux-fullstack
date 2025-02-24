
// Home Page

var swiper = new Swiper(".mySwiper", {
  loop: true,
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
  // autoplay: {
  //   delay: 5000,
  //   disableOnInteraction: false,
  // },
});




var swiper2 = new Swiper(".mySwiper2", {
  slidesPerView: 1,
  spaceBetween: 20,
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
  breakpoints: {
    640: {
      slidesPerView: 2,
    },
    768: {
      slidesPerView: 3,
    },
    1024: {
      slidesPerView: 4,
    },
  },
});




var swiper3 = new Swiper(".mySwiper3", {
  slidesPerView: 1,
  spaceBetween: 20,
  autoplay: {
    delay: 5000,
    disableOnInteraction: false,
  },
  breakpoints: {
    768: {
      slidesPerView: 2,
    },
  },
});

// Product Detail Page

// $(function(){
//   var slider = new Swiper ('.gallery-slider', {

//     slidesPerView: 1,
//     navigation: {
//         nextEl: '.swiper-button-next',
//         prevEl: '.swiper-button-prev',
//     },
//   });


//   var thumbs = new Swiper ('.gallery-thumbs', {
//     slidesPerView: 3,
//             centeredSlides: true,
//             slideToClickedSlide: true,
//           });

//           slider.controller.control = thumbs;
//           thumbs.controller.control = slider;
//     });


// Product Detail Swiper

var swiper = new Swiper(".gallery-thumbs", {
  spaceBetween: 10,
  slidesPerView: 4,
});
var swiper2 = new Swiper(".gallery-slider", {
  spaceBetween: 10,
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
  thumbs: {
    swiper: swiper,
  },
});


// Related Products Swiper
var mySwiper_related_product = new Swiper(".mySwiper_related_products", {
  slidesPerView: 1,
  spaceBetween: 20,
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
  breakpoints: {
    640: {
      slidesPerView: 2,
    },
    768: {
      slidesPerView: 3,
    },
    1024: {
      slidesPerView: 4,
    },
  },
});




// Search Bar


document.addEventListener('DOMContentLoaded', function () {
  // Store references to the elements in variables
  const searchBarClose = document.getElementById('search-bar-close');
  const searchBtn = document.getElementById('search-btn');
  const searchBtn2 = document.getElementById('search-btn-2');
  const searchTopBar = document.getElementById('search-top-bar');

  // Check if elements exist before adding event listeners
      // Reusable function to toggle the class
      function toggleSearchBar() {
          searchTopBar.classList.toggle('search-bar-activate');
      }

      // Add event listeners using the variables and reusable function
      searchBarClose.addEventListener('click', toggleSearchBar);
      searchBtn.addEventListener('click', toggleSearchBar);
      searchBtn2.addEventListener('click', toggleSearchBar);
  
});



// Filter


let filter_close_button = document.getElementById('filter_close_button');
let filters_sidebar = document.getElementById('filters-sidebar');
let filter_button = document.getElementById('filter_button');

filter_close_button.addEventListener('click', function () {
  filters_sidebar.classList.toggle('open');
});

filter_button.addEventListener('click', function () {
  filters_sidebar.classList.toggle('open');
});



// Quantity Selector



document.addEventListener('DOMContentLoaded', function() {
  // Get all the filter category radio buttons
  const filterCategoryRadios = document.querySelectorAll('input[name="filter_category"]');

  // Listen for when a radio button is selected
  filterCategoryRadios.forEach(function(radio) {
      radio.addEventListener('change', function() {
          const selectedCategoryId = this.getAttribute('data-category'); // Get the selected category ID

          // Get all product items
          const productItems = document.querySelectorAll('.product-item');

          productItems.forEach(function(item) {
              // If the category is "All", show all products
              if (selectedCategoryId === "All") {
                  item.style.display = 'block';
              } else {
                  // Otherwise, compare the selected category with the product's category
                  if (item.getAttribute('data-category') == selectedCategoryId) {
                      item.style.display = 'block';  // Show the product if it matches
                  } else {
                      item.style.display = 'none';  // Hide the product if it doesn't match
                  }
              }
          });
      });
  });
});









