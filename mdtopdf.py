import requests
import json

def load_md(name):
 	
 	#open and read the file
 	f = open(name + ".md", "r")
 	temp = f.read()
 	
 	# return
 	return temp
 
def save_to_pdf(bytes, filename):
	
	# open file to overwrite content in bytes
	f = open(filename + ".pdf", "wb")
	f.write(bytes)
	f.close()
 
def pdf(md):
 	
 	# prepare
	url = "https://md-to-pdf.fly.dev"
	data = { "markdown" : md, "css" : ""}
	
	# send request
	r = requests.post(url, data=data)
	print(r.status_code)
	
	# return
	if r.status_code == 200:
		return r.content
	else:
	    return "error"

md = load("<your md filename>")
pdf = pdf(md)
save_to_pdf(pdf, "<your pdf filename>")