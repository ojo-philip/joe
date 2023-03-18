let navBtn = document.querySelector(".nav-btn");
let closeBtn = document.querySelector(".nav-close-btn");
let navBar = document.querySelector(".close-links")
let footerDate = document.querySelector(".footer-date")
let backToTop = document.querySelector(".back-to-top")
let articleLinks = document.querySelector(".article-links")
let articleToggle = document.querySelector(".article-click")



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