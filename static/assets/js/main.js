
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
      slidesPerView: 1,
    },
    768: {
      slidesPerView: 2,
    },
    1024: {
      slidesPerView: 3,
    },
    1200: {
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
  const ov_hidden = document.getElementById('ov-hidden')
  const searchBarClose = document.getElementById('search-bar-close');
  const searchBtn = document.getElementById('search-btn');
  const searchBtn2 = document.getElementById('search-btn-2');
  const searchTopBar = document.getElementById('search-top-bar');

  // Check if elements exist before adding event listeners
      // Reusable function to toggle the class
      function toggleSearchBar() {
          searchTopBar.classList.toggle('search-bar-activate');
          ov_hidden.classList.toggle('ov-hidden');
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

// Function to handle adding the product to the cart
// function addToCart(event) {
//   event.preventDefault(); // Prevent default anchor behavior
  
//   // Get the selected size and color
//   var selectedSize = document.querySelector('input[name="size"]:checked');
//   var selectedColor = document.querySelector('input[name="color"]:checked');
  
//   if (!selectedSize || !selectedColor) {
//       alert("Please select both size and color.");
//       return;
//   }
  
//   // Get the product ID from the data attribute on the link
//   var productId = event.target.getAttribute("data-product-id");
  
//   // Prepare the data to send via GET or AJAX
//   var url = `/cart/add/${productId}/?size=${selectedSize.value}&color=${selectedColor.value}`;

//   // Using Fetch API for GET request (you can use AJAX or jQuery if you prefer)
//   fetch(url, {
//       method: "GET",
//   })
//   .then(response => response.json())
//   .then(data => {
//       if (data.success) {
//           alert("Item added to the cart!");
//           window.location.href = "/cart/"; // Redirect to cart page
//       } else {
//           alert("Failed to add item to cart.");
//       }
//   })
//   .catch(error => {
//       console.error("Error adding to cart:", error);
//       alert("An error occurred. Please try again.");
//   });
// }


