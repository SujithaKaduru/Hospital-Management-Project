from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('appointment.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        # Retrieve form data
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        address = request.form['address']
        symptoms = request.form['symptoms']
        doctor_recommendation = request.form['doctor-recommendation']
        date = request.form['date']
        time = request.form['time']

        # Here you can process the form data, such as saving it to a database or sending it to an external service
        # For this example, let's just print the data
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Phone: {phone}")
        print(f"Address: {address}")
        print(f"Symptoms: {symptoms}")
        print(f"Doctor Recommendation: {doctor_recommendation}")
        print(f"Date: {date}")
        print(f"Time: {time}")

        return "Appointment successfully booked!"

if __name__ == '__main__':
    app.run(debug=True)
