let navigationBar = document.getElementsByTagName("header")[0]
let appLogo = document.getElementsByClassName("app-logo")[0]

if (screen.width < 1024) {
    navigationBar.classList.add('header-fixed')
} else {
    window.onscroll = function() {
        if (window.pageYOffset > appLogo.offsetTop) {
            navigationBar.classList.add('header-fixed')
        } else {
            navigationBar.classList.remove('header-fixed')
        }
    }
}

