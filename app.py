from flask import Flask, request, render_template #import main Flask class and request object
import csv
import os.path
from datetime import date, datetime

app = Flask(__name__) #create the Flask app

@app.route('/') 
def home():
    return render_template("home.html")

@app.route('/log')
def query_example():
    time = request.args.get('time') #if key doesn't exist, returns None
    temp = request.args.get('temp') #if key doesn't exist, returns None
    hum = request.args.get('hum') #if key doesn't exist, returns None

    filename = date.today().strftime("%m%d%Y")+'.csv'
    file_exists = os.path.isfile(filename)
    ts = str(int(datetime.now().timestamp()))

    with open (filename,'a') as filedata:
        header = ['time', 'temperature', 'humidity', 'timestamp']  
        writer = csv.DictWriter(filedata, delimiter=',', fieldnames=header)

        if not file_exists:
            writer.writeheader()  # file doesn't exist yet, write a header

        writer.writerow({'time': time, 'temperature': temp, 'humidity': hum, 'timestamp': ts}) 

    return '<h1>The values registered are the following: <br /><br />Time: '+time+'<br />Temperature: '+temp+'<br />Humidity: '+hum+'<br />Timestamp: '+ts+'</h1>'


if __name__ == '__main__':
    app.run(debug=True, port=5000) #run app in debug mode on port 5000