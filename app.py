from flask import Flask, render_template, request, jsonify
import json
import uuid
import os
from datetime import datetime

app = Flask(__name__)
DATA_FILE = 'forms_data.json'

def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            content = f.read().strip()
            if not content: return {}
            data = json.loads(content)
            return data if isinstance(data, dict) else {}
    except Exception:
        return {}

def save_data(data):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

@app.route('/')
def dashboard():
    forms = load_data()
    return render_template('dashboard.html', forms=forms)

@app.route('/builder')
def builder():
    return render_template('index.html')

@app.route('/save', methods=['POST'])
def save_form():
    form_data = request.json
    forms = load_data()
    form_id = str(uuid.uuid4())[:8]
    
    forms[form_id] = {
        "name": form_data.get('name', 'Untitled Form'),
        "fields": form_data.get('fields', []),
        "created_at": datetime.now().strftime("%b %d, %Y")
    }
    
    save_data(forms)
    return jsonify({"success": True, "id": form_id})

@app.route('/delete/<form_id>', methods=['DELETE'])
def delete_form(form_id):
    forms = load_data()
    if form_id in forms:
        del forms[form_id]
        save_data(forms)
        return jsonify({"success": True})
    return jsonify({"success": False}), 404

@app.route('/view/<form_id>')
def view_form(form_id):
    forms = load_data()
    form = forms.get(form_id)
    if not form: return "Form not found", 404
    # Ensure variables match fill_form.html
    return render_template('fill_form.html', schema=form['fields'], name=form['name'])

if __name__ == '__main__':
    app.run(debug=True, port=5000)