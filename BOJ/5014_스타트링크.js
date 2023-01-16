let [F, S, G, U, D] = require("fs").readFileSync("dev/stdin").toString().split(" ").map(Number)
const q = [S]
const v = Array(F + 1).fill(-1)
v[S] = 0
let answer = "use the stairs"
while (q.length) {
  let cur = q.shift()
  if (cur === G) {
    answer = v[cur]
    break
  }
  for (let dir of [U, -D]) {
    let ncur = cur + dir
    if (0 < ncur && ncur <= F && v[ncur] === -1) {
      q.push(ncur)
      v[ncur] = v[cur] + 1
    }
  }
}
console.log(answer)
