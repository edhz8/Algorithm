const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "../input.txt")
  .toString()
  .split("\n")
let N = Number(input.shift())
const G = input.map((e) => e.split(" ").map(Number))
const dp = Array.from(Array(N), () => Array(N).fill(0n))
dp[0][0] = 1n
for (let i = 0; i < N; i++) {
  for (let j = 0; j < N; j++) {
    if (G[i][j] === 0) continue
    const ni = i + G[i][j]
    if (ni < N) {
      dp[ni][j] += BigInt(dp[i][j])
    }
    const nj = j + G[i][j]
    if (nj < N) {
      dp[i][nj] += BigInt(dp[i][j])
    }
  }
}
console.log(dp[N - 1][N - 1].toString())
