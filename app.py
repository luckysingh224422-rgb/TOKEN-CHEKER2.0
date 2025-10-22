from flask import Flask, request, render_template_string, jsonify
import requests
import os

app = Flask(__name__)

GRAPH_API_URL = "https://graph.facebook.com/v18.0"

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>AAHAN - Token Checker</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #0a0a15 0%, #1a1a2e 50%);
            color: white;
            margin: 0;
            padding: 20px;
            min-height: 100vh;
        }
        .container {
            max-width: 500px;
            margin: 0 auto;
            background: rgba(255,255,255,0.1);
            padding: 20px;
            border-radius: 10px;
            backdrop-filter: blur(10px);
        }
        .title {
            text-align: center;
            color: #ffd700;
            font-size: 32px;
            margin-bottom: 20px;
        }
        input[type="text"] {
            width: 100%;
            padding: 12px;
            margin: 10px 0;
            border: 1px solid #ffd700;
            border-radius: 5px;
            background: rgba(0,0,0,0.5);
            color: white;
        }
        button {
            width: 100%;
            padding: 12px;
            background: #ffd700;
            color: black;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-weight: bold;
        }
        .result-item {
            background: rgba(0,0,0,0.3);
            padding: 15px;
            margin: 10px 0;
            border-radius: 5px;
            border-left: 4px solid #ffd700;
        }
        .error {
            color: #ff4444;
            background: rgba(255,0,0,0.1);
            padding: 10px;
            border-radius: 5px;
            margin: 10px 0;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="title">👑 AAHAN 👑</div>
        <div style="text-align: center; margin-bottom: 20px;">ULTIMATE TOKEN CHECKER</div>
        
        <form method="POST">
            <input type="text" name="token" placeholder="Enter Facebook Access Token" required>
            <button type="submit">GET PAGE TOKENS</button>
        </form>

        {% if pages %}
            <div style="margin-top: 20px;">
                <h3>📄 FOUND PAGES:</h3>
                {% for page in pages %}
                    <div class="result-item">
                        <strong>{{ page.name }}</strong><br>
                        <small>Page ID: {{ page.id }}</small><br>
                        <code style="word-break: break-all; font-size: 12px;">{{ page.access_token }}</code>
                    </div>
                {% endfor %}
            </div>
        {% endif %}

        {% if error %}
            <div class="error">{{ error }}</div>
        {% endif %}

        <div style="margin-top: 20px; text-align: center; color: #ffd700;">
            THE UNSTOPPABLE LEGEND AAHAN HERE ❣️
        </div>
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        token = request.form.get('token')
        if not token:
            return render_template_string(HTML_TEMPLATE, error="Token is required")

        try:
            # First verify the token is valid
            verify_url = f"{GRAPH_API_URL}/me?access_token={token}"
            verify_res = requests.get(verify_url, timeout=10)
            
            if verify_res.status_code != 200:
                return render_template_string(HTML_TEMPLATE, error="Invalid token or network error")
            
            # Get pages
            url = f"{GRAPH_API_URL}/me/accounts?fields=name,id,access_token&access_token={token}"
            res = requests.get(url, timeout=30)
            data = res.json()

            if "data" in data and len(data["data"]) > 0:
                return render_template_string(HTML_TEMPLATE, pages=data["data"])
            else:
                error_msg = data.get("error", {}).get("message", "No pages found or invalid token permissions.")
                return render_template_string(HTML_TEMPLATE, error=error_msg)
                
        except requests.exceptions.Timeout:
            return render_template_string(HTML_TEMPLATE, error="Request timeout - try again")
        except requests.exceptions.ConnectionError:
            return render_template_string(HTML_TEMPLATE, error="Network connection error")
        except Exception as e:
            return render_template_string(HTML_TEMPLATE, error=f"Error: {str(e)}")

    return render_template_string(HTML_TEMPLATE)

@app.route('/health')
def health():
    return jsonify({"status": "healthy", "message": "AAHAN Token Checker is running"})

@app.route('/test')
def test():
    return "🚀 Server is working! AAHAN Token Checker is live."

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    print(f"🚀 Starting AAHAN Token Checker on port {port}...")
    app.run(host='0.0.0.0', port=port, debug=False)
