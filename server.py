from flask import Flask,render_template,url_for, request, redirect
import csv
import os 
app = Flask(__name__)


@app.route('/') 
def start():
	return render_template ('index.html') 

	@app.route('/<string:page_name>') 
	def hmtl_page(page_name):
		return render_template (page_name) 

		def write_to_file(data):
			with open('database.txt','a') as database: 
				email= data['email']
				subject= data['subject']
		message= data['message'] #here I am extracting from a dictionary
		file = database.write(f'\n{email},{subject},{message}')

# def write_to_csv(data):
# 	file_exists = os.path.isfile("./database2.csv",)
# 	with open('database2.csv', newline="", mode='a') as database2: 
# 		email= data['email']
# 		subject= data['subject']
# 		message= data['message'] #here I am extracting from a dictionary
# 		name= data['name'] 
# 		# csv_writer = csv.writer(database2, delimiter = ',', quotechar='"', quoting =csv.QUOTE_MINIMAL )
# 		# csv_writer.writerow([email,subject,name,message])
# 		writer = csv.DictWriter(database2, fieldnames = ["email", "subject", "message","name"])
# 		if not file_exists:
# 			writer.writeheader()
# 		#writer.writerow({'email':email,'subject':subject,'name':name,'message':message})
# 		writer.writerow(data)


def write_to_csv(data):
	#file_exists = os.path.isfile("./database2.csv",)
	fileEmpty = os.stat("./database.csv").st_size == 0
	try:
		with open('database.csv', newline="", mode='a') as database2: 
			writer = csv.DictWriter(database2, fieldnames = ["email", "subject", "message","name"])
			if fileEmpty:
				writer.writeheader()
				writer.writerow(data)
			except OSError as err:
				print(f'something went wrong: {err}') 




@app.route('/submit_form', methods=['POST', 'GET']) # Here I am adding the methods and creating a new end point 
def submit_form():
	if request.method == 'POST':
		try:
			data = request.form.to_dict() 
			write_to_csv(data)
			return redirect('/thank_you.html')
		except :
			return 'did not save to database'


	else:
		return 'something went wrong'












