function checkWord() {
    const userInput = document.getElementById('user-input').value;
    // Dummy validation: checks if the input is not empty
    if (userInput.trim() === '') {
        alert('Please enter a word.');
    } else {
        // Implement actual game logic here
        alert('Word submitted: ' + userInput);
    }
}
