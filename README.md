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
