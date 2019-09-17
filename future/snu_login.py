import requests
from getpass import getpass

ADDRESS = "https://sso.snu.ac.kr/snu/ssologin_proc.jsp?si_redirect_address=https://my.snu.ac.kr/user/loginProcess.face?langKnd=en"
# ADDRESS = "https://sso.snu.ac.kr/safeidentity/modules/auth_idpwd"
ADDRESS = "https://my.snu.ac.kr/user/loginProcess.face?langKnd=en"
payload = {}

with requests.Session() as s:
    while True:  # try login
        username = input('id: ')
        password = getpass('password: ')
        try:
            s.get(ADDRESS) #download csrftoken
            csrftoken = s.cookies['csrftoken']
            payload['csrfmiddlewaretoken'] = csrftoken
        except:
            pass
        payload['userId'] = username
        payload['si_id'] = username
        payload['si_pwd'] = password
        payload["username"] = username
        payload['password'] = password

        # ret = s.post(ADDRESS, data=payload)
        r = s.post(ADDRESS, data=payload)
        r.encoding='utf-8-sig'
        print(r.status_code)
        print(r.text)
