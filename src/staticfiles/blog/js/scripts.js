let navBtn = document.querySelector(".nav-btn");
let closeBtn = document.querySelector(".nav-close-btn");
let navBar = document.querySelector(".close-links")
let footerDate = document.querySelector(".footer-date")
let backToTop = document.querySelector(".back-to-top")
let articleLinks = document.querySelector(".article-links")
let articleToggle = document.querySelector(".article-click")
let subOverlay = document.querySelector(".sub_overlay");
let openOverlay = document.querySelector("#subscribe_here");
let closeOverlay = document.querySelector(".close-overlay");


navBtn.addEventListener("click", function(){
  navBar.classList.toggle("show-nav")
})

closeBtn.addEventListener("click", function(){
  navBar.classList.remove("show-nav")
})

let date = new Date();
let year = date.getFullYear();
footerDate.innerHTML = year;


window.addEventListener("scroll", function(){
  let height = window.pageYOffset;
  if (height > 1000) {
    backToTop.classList.add("show-scroll")
  } else {
    backToTop.classList.remove("show-scroll")
  }
}
)

articleToggle.addEventListener("click", function () {
  articleLinks.classList.toggle("show-articles")
})

backToTop.addEventListener("click", function(){
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
  })



openOverlay.addEventListener("click", function(){
  subOverlay.classList.add("show_overlay")
})
closeOverlay.addEventListener("click", function(){
  subOverlay.classList.remove("show_overlay")
})