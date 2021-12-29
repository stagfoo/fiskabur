// This will be replaced with your chumbucket build but here is some helpful functions

window.addEventListener('pywebviewready', function() {
    document.querySelector('#app h1').innerHTML = '<i>pywebview</i> is ready'
})

function getImage(){
    document.querySelector('#app h1').innerText = "pressed";
    pywebview.api.openFile().then((fileName) => {
        document.querySelector('#app h1').innerText = fileName;
    })
}