let words = ['Access', '-Granted-']
let currentWordIndex = 0;

function redirect() {
    var target_url = "{{ target_url }}";
    setTimeout(function() {
        window.location.href = target_url;
    }, 750); // Redirect after 0.5 seconds
}


function displayWord(word) {
    const lettersArray = word.split('');
    const resultElement = document.getElementById('currentWord');
    resultElement.textContent = '';
    let index = 0;

    function showNextLetter() {
        if (index < lettersArray.length) {
            resultElement.textContent += lettersArray[index];
            index++;
            setTimeout(showNextLetter, 150); // Adjust the timing here
        } else {
            if (currentWordIndex === 0) {
                firstWordBehavior(resultElement);
            } else if (currentWordIndex === 1) {
                secondWordBehavior(resultElement);
            } else {
                flashWord(resultElement);
            }
        }
    }

    showNextLetter();
}

function firstWordBehavior(element) {
    // No flashing for the first word
    const pastWordsElement = document.getElementById('pastWords');
    const newWordElement = document.createElement('p');
    newWordElement.textContent = element.textContent;
    pastWordsElement.appendChild(newWordElement);
    element.textContent = '';
    currentWordIndex++;
    setTimeout(() => displayWord(words[currentWordIndex]), 500); // Delay before next word
}

function secondWordBehavior(element) {
    flashWord(element); // Flashing behavior for the second word
}

function flashWord(element) {
    element.classList.add('flash');
    setTimeout(() => {
        element.classList.remove('flash');
        currentWordIndex++;
        const pastWordsElement = document.getElementById('pastWords');
        const newWordElement = document.createElement('p');
        newWordElement.textContent = element.textContent;
        pastWordsElement.appendChild(newWordElement);
        element.textContent = '';
        if (currentWordIndex < words.length) {
            setTimeout(() => displayWord(words[currentWordIndex]), 500); // Delay before next word
        } else {
            redirect();
        }
    }, 2250); // Flash animation duration (0.75s * 3)
}

window.onload = () => {
    displayWord(words[currentWordIndex]);
};
