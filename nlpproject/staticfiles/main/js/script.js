var last="op";

function addWord() {
    var ul = document.getElementById("query-list");
    var word = document.getElementById("word-input");
    var li = document.createElement("li");
    if(word.value!==" ") {
        if(last!=="word"){
            li.appendChild(document.createTextNode(word.value));
            ul.appendChild(li);
            word.value='';
            last = "word";
        }
        else {
            alert("Cannot enter two words in a row!");
        }
    }
    else {
        alert("Blank Field!");
    }
}
function addOp(op) {
    var ul = document.getElementById("query-list");
    var li = document.createElement("li");
    if(last!=="op"){
        li.appendChild(document.createTextNode(op.value));
        ul.appendChild(li);
        last = "op";
    }
    else {
        alert("Cannot enter two operators in a row!");
    }
}

function sendQuery() {
    var form = document.getElementById("query-form");
    var query = "";
    const list = document.querySelectorAll('#query-list li');
    if(last!=="op") {
        for (let i = 0; i < list.length; i++) {
            query += list[i].textContent.toLowerCase() + ' ';
        }
        document.getElementById("query").value = query;
        form.submit();
    }
    else {
        alert("Operator should have an ending word!");
    }
}
