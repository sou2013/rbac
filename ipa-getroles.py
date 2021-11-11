import requests
import json

url="https://ipa.rhel7.local/ipa/json"
headers = {'Connection': 'keep-alive',
'referer':'https://ipa.rhel7.local/ipa',
'Content-Type':'application/json',
'Accept':'application/json'

}

data= {
"jsonrpc": "2.0", "method":"user_show","params":[["tester1"],{"all": "true","version": "2.215"}],"id":0
}

# cookie is from browser after login using user/pswd on web GUI

cookies = {'ipa_session':'MagBearerToken=UnLlaG6tGBt1zkimE%2bENc39QQ5MzsGQhUDDkDQD6e69UCx%2bSPpx5NboOiNF7V0IzuGrMH1pttKukbmS8kA%2fP6lIFHMjCu3GmjdTlE$
}
print requests.post(url, data=json.dumps(data), headers=headers, cookies=cookies).content
