from mitmproxy import http

def response(flow: http.HTTPFlow) -> None:
	flow.response.replace("[tT]rump","Drumpf")
	flow.response.replace("江泽民","长者")
	flow.response.replace("Jiang Zemin","The Elder")
