const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "../input.txt")
  .toString()
  .split("\n")
const N = input.shift()
const nums = input.shift().split(" ").map(Number)
const L = []
const bisect_left = (arr, num) => {
  let l = 0
  let r = arr.length - 1
  let mid
  while (l < r) {
    mid = parseInt((l + r) / 2)
    if (arr[mid] >= num) r = mid
    else l = mid + 1
  }
  return l
}
for (const n of nums) {
  if (L.length == 0 || L.at(-1) < n) L.push(n)
  else L[bisect_left(L, n)] = n
}
console.log(L.length)
