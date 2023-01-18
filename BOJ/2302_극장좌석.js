const input = require("fs").readFileSync("../input.txt").toString().split("\n").map(Number)
let N = input.shift()
input.shift()
const nums = new Set(input)
dp = Array(N + 1).fill(0)
dp[0] = dp[1] = 1
for (let i = 2; i < N + 1; i++) {
  dp[i] += dp[i - 1]
  if (!nums.has(i) && !nums.has(i - 1)) dp[i] += dp[i - 2]
}
console.log(dp[N])
