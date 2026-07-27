from flask import Flask, request, jsonify, render_template
from auditor import audit_page

# Initializing the Flask apapp
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
# API endpoint
@app.route('/api/audit', methods=['GET'])
def audit_endpoint():
    
    target_url = request.args.get('url')
    
    if not target_url:
        return jsonify({"error": "Please provide a URL to audit."}), 400
    
    # Auditing function
    result = audit_page(target_url)
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)