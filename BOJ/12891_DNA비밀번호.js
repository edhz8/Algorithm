const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "../input.txt")
  .toString()
  .split("\n")
let [S, P] = input.shift().split(" ").map(Number)
let DNA = input.shift()
let [na, nc, ng, nt] = input.shift().split(" ").map(Number)
let [ca, cc, cg, ct] = [0, 0, 0, 0]
let answer = 0
for (let i = 0; i < P; i++) {
  if (DNA[i] == "A") ca++
  if (DNA[i] == "C") cc++
  if (DNA[i] == "G") cg++
  if (DNA[i] == "T") ct++
}
if (na <= ca && nc <= cc && ng <= cg && nt <= ct) answer++
for (let i = P; i < S; i++) {
  if (DNA[i] == "A") ca++
  if (DNA[i] == "C") cc++
  if (DNA[i] == "G") cg++
  if (DNA[i] == "T") ct++
  if (DNA[i - P] == "A") ca--
  if (DNA[i - P] == "C") cc--
  if (DNA[i - P] == "G") cg--
  if (DNA[i - P] == "T") ct--
  if (na <= ca && nc <= cc && ng <= cg && nt <= ct) answer++
}
console.log(answer)
