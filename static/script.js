document.getElementById("programmatic-solution-toggle").addEventListener("click", function() {
    var answerList = document.getElementById("programmatic-solution-list");
    answerList.classList.toggle("visible");
});

document.getElementById("nyt-solution-toggle").addEventListener("click", function() {
    var answerList = document.getElementById("nyt-solution");
    answerList.classList.toggle("visible");
});