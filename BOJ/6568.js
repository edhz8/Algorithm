const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "../input.txt")
  .toString()
  .split("\n")
  .map((e) => parseInt(e, 2))

while (input.length) {
  const memory = input.splice(0, 32)
  let adder = 0
  let pc = 0
  let NOT_END = true
  while (NOT_END) {
    let address = memory[pc]
    let cmd = Math.floor(address / 32)
    let x = address % 32
    pc = (pc + 1) % 32
    console.log(pc, adder, memory[pc], cmd, x)
    switch (cmd) {
      case 0:
        memory[x] = adder
        break
      case 1:
        adder = memory[x]
        break
      case 2:
        if (adder === 0) pc = x
        break
      case 3:
        break
      case 4:
        adder = adder > 0 ? adder - 1 : 255
        break
      case 5:
        adder = (adder + 1) % 256
        break
      case 6:
        pc = x
        break
      default:
        NOT_END = false
        break
    }
  }
  console.log(adder.toString(2).padStart(8, "0"))
}
