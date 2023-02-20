const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "../input.txt")
  .toString()
  .split("\n")
let [A, B, C] = input.shift().split(" ").map(Number)
const v = Array.from(Array(A + 1), () => Array.from(Array(B + 1), () => Array(C + 1).fill(0)))
const answer = Array(C + 1).fill(-1)
const dfs = (a, b, c) => {
  v[a][b][c] = true
  if (a === 0) {
    answer[c] = c
  }
  let t = Math.min(a, B - b)
  if (!v[a - t][b + t][c]) dfs(a - t, b + t, c)
  t = Math.min(a, C - c)
  if (!v[a - t][b][c + t]) dfs(a - t, b, c + t)
  t = Math.min(b, A - a)
  if (!v[a + t][b - t][c]) dfs(a + t, b - t, c)
  t = Math.min(b, C - c)
  if (!v[a][b - t][c + t]) dfs(a, b - t, c + t)
  t = Math.min(c, A - a)
  if (!v[a + t][b][c - t]) dfs(a + t, b, c - t)
  t = Math.min(c, B - b)
  if (!v[a][b + t][c - t]) dfs(a, b + t, c - t)
}
dfs(0, 0, C)

console.log(answer.filter((e) => e > -1).join(" "))
