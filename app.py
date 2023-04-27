from flask import Flask, render_template

app = Flask(__name__)

all_jobs = [{
  'id': 1,
  'post': 'Data Analysis',
  'salary': 1000,
  'location': 'HQ'
}, {
  'id': 2,
  'post': 'Data Scientist',
  'salary': 1100,
  'location': 'Mirpur'
}, {
  'id': 3,
  'post': 'Frontend Eng',
  'salary': 1300,
  'location': 'Dhaka'
}, {
  'id': 4,
  'post': 'Backend Eng',
  'salary': 1400,
  'location': 'Khula'
}]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=all_jobs)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
