




let fileText = '';

const fileInput = document.getElementById('file-input');
fileInput.onchange = () => {
    let fs = new FileReader();
    fs.readAsText(fileInput.files[0]);
    fs.onload = () => {
        handleResults(fs.result);
    }
}

function handleResults(result) {
    fileText = result;
    solveDayOne(fileText);
    solveDayTwo(fileText);

}

function solveDayOne(fileText) {
    let solution = NaN;
    document.getElementById("solution-1").replaceWith(`Solution: ${solution}`);
}

function solveDayTwo(fileText) {
    let solution = NaN;
    document.getElementById("solution-2").replaceWith(`Solution: ${solution}`);
}