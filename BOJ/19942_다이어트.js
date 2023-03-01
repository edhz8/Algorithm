const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "../input.txt")
  .toString()
  .split("\n")
const N = Number(input.shift())
const M = input.shift().split(" ").map(Number)
const infos = []
for (let i = 0; i < N; i++) infos.push(input.shift().split(" ").map(Number))
const v = []
const info = [0, 0, 0, 0, 0]
let answer1 = Number.MAX_VALUE
let answer2 = []
const rec = (start) => {
  if (M.every((e, i) => e <= info[i])) {
    if (answer1 > info[4]) {
      answer1 = info[4]
      answer2 = [...v]
    }
    return
  }
  for (let i = start; i < N; i++) {
    v.push(i + 1)
    for (let j = 0; j < 5; j++) info[j] += infos[i][j]
    rec(i + 1)
    for (let j = 0; j < 5; j++) info[j] -= infos[i][j]
    v.pop()
  }
}
rec(0)
if (answer1 === Number.MAX_VALUE) {
  console.log(-1)
} else {
  console.log(answer1)
  console.log(answer2.join(" "))
}
