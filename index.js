
  document.addEventListener("DOMContentLoaded", function() {
    var professionElement = document.getElementById("profession");
    var texts = ["Developer", "Freelancer"]; // Array of texts to show
    var currentTextIndex = 0; // Index of the current text being displayed
    var currentLetterIndex = 0; // Index of the current letter being displayed

    // Function to show the next letter of the current text
    function showNextLetter() {
        var currentText = texts[currentTextIndex];
        if (currentLetterIndex < currentText.length) {
            var partialText = currentText.substring(0, currentLetterIndex + 1);
            professionElement.textContent = partialText;
            currentLetterIndex++;
        } else {
            // Reset currentLetterIndex if reached the end of the text
            currentLetterIndex = 0;
            // Move to the next text
            currentTextIndex = (currentTextIndex + 1) % texts.length;
        }
    }

    // Call showNextLetter every 200 milliseconds
    setInterval(showNextLetter, 400);
});

