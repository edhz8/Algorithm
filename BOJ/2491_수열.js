const input = require("fs").readFileSync("../input.txt").toString().split("\n")
const N = Number(input[0])
const nums = input[1].split(" ").map((e) => Number(e))
let answer = 1
let asc = 1
let desc = 1
for (let i = 0; i < N - 1; i++) {
  if (nums[i] <= nums[i + 1]) asc++
  else asc = 1
  if (nums[i] >= nums[i + 1]) desc++
  else desc = 1
  answer = Math.max(answer, asc, desc)
}
console.log(answer)
