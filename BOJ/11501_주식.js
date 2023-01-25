const input = require("fs").readFileSync("../input.txt").toString().split("\n")
const T = Number(input.shift())
for (let i = 0; i < T; i++) {
  input.shift()
  let Max = 0
  let answer = 0
  input
    .shift()
    .split(" ")
    .reverse()
    .forEach((num) => {
      num = Number(num)
      Max = Math.max(Max, num)
      answer += Max - num
    })
  console.log(answer)
}
