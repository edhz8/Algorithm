const input = require("fs").readFileSync("../input.txt").toString().split("\n")
const n = Number(input.shift())
const dp = Array(n).fill(0)
let prev = 0
for (let i = 0; i < n; i++) {
  const [t, p] = input.shift().split(" ").map(Number)
  if (i > 0) prev = Math.max(prev, dp[i - 1])
  const future_index = i + t - 1
  if (future_index < n) dp[future_index] = Math.max(dp[future_index], prev + p)
}
console.log(Math.max(...dp))
