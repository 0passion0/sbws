import requests
son=requests.session()
u='https://www.17k.com/ck/user/login'
'''a=input()
b=input()'''
d={
    'loginName':'13294759221',
    'password':'bTLG2002'
}
url=son.post(u,data=d)
url.encoding='utf-8'
sr=son.get('https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919')
print(sr.json())