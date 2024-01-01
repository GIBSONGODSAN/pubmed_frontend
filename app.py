from flask import Flask, render_template, request
import os
import json
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    try:
        # Read the scraped data directly from the output file
        scraped_data = []
        output_file = 'output.json'
        if os.path.exists(output_file):
            with open(output_file, 'r') as file:
                try:
                    scraped_data = json.load(file)
                except json.JSONDecodeError:
                    print("Error decoding JSON file or file is empty")

        return render_template('submit.html', scraped_data=scraped_data)
    except subprocess.CalledProcessError as e:
        return f"Error occurred"

if __name__ == '__main__':
    app.run(host='192.168.1.4', port=80, debug=True)
