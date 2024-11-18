from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# MySQL Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://aman:test%401234@staging-form-db.cxy0qeyi820l.us-east-1.rds.amazonaws.com:3306/flask_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class BioData(db.Model):
    __tablename__ = 'bio_data'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    department = db.Column(db.String(255), nullable=False)
    employee_id = db.Column(db.String(255), nullable=False)
    company_name = db.Column(db.String(255), nullable=False)
    designation = db.Column(db.String(255), nullable=False)
    contact_no = db.Column(db.String(255), nullable=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        try:
            # Extract form data
            name = request.form['name']
            department = request.form['department']
            employee_id = request.form['employee_id']
            company_name = request.form['company_name']
            designation = request.form['designation']
            contact_no = request.form['contact_no']
            
            # Create a new BioData record
            new_bio = BioData(
                name=name, 
                department=department, 
                employee_id=employee_id, 
                company_name=company_name,
                designation=designation, 
                contact_no=contact_no
            )
            
            # Add and commit to the database
            db.session.add(new_bio)
            db.session.commit()
            
            return redirect(url_for('success'))
        except Exception as e:
            return f"An error occurred: {str(e)}"

@app.route('/success')
def success():
    return "Data submitted successfully!"

if __name__ == '__main__':
    app.run(debug=True)

