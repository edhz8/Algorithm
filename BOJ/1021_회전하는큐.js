const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "../input.txt")
  .toString()
  .split("\n")
let [N, M] = input.shift().split(" ").map(Number)
let nums = input.shift().split(" ").map(Number)
let q = Array.from({ length: N }, (_, i) => i + 1)
let cnt = 0
for (const num of nums) {
  // console.log(num)
  while (1) {
    if (q[0] === num) {
      q.shift()
      break
    } else if (q.indexOf(num) <= q.length / 2) q.push(q.shift())
    else q.unshift(q.pop())
    cnt++
    // console.log(q)
  }
}
console.log(cnt)
