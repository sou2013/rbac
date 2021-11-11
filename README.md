# rbac
maskedhiq_1234o1WUfdFmPeXikyfK2sUlNktJ8Mr1dx2cSA1V


/// create client cert for ipa server
https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/configuring_and_managing_identity_management/dc-web-ui-auth_configuring-and-managing-idm#requesting-and-exporting-a-user-certificate_dc-web-ui-auth

cd /home/stan/workspace/rbac
certutil -R -d certdb -a -g 4096 -n idm_user -s 'CN=idm_user,O=RHEL7.LOCAL' > certificate_request.csr   <-- create cert request. uses temp db, cert will be in ipa server by next step
sudo ipa cert-request certificate_request.csr --principal=idm_user@RHEL7.LOCAL --profile-id=IECUserRoles --certificate-out=./idm_user.pem
certutil -A -d certdb -n idm_user -t "P,," -i ./idm_user.pem
pk12util -d certdb -o ./idm_user.p12 -n idm_user    <-- exports cert from db to p12

/// json-rpc against ipa server

export COOKIEJAR=./mycookie.txt

curl -v  \
-H Referer:https://ipa.rhel7.local/ipa  \
-H "Content-Type:application/x-www-form-urlencoded" \
-H "Accept:text/plain" \
-c $COOKIEJAR -b $COOKIEJAR \
--cacert /etc/ipa/ca.crt  \
--data "user=admin&password=******" \
-X POST \
https://ipa.rhel7.local/ipa/session/login_password

curl -v -H referer:https://ipa.rhel7.local/ipa -H "Content-Type:application/json" -H "Accept:application/json" \
--negotiate -u : --cacert /etc/ipa/ca.crt -d '{"jsonrpc": "2.0", "method":"user_show","params":[["admin"],{"all": true,"version": "2.215"}],"id":0}' \
-c $COOKIEJAR -b $COOKIEJAR \
-X POST https://ipa.rhel7.local/ipa/json
