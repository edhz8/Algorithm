const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "../input.txt")
  .toString()
  .split("\n")
const [N, M] = input.shift().split(" ").map(Number)
const rs = []
for (let i = 0; i < N; i++) rs[i + 1] = Number(input.shift())
const wk = []
for (let i = 0; i < M; i++) wk[i + 1] = Number(input.shift())
const pl = Array(N + 1).fill(0)
let answer = 0
const q = []
for (let i = 0; i < 2 * M; i++) {
  const num = Number(input.shift())
  if (num < 0) {
    const index = pl.findIndex((e) => e === -num)
    answer += rs[index] * wk[-num]
    pl[index] = 0
  } else {
    q.push(num)
  }
  if (q.length > 0) {
    for (let index = 1; index <= N; index++) {
      if (pl[index] == 0) {
        pl[index] = q.shift()
        break
      }
    }
  }
}
console.log(answer)
