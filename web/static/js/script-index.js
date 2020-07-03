let locationList = document.querySelectorAll("#highlight-list li img")
let locationOverlayList = document.querySelectorAll("#highlight-list li .overlay-background")

let highlightUrl = document.getElementById("highlight-url")
let highlightImage = document.getElementById("highlight-image")
let highlightName = document.getElementById("highlight-name")
let highlightRemarks = document.getElementById("highlight-remarks")

locationOverlayList[0].style.visibility = 'visible'

locationList.forEach(element => {
    element.onclick = function() {
        let index = Array.from(locationList).indexOf(this)
        locationOverlayList.forEach(overlay => { overlay.style.visibility = 'hidden' })
        locationOverlayList[index].style.visibility = 'visible'

        let url = this.getAttribute("data-url")
        let name = this.alt
        let image = this.src
        let remarks = this.getAttribute("data-remarks")
    
        highlightUrl.href = url
        highlightImage.src = image
        highlightImage.alt = name
        highlightName.innerText = name
        highlightRemarks.innerText = remarks
    }
});