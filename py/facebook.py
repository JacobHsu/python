import lxml.etree
import lxml.html
import requests
import pyquery

def getFacebookWall():
    response = requests.get(
        'https://www.facebook.com/',
        headers={
            'Cookie': '<devtools / [network] clear [*] preserve log > Headers > cookie>'
        }
    )
    if response.status_code != 200:
        print('request error')
        return

    with open(f'facebook.html', 'wb') as f:
        # 對 HTML 進行格式化再輸出存檔
        html = response.text
        html = lxml.html.fromstring(html)
        html = lxml.etree.tostring(html, pretty_print=True)
        f.write(html)
    
    d = pyquery.PyQuery(response.text) # HTML轉DOM文件
    elems = d('div.hidden_elem > code') #d相當於jQuery $
    # 分析時，因無法短時間找出規則，先把各個註解部分輸出存檔
    for idx, elem in enumerate(elems.items()):
        elem_html = elem.html()[5:-4]
        elem_d = pyquery.PyQuery(elem_html)
        # 因為看套件庫程式碼回傳的是 list，所以之前寫 ... is None 的判斷是錯誤的，應該採用 len(...) == 0
        # https://github.com/gawel/pyquery/blob/master/pyquery/pyquery.py
        # line 
        if len(elem_d('div.userContentWrapper')) == 0:
            continue

        with open(f'facebook-{idx:>02}.html', 'wb') as f:
            # 對 HTML 進行格式化再輸出存檔
            elem_html = lxml.html.fromstring(elem_html)
            elem_html = lxml.etree.tostring(elem_html, pretty_print=True)
            f.write(elem_html)

        print('----------')

        # 發現發文人名存在於 h5 標籤下的 a 標籤內
        username = elem_d('h5 a').text()
        print(f'{username}:')
        # 發現文章內容存在於 div.userContent 標籤內
        content = elem_d('div.userContent').text()
        print(f'{content}')


if __name__ == '__main__':
    getFacebookWall()