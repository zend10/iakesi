let modalContainer = document.getElementById("modal-container")
let modalImage = document.getElementById("modal-image")
let modalCaption = document.getElementById("modal-caption")

let locationList = document.querySelectorAll("#section-locations .item-image img")
locationList.forEach(element => {
    element.onclick = function() {
        modalContainer.style.display = "block"
        modalImage.src = this.src
        modalCaption.innerHTML = this.alt
    }
})

let modalClose = document.getElementById("modal-close")

modalClose.onclick = function() {
    modalContainer.style.display = "none"
}
