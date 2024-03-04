from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Bengaluru, India',
        'salary': 'Rs. 10,00,000'
    },
    {
        'id': 2,
        'title': 'Data Scienist',
        'location': 'Dehli, India',
        'salary': 'Rs. 15,00,000'
    },
    {
        'id': 3,
        'title': 'Frontend Engineer',
        'location': 'New Yourk, USA'
    },
    {
        'id': 2,
        'title': 'Backend Engineer',
        'location': 'LA, USA',
        'salary': 'Rs. 25,00,000'
    },
]


@app.route('/')
def hello_world():
  return render_template('home.html', companyName='HYUNDAI', jobs=JOBS)


if (__name__ == '__main__'):
  app.run(host='0.0.0.0', debug=True)

  #finished on 1.23.27
