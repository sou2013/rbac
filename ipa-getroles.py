import requests
url="https://HOST/ipa/json"
headers = {'Connection': 'keep-alive',
'referer':'https://HOST/ipa',
'Content-Type':'application/json',
'Accept':'application/json'

}

data= {
    'subject': 'Alice-subject',
    'addbbcode18': '%23444444'
    }

cookies = {'ipa_session':'MagBearerToken=GH6LpfsQeZrM2v3k80p6RiLQccqsXba7Kt59s6o8lyOr3/uaT12wsvJ0ZYoL/D7r3AIBfZWNS0YeSzlzrClRS0kkiF3+XiZIJlcBvpxK6ePrY+junoWAgu3NDXvMtXDWf3ji9MYGbDId/tLbdRltxvO5LDCOfDsAPAXf64YdWK5h40gkV5IuGHp76FDfS5jjepRDv/8XwzINgBEhzdQeTe5CZLyS/YH2j/jdj0O5SqtHBHSTSdqNl874vrdxoSXCMj+DLho7qhQEeUsPPq7eeg=='
}
print requests.get(url, data=data, headers=headers, cookies=cookies).content
