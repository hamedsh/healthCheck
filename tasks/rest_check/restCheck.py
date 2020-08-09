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
        res_req = requests.request(method, url, body=body, timeout=timeout)
        load_time = round(time.perf_counter() - st)
        res_req.raise_for_status()
        res['result'] = res_req.content
    except requests.exceptions.Timeout as e:
        res['status'] = 408
        res['message'] = ERRORS[408]
    except requests.exceptions.BaseHTTPError as e:
        res['status'] = -1
        res['message'] = e.__str__()
    except (requests.ConnectionError, requests.exceptions.InvalidURL, requests.RequestException) as e:
        res['status'] = e.response.status_code
        res['message'] = e.__str__()
    except Exception as e:
        res['status'] = -2
        res['message'] = e.__str__()
    return res
