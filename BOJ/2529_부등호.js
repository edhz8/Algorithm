const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "../input.txt")
  .toString()
  .split("\n")
let k = Number(input.shift())
const move = input.shift().split(" ")
let Min = "9".repeat(k + 1)
let Max = "0".repeat(k + 1)
const rec = (number) => {
  if (number.length == k + 1) {
    const result = number.join("")
    if (Min > result) Min = result
    if (Max < result) Max = result
    return
  }
  for (let i = 0; i < 10; i++) {
    if (
      number.length == 0 ||
      (move[number.length - 1] == ">" && number[number.length - 1] > i && number.findIndex((e) => e == i) == -1) ||
      (move[number.length - 1] == "<" && number[number.length - 1] < i && number.findIndex((e) => e == i) == -1)
    ) {
      number.push(i)
      rec(number)
      number.pop()
    }
  }
}
rec([])
console.log(Max)
console.log(Min)
