# python

[Code With Mu](https://codewith.mu/): a simple Python editor for beginner programmers.

[python downloads](https://www.python.org/downloads/)  
Python 3.6 開始才提供一種很有效率的格式化字串輸出功能（`f-string`） 

## f-string

最早的格式化是用%(百分號), 它這麼用：

```py
In : name = 'python'

In : 'Hello %s' % name
Out: 'Hello python'
```

%符號前面使用一個字符串作為模板，模板中有標記格式的佔位符號。佔位符控制著顯示的格式，這裡用的%s表示格式化成字符串，另外常用的是%d(十進制整數)、%f(浮點數)。

當要格式化的參數很多時，可讀性很差，還容易出錯（數錯佔位符的數量），也不靈活，舉個例子，name這個變量要在格式化時用2次，就要傳入2次。

Python 3.6新增了f-strings，這個特性叫做字面量格式化字符串，F字符串是開頭有一個f的字符串文字，Python會計算其中的用大括號包起來的表達式，並將計算後的值替換進去。

```py
In : name = 'python'

In : f'Hello {name}'
Out: 'Hello python'
```

```py
In : id = 123
In : name = 'python'

In : 'User[%s]: %s' % (id, name)
Out: 'User[123]: python'
```

```py
In : f'User[{d["id"]}]: {d["name"]}'
Out: 'User[123]: python'
```

## for in

list creation from for loop `for in `  

```py
stocks = [{
    'name': '2412',
    'close': 106
}, {
    'name': '2303',
    'close': 15
}]
print([
    stock['name']
    for stock in stocks
    if stock['close'] > 100
]) # ['2412']
```

## json

```py
import json

s = '{"name":"jacob"}'

d = json.loads(s)
print(d['name']) #jacob

d = [{
    'name': 'hsu'
}]
print(json.dumps(d)) #[{"name": "hsu"}]
```

## url

https://repl.it/languages/python3

```py
import urllib.parse as up

url = 'https://24h.pchome.com.tw/prod/DYAJFQ-1900A9TCG'
result = up.urlparse(url)
print(result)
print(result.path.split('/')[-1]) #DYAJFQ-1900A9TCG
```

ParseResult(scheme='https', netloc='24h.pchome.com.tw', path='/prod/DYAJFQ-1900A9TCG', params='', query='', fragment='')

## requests 

```py
import requests
import urllib.parse as up

import chardet

def search(word):
    word = up.quote(word)
    url = f'https://www.google.com/search?q={word}'

    response = requests.get(
        url,
        headers={
            'Cookie': '<請自行從瀏覽器取得'
        }
    )

    if response.status_code != 200:
        print('request error')
        return

    with open('google.html','wb') as f:
        f.write(response.content)

    print(response.text)

    print(chardet.detect(response.content)) # {'encoding':'Big5', 'confidence':0.99, 'language':'Chinese'}

if __main__ == '__main__':
    search('vti')
```
