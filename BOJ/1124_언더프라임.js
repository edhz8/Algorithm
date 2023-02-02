const input = require("fs").readFileSync("../input.txt").toString().split(" ").map(Number)
let A = input.shift()
let B = input.shift()
const isPrime = Array(B + 1).fill(true)
isPrime[0] = isPrime[1] = false
let answer = 0
for (let i = 0; i < Math.sqrt(B) + 1; i++) {
  if (isPrime[i]) {
    for (let j = i * 2; j < B + 1; j += i) isPrime[j] = false
  }
}
const primes = []
for (let i = 0; i <= B; i++) {
  if (isPrime[i]) primes.push(i)
}
for (let i = Math.max(A, 2); i <= B; i++) {
  let count = 0
  let num = i
  for (const prime of primes) {
    while (num % prime == 0) {
      num /= prime
      count++
    }
  }
  if (isPrime[count]) {
    answer++
  }
}
console.log(answer)
