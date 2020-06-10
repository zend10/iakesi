let locationList = document.querySelectorAll("#highlight-list li img")
let locationOverlayList = document.querySelectorAll("#highlight-list li .overlay-background")

let highlightImage = document.getElementById("highlight-image")
let highlightName = document.getElementById("highlight-name")
let highlightRemarks = document.getElementById("highlight-remarks")

let navigationBar = document.getElementsByTagName("header")[0]
let appLogo = document.getElementsByClassName("app-logo")[0]

locationOverlayList[0].style.visibility = 'visible'

locationList.forEach(element => {
    element.onclick = function() {
        let index = Array.from(locationList).indexOf(this)
        locationOverlayList.forEach(overlay => { overlay.style.visibility = 'hidden' })
        locationOverlayList[index].style.visibility = 'visible'

        let name = this.alt
        let image = this.src
        let remarks = this.getAttribute("data-remarks")
    
        highlightImage.src = image
        highlightImage.alt = name
        highlightName.innerText = name
        highlightRemarks.innerText = remarks
    }
});

window.onscroll = function() {
    if (window.pageYOffset > appLogo.offsetTop) {
        navigationBar.classList.add('header-fixed')
    } else {
        navigationBar.classList.remove('header-fixed')
    }
}