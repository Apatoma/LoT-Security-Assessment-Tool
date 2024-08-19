from flask import Flask, request, jsonify, render_template
from app import app
from app.scanner import IoTScanner

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        network_ip = request.form.get('network_ip')
        scanner = IoTScanner(network_ip)
        results = scanner.scan_network()
        return render_template('report.html', results=results)
    return render_template('index.html')
