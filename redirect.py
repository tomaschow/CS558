import mitmproxy
from mitmproxy import http


def request(flow:http.HTTPFlow) -> None:
	if "www.kittenwar.com" not in flow.request.url:
		flow.request.host = "kittenwar.com"
		flow.request.url = "http://www.kittenwar.com"
		flow.request.headers["Host"] = "kittenwar.com"
		flow.request.scheme = "http"
