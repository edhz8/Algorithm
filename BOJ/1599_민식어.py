d={
    'a':'a',
    'b':'b',
    'k':'c',
    'd':'d',
    'e':'e',
    'g':'f',
    'h':'g',
    'i':'h',
    'l':'i',
    'm':'j',
    'n':'k',
    'N':'l',
    'o':'m',
    'p':'n',
    'r':'o',
    's':'p',
    't':'q',
    'u':'r',
    'w':'s',
    'y':'t'
    }
words = [input() for _ in range(int(input()))]
def convert(w): return ''.join(d[c] for c in w)
for n,w in sorted({convert(word.replace('ng','N')) : word for word in words}.items()) : print(w)