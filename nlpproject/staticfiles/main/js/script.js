var last="op";

function addWord() {
    var ul = document.getElementById("query");
    var word = document.getElementById("word-input");
    var li = document.createElement("li");
    if(word.value.length>1 && last!="word"){
        li.appendChild(document.createTextNode(word.value));
        ul.appendChild(li);
        word.value='';
        last = "word";
    }
}
function addOp(op) {
    var ul = document.getElementById("query");
    var li = document.createElement("li");
    if(last!="op"){
        li.appendChild(document.createTextNode(op.value));
        ul.appendChild(li);
        last = "op";
    }
}
