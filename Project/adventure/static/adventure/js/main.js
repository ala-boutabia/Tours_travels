

window.addEventListener('scroll', function () {

    let nav = document.querySelector('nav')
    let windowPosition = window.screenY > 100;
    nav.classList.toggle('window-scroll', windowPosition)

})

