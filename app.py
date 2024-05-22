from flask import request, render_template, redirect, url_for
from init import app, mongo, q
from tasks import count_words_at_url

@app.route('/')
def index():
    results = mongo.db.results.find()
    print(results)
    return render_template('index.html', results=results)

@app.route('/submit', methods=['POST'])
def submit():
    url = request.form['url']
    job = q.enqueue(count_words_at_url, url)
    mongo.db.jobs.insert_one({'job_id': job.id, 'url': url})
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
