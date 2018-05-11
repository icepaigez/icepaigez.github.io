var myImage = document.querySelector('img');

myImage.onclick = function() {
    var mySrc = myImage.getAttribute('src');
    if(mySrc === 'images/firefox-icon.png') {
      myImage.setAttribute ('src','images/soulja boys.jpeg');
    } else {
      myImage.setAttribute ('src','images/polar bear.jpeg');
    }
}
