# [세팅]
# 1. python을 설치한다.
# 2. 도스창에 pip install requests 입력하여 requests 라이브러리를 설치한다.
# 3. 도스창에 pip install beautifulsoup4 입력하여 설치한다.
# [사용법]
# 1. 1을 누르면 크롤링을 완료한다.
# 2. 2를 누르고 문제 번호를 입력하면 풀어도 되는 문제인지 알려준다.
# 단, 1은 맨 처음에만 실행하면 된다.
# 2를 누르기전에 1을 꼭 누르는것이 아닌, 프로그램 실행시 최초에만 1을 입력하여 크롤링을 해오자.


import requests
from bs4 import BeautifulSoup as bs
users = {
    '주영' : {
        'id' : '2weeks0',
        'solved' : [],

    },
    '예찬' : {
        'id' : 'dogcu',
        'solved' : [],

    },
    '규현' : {
        'id' : 'edhz8888',
        'solved' : [],

    },
    '봉민' : {
        'id' : 'nim924',
        'solved' : [],

    },
}
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
def init():
    for user in users.items():
        print(user[0],'의 정보 읽는중')
        page = requests.get('https://www.acmicpc.net/user/'+user[1]['id'],headers=headers)
        soup = bs(page.text,"html.parser")
        element = soup.find('div',{'class':'problem-list'})
        nums = element.select('a')
        for num in nums:
            users[user[0]]['solved'].append(num.text)
def find():
    num = input('찾을 문제 번호를 입력해주세요.')
    people = []
    for user in users.items():
        if num in user[1]['solved']: people.append(user[0])
    if people :
        print(people,'이 문제를 풀었습니다.')
    else : print('이 문제를 푼 사람은 없습니다.') 
while 1:
    cmd = input("정보를 가져오기 1, 문제 중복검사 2,종료는 3 입력하세요.")
    if cmd=='1' : init()
    elif cmd=='2' : find()
    elif cmd=='3' : exit(0)
