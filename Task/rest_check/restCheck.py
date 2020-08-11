import requests
import time

ERRORS = {
    408: "timeout exception",
    -1: "base http error",
    -2: "unknown error",
}


def call_api(url: str, method: str, timeout, body: object = None):
    res = {'status': 0, 'message': '', 'result': None}
    method = method.upper()
    try:
        st = time.perf_counter()
        res_req = requests.request(method, url, json=body, timeout=timeout)
        load_time = round(time.perf_counter() - st)
        res_req.raise_for_status()
        res['result'] = res_req.content
    except requests.exceptions.HTTPError as errh:
        res['status'] = -1
        res['message'] = "An Http Error occurred:" + repr(errh)
    except requests.exceptions.ConnectionError as errc:
        res['status'] = -2
        res['message'] = "An Error Connecting to the API occurred:" + repr(errc)
    except requests.exceptions.Timeout as errt:
        res['status'] = -2
        res['message'] = "A Timeout Error occurred:" + repr(errt)
    except requests.exceptions.RequestException as err:
        res['status'] = -2
        res['message'] = "An Unknown Error occurred" + repr(err)
    except Exception as e:
        res['status'] = -2
        res['message'] = e.__str__()
    return res
