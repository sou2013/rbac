curl -v -H referer:https://HOST/ipa -H "Content-Type:application/json" -H "Accept:application/json" \
--negotiate -u : --cacert /etc/ipa/ca.crt -d '{"jsonrpc": "2.0", "method":"user_show","params":[["testoperator"],{"all": true,"version": "2.215"}],"id":0}' \
-X POST https://HOST/ipa/json

