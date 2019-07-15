const md5 = require("blueimp-md5")
const palettes = {
    "ocean": ["#DDE5FF", "#9BB2FF", "#7A99FF", "#597FFF"],
    "sunset": ["#FFE0BA", "#FFB978", "#FF898B", "#DB8CD2"],
    "caterpillar": ["#E9FFCC", "#A8FFAB", "#7FF0C3", "#7FD5C3"]
}

let icon = [
    ["0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0"]
]

function get_palettes() {
    let acc = "";
    for (var p in palettes) {
        acc += p + " ";
    }
    return acc.trim();
}

function md5_hash(s) {
    return md5(s);
}