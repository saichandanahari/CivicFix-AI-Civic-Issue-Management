from flask import Flask, render_template, request, redirect, url_for, jsonify
import sqlite3, os
from datetime import datetime
from ai_engine import analyze_with_ai

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
DB = 'civicfix.db'

def db():
    c = sqlite3.connect(DB); c.row_factory = sqlite3.Row; return c

def init_db():
    c = db()
    c.execute('''CREATE TABLE IF NOT EXISTS reports(
        id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, description TEXT,
        category TEXT, severity TEXT, safety_risk TEXT, department TEXT,
        summary TEXT, priority_reason TEXT, location TEXT, image TEXT,
        status TEXT DEFAULT 'Reported', created_at TEXT)''')
    c.commit(); c.close()

@app.route('/')
def home(): return render_template('index.html')

@app.route('/report', methods=['GET','POST'])
def report():
    if request.method == 'POST':
        name = request.form.get('name','Anonymous').strip() or 'Anonymous'
        description = request.form.get('description','').strip()
        location = request.form.get('location','').strip()
        image = request.files.get('image')
        if not description or not location:
            return render_template('report.html', error='Please enter description and location.')
        filename = None
        if image and image.filename:
            filename = datetime.now().strftime('%Y%m%d%H%M%S_') + image.filename.replace(' ','_')
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        result = analyze_with_ai(description, location)
        c = db()
        c.execute('''INSERT INTO reports
        (name,description,category,severity,safety_risk,department,summary,priority_reason,location,image,status,created_at)
        VALUES(?,?,?,?,?,?,?,?,?,?,?,?)''',
        (name,description,result['category'],result['severity'],result['safety_risk'],
         result['department'],result['summary'],result['priority_reason'],location,
         filename,'Reported',datetime.now().strftime('%Y-%m-%d %H:%M')))
        c.commit(); c.close()
        return redirect(url_for('success', category=result['category'], severity=result['severity'], source=result['source']))
    return render_template('report.html')

@app.route('/success')
def success():
    return render_template('success.html', category=request.args.get('category'), severity=request.args.get('severity'), source=request.args.get('source'))

@app.route('/dashboard')
def dashboard():
    c = db(); reports = c.execute('SELECT * FROM reports ORDER BY id DESC').fetchall(); c.close()
    return render_template('dashboard.html', reports=reports, total=len(reports),
        critical=sum(r['severity']=='High' for r in reports),
        active=sum(r['status'] in ('Assigned','In Progress') for r in reports),
        resolved=sum(r['status']=='Resolved' for r in reports))

@app.post('/api/status/<int:rid>')
def status(rid):
    s = request.get_json().get('status')
    if s not in ['Reported','Verified','Assigned','In Progress','Resolved']:
        return jsonify(error='Invalid status'), 400
    c = db(); c.execute('UPDATE reports SET status=? WHERE id=?',(s,rid)); c.commit(); c.close()
    return jsonify(success=True)

@app.get('/api/reports')
def reports_api():
    c=db(); data=[dict(x) for x in c.execute('SELECT * FROM reports ORDER BY id DESC')]; c.close(); return jsonify(data)

if __name__ == '__main__':
    init_db(); app.run(debug=True)
