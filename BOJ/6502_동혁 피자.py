cnt = 0
while True:
    a = input()
    cnt += 1
    if a[0] == "0":
        break
    r, w, l = map(int,a.split())
    if 4 * (r ** 2) >= (w ** 2) + (l ** 2):
        print("Pizza %d fits on the table."%cnt)
    else:
        print("Pizza %d does not fit on the table."%cnt)