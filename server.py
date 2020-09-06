from flask import Flask, render_template, url_for, request
import csv
app = Flask(__name__)


@app.route('/')
def my_root(username=None, post_id=None):
    return render_template('index.html')

@app.route('/<string:page_name>')
def my_html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a') as f:
        email = data['email']
        subject = data['subject']
        message = data['message']
        f.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as csv_data:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(csv_data, delimiter=',', quotechar="|",  quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return render_template('thankyou.html')
        except:
            return 'did not go well!!!!!!'
    else:
        return 'Something went wrong'
