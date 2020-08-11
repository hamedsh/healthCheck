from Task.rest_check.restCheck import call_api

res = call_api('http://127.0.0.1:8008/ok', 'POST', 5, {'num': 10})
if res['status'] == 0:
    print(f'------{res["result"]}')
else:
    print('error handling'+ str(res))
