const md5 = require("blueimp-md5");
const assert = require("assert");
const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});
const palettes = {
  ocean: ["#DDE5FF", "#9BB2FF", "#7A99FF", "#597FFF"],
  sunset: ["#FFE0BA", "#FFB978", "#FF898B", "#DB8CD2"],
  dragon: ["#E3FFEE", "#84CFA3", "#57B098", "#308A8F"]
};

let icon = [
  ["0", "0", "0", "0", "0", "0"],
  ["0", "0", "0", "0", "0", "0"],
  ["0", "0", "0", "0", "0", "0"],
  ["0", "0", "0", "0", "0", "0"],
  ["0", "0", "0", "0", "0", "0"],
  ["0", "0", "0", "0", "0", "0"]
];

function get_palettes() {
  let acc = "";
  for (let p in palettes) {
    acc += p + " ";
  }
  return acc.trim();
}

function hex_to_dec(n) {
  return parseInt(n, 16);
}

function fill_icon(hash_str, num, palette) {
  let row = 0;
  let col = 0;
  for (let c = 0; c < 18; c++) {
    let color_index = hex_to_dec(hash_str[c]) % num;
    let color = palette[color_index];
    icon[row][col] = icon[row][5 - col] = color;
    if (col === 2) {
      row += 1;
      col = 0;
    } else {
      col += 1;
    }
  }
}

function generate_img(username, bg_color) {
  return NaN;
}

function main() {
  console.log("test");
  let user = "";
  rl.question("yss", answer => {
    user = answer;
    rl.close();
  });
  console.log(user);
  fill_icon(md5("matt"), 3, palettes["dragon"]);
  console.log(icon);
}

main();
