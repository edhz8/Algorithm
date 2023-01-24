const input = require("fs").readFileSync("../input.txt").toString().split("\n")
let [M, N] = input.shift().split(" ").map(Number)
var G = []
for (let i = 0; i < M; i++) {
  G.push([...input.shift()].map(Number))
}
var D = [
  [-1, 0],
  [0, 1],
  [1, 0],
  [0, -1],
]
const dfs = (x, y) => {
  if (x === M - 1) {
    console.log("YES")
    process.exit(0)
  }
  for (let [dx, dy] of D) {
    const [nx, ny] = [x + dx, y + dy]
    if (0 <= nx && nx < M && 0 <= ny && ny < N && G[nx][ny] === 0) {
      G[nx][ny] = 1
      dfs(nx, ny)
    }
  }
}
for (let i = 0; i < N; i++) {
  if (G[0][i] === 0) {
    dfs(0, i)
  }
}
console.log("NO")
