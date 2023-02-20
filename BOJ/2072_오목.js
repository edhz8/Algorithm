const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "../input.txt")
  .toString()
  .split("\n")
const N = Number(input.shift())
const G = Array.from(Array(19), () => Array(19).fill(0))
for (let i = 0; i < N; i++) {
  let [x, y] = input.shift().split(" ").map(Number)
  x--
  y--
  let cur = i % 2 == 0 ? "W" : "B"
  G[x][y] = cur
  let e = 0 //동
  while (y + e < 19 && G[x][y + e] == cur) e++
  let w = 0 //서
  while (y - w >= 0 && G[x][y - w] == cur) w++
  let n = 0 //북
  while (x - n >= 0 && G[x - n][y] == cur) n++
  let s = 0 //남
  while (x + s < 19 && G[x + s][y] == cur) s++
  let a = 0 //남동
  while (x + a < 19 && y + a < 19 && G[x + a][y + a] == cur) a++
  let b = 0 //북서
  while (x - b >= 0 && y - b >= 0 && G[x - b][y - b] == cur) b++
  let c = 0 //북동
  while (x - c >= 0 && y + c < 19 && G[x - c][y + c] == cur) c++
  let d = 0 //남서
  while (x + d < 19 && y - d >= 0 && G[x + d][y - d] == cur) d++

  if ((e + w - 1 == 5) | (n + s - 1 == 5) | (a + b - 1 == 5) | (c + d - 1 == 5)) {
    console.log(i + 1)
    process.exit(0)
  }
}
console.log(-1)
