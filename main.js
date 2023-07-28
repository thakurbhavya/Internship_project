document.getElementById('imageInput').addEventListener('change', function (e) {
  const file = e.target.files[0];
  const reader = new FileReader();

  reader.onload = function (event) {
    const dataURL = event.target.result;
    const image = new Image();
    image.src = dataURL;
    image.onload = function () {
      document.getElementById('imageDisplay').innerHTML = '';
      document.getElementById('imageDisplay').appendChild(image);
    };

    const imageString = dataURL.split(',')[1];
    document.getElementById('outputText').innerText = 'Class 1: ' + imageString;
  };

  if (file) {
    reader.readAsDataURL(file);
  }
});
