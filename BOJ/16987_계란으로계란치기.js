const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "../input.txt")
  .toString()
  .split("\n")

const N = Number(input.shift())
const eggs = input.map((string) => string.split(" ").map(Number))
let answer = 0
const rec = (index, cnt) => {
  if (index == N) {
    answer = Math.max(answer, cnt)
    return
  }

  if (eggs[index][0] <= 0 || cnt === N - 1) {
    rec(index + 1, cnt)
    return
  }

  for (let i = 0; i < N; i++) {
    if (i == index || eggs[i][0] <= 0) continue
    eggs[i][0] -= eggs[index][1]
    eggs[index][0] -= eggs[i][1]
    rec(index + 1, cnt + Number(eggs[index][0] <= 0) + Number(eggs[i][0] <= 0))
    eggs[i][0] += eggs[index][1]
    eggs[index][0] += eggs[i][1]
  }
}
rec(0, 0)
console.log(answer)
