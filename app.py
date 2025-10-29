from flask import Flask, request, render_template_string, jsonify
import requests
import os
import secrets

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(16)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

GRAPH_API_URL = "https://graph.facebook.com/v18.0"

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>👑 AAHAN - PAGE TOKEN CHECKER</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #0a0a15 0%, #1a1a2e 50%, #16213e 100%);
            color: white;
            min-height: 100vh;
            padding: 20px;
        }
        
        .container {
            max-width: 800px;
            margin: 0 auto;
        }
        
        .header {
            text-align: center;
            margin-bottom: 30px;
        }
        
        .title {
            font-size: 3em;
            color: #ffd700;
            margin-bottom: 10px;
            text-shadow: 0 0 20px #ffd700;
        }
        
        .subtitle {
            color: #00f3ff;
            font-size: 1.2em;
        }
        
        .option-buttons {
            display: flex;
            gap: 20px;
            margin-bottom: 30px;
            justify-content: center;
        }
        
        .option-btn {
            padding: 15px 30px;
            font-size: 1.1em;
            border: 2px solid #ffd700;
            background: rgba(255, 215, 0, 0.1);
            color: #ffd700;
            border-radius: 10px;
            cursor: pointer;
            transition: all 0.3s;
        }
        
        .option-btn.active {
            background: #ffd700;
            color: black;
        }
        
        .option-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(255, 215, 0, 0.3);
        }
        
        .content-box {
            background: rgba(255, 255, 255, 0.1);
            border: 2px solid #ffd700;
            border-radius: 15px;
            padding: 30px;
            margin-bottom: 20px;
            backdrop-filter: blur(10px);
        }
        
        .input-group {
            margin-bottom: 20px;
        }
        
        .input-label {
            display: block;
            color: #00f3ff;
            margin-bottom: 10px;
            font-size: 1.1em;
        }
        
        input[type="text"] {
            width: 100%;
            padding: 15px;
            border: 2px solid #00f3ff;
            border-radius: 8px;
            background: rgba(0, 0, 0, 0.5);
            color: white;
            font-size: 1em;
        }
        
        input[type="text"]:focus {
            border-color: #ffd700;
            outline: none;
            box-shadow: 0 0 10px #ffd700;
        }
        
        .file-upload-box {
            border: 3px dashed #00f3ff;
            border-radius: 10px;
            padding: 40px 20px;
            text-align: center;
            cursor: pointer;
            transition: all 0.3s;
            background: rgba(0, 243, 255, 0.05);
        }
        
        .file-upload-box:hover {
            border-color: #ffd700;
            background: rgba(255, 215, 0, 0.05);
        }
        
        .file-upload-box.dragover {
            border-color: #00ff88;
            background: rgba(0, 255, 136, 0.1);
        }
        
        .upload-icon {
            font-size: 3em;
            margin-bottom: 15px;
            color: #00f3ff;
        }
        
        .file-input {
            display: none;
        }
        
        .submit-btn {
            width: 100%;
            padding: 15px;
            background: #ffd700;
            color: black;
            border: none;
            border-radius: 8px;
            font-size: 1.2em;
            font-weight: bold;
            cursor: pointer;
            transition: all 0.3s;
            margin-top: 20px;
        }
        
        .submit-btn:hover {
            background: #ffed4a;
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(255, 215, 0, 0.4);
        }
        
        .file-info {
            margin-top: 15px;
            padding: 15px;
            background: rgba(0, 243, 255, 0.1);
            border-radius: 8px;
            border: 1px solid #00f3ff;
        }
        
        .stats {
            display: flex;
            justify-content: space-between;
            margin: 20px 0;
            padding: 20px;
            background: rgba(0, 0, 0, 0.3);
            border-radius: 10px;
            border: 1px solid #00f3ff;
        }
        
        .stat-item {
            text-align: center;
            flex: 1;
        }
        
        .stat-number {
            font-size: 2em;
            font-weight: bold;
            color: #ffd700;
        }
        
        .stat-label {
            color: #00f3ff;
            font-size: 0.9em;
        }
        
        .progress-bar {
            width: 100%;
            height: 10px;
            background: rgba(0, 0, 0, 0.3);
            border-radius: 5px;
            margin: 20px 0;
            overflow: hidden;
        }
        
        .progress-fill {
            height: 100%;
            background: linear-gradient(90deg, #00f3ff, #ffd700);
            width: 0%;
            transition: width 0.3s;
        }
        
        .result-item {
            background: rgba(0, 0, 0, 0.3);
            padding: 20px;
            margin: 15px 0;
            border-radius: 10px;
            border-left: 4px solid #ffd700;
        }
        
        .result-item.valid {
            border-left-color: #00ff88;
        }
        
        .result-item.invalid {
            border-left-color: #ff4444;
        }
        
        .token-status {
            display: inline-block;
            padding: 3px 10px;
            border-radius: 15px;
            font-size: 0.8em;
            font-weight: bold;
            margin-left: 10px;
        }
        
        .status-valid {
            background: #00ff88;
            color: black;
        }
        
        .status-invalid {
            background: #ff4444;
            color: white;
        }
        
        .error {
            background: rgba(255, 0, 0, 0.1);
            border: 1px solid #ff4444;
            color: #ff4444;
            padding: 15px;
            border-radius: 8px;
            margin: 15px 0;
            text-align: center;
        }
        
        .success {
            background: rgba(0, 255, 136, 0.1);
            border: 1px solid #00ff88;
            color: #00ff88;
            padding: 15px;
            border-radius: 8px;
            margin: 15px 0;
            text-align: center;
        }
        
        .loading {
            display: inline-block;
            width: 20px;
            height: 20px;
            border: 3px solid #f3f3f3;
            border-top: 3px solid #ffd700;
            border-radius: 50%;
            animation: spin 1s linear infinite;
            margin-right: 10px;
        }
        
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        
        .footer {
            text-align: center;
            margin-top: 30px;
            padding: 20px;
            background: rgba(255, 215, 0, 0.1);
            border-radius: 10px;
            border: 1px solid #ffd700;
            color: #ffd700;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <div class="title">👑 AAHAN 👑</div>
            <div class="subtitle">PAGE TOKEN CHECKER</div>
        </div>
        
        <div class="option-buttons">
            <button class="option-btn active" onclick="showSingleToken()">🔑 Single Token</button>
            <button class="option-btn" onclick="showFileUpload()">📁 TXT File Upload</button>
        </div>
        
        <!-- Single Token Option -->
        <div id="single-token" class="content-box">
            <form method="POST">
                <div class="input-group">
                    <label class="input-label">Enter Facebook Access Token:</label>
                    <input type="text" name="token" placeholder="EAABwzLixnjYBO... (paste your token here)" required>
                </div>
                <button type="submit" class="submit-btn">🚀 Get Page Tokens</button>
            </form>
        </div>
        
        <!-- File Upload Option -->
        <div id="file-upload" class="content-box" style="display: none;">
            <form method="POST" enctype="multipart/form-data">
                <div class="input-group">
                    <label class="input-label">Upload TXT File with Tokens:</label>
                    <div class="file-upload-box" id="uploadArea">
                        <div class="upload-icon">📁</div>
                        <h3>Click here or drag & drop TXT file</h3>
                        <p>File should contain one token per line</p>
                        <p style="color: #00f3ff; font-size: 0.9em; margin-top: 10px;">
                            Maximum file size: 16MB
                        </p>
                        <input type="file" id="fileInput" class="file-input" name="token_file" accept=".txt" required>
                    </div>
                </div>
                
                <div id="filePreview"></div>
                
                <button type="submit" class="submit-btn">⚡ Process Tokens from File</button>
            </form>
        </div>

        <!-- Results will appear here -->
        {% if pages %}
            <div class="content-box">
                <h3 style="color: #00ff88; text-align: center; margin-bottom: 20px;">✅ TOKENS FOUND</h3>
                {% for page in pages %}
                    <div class="result-item valid">
                        <strong style="color: #00f3ff; font-size: 1.1em;">
                            {{ page.name }} <span class="token-status status-valid">VALID</span>
                        </strong><br>
                        <div style="margin: 8px 0;">
                            <span style="color: #ffd700;">Page ID:</span> {{ page.id }}
                        </div>
                        <div style="background: rgba(0,0,0,0.5); padding: 10px; border-radius: 5px; margin-top: 8px;">
                            <span style="color: #ffd700;">Access Token:</span><br>
                            <code style="color: #00f3ff; word-break: break-all; font-size: 0.8em;">
                                {{ page.access_token }}
                            </code>
                        </div>
                    </div>
                {% endfor %}
            </div>
        {% endif %}

        {% if error %}
            <div class="error">
                ❌ {{ error }}
            </div>
        {% endif %}

        <div class="footer">
            🔥 THE UNSTOPPABLE LEGEND AAHAN HERE ❣️
        </div>
    </div>

    <script>
        function showSingleToken() {
            document.getElementById('single-token').style.display = 'block';
            document.getElementById('file-upload').style.display = 'none';
            document.querySelectorAll('.option-btn').forEach(btn => btn.classList.remove('active'));
            event.target.classList.add('active');
        }
        
        function showFileUpload() {
            document.getElementById('single-token').style.display = 'none';
            document.getElementById('file-upload').style.display = 'block';
            document.querySelectorAll('.option-btn').forEach(btn => btn.classList.remove('active'));
            event.target.classList.add('active');
        }
        
        // File upload handling
        const fileInput = document.getElementById('fileInput');
        const uploadArea = document.getElementById('uploadArea');
        
        fileInput.addEventListener('change', function(e) {
            if (this.files.length > 0) {
                handleFileSelect(this.files[0]);
            }
        });
        
        function handleFileSelect(file) {
            if (!file) return;
            
            // Check if file is TXT
            if (!file.name.toLowerCase().endsWith('.txt')) {
                alert('❌ Please select a .txt file only!');
                return;
            }
            
            // Check file size (16MB max)
            if (file.size > 16 * 1024 * 1024) {
                alert('❌ File is too large! Maximum 16MB allowed.');
                return;
            }
            
            const reader = new FileReader();
            
            reader.onload = function(e) {
                const content = e.target.result;
                const lines = content.split('\n');
                const tokens = lines.filter(line => line.trim().length > 0);
                
                if (tokens.length === 0) {
                    alert('❌ No tokens found in the file!');
                    return;
                }
                
                // Show file info
                const filePreview = document.getElementById('filePreview');
                filePreview.innerHTML = `
                    <div class="success">
                        ✅ <strong>${file.name}</strong> loaded successfully!<br>
                        📊 Found <strong>${tokens.length}</strong> tokens in file
                    </div>
                `;
            };
            
            reader.onerror = function() {
                alert('❌ Error reading file!');
            };
            
            reader.readAsText(file);
        }
        
        // Drag and drop functionality
        ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
            uploadArea.addEventListener(eventName, preventDefaults, false);
        });
        
        function preventDefaults(e) {
            e.preventDefault();
            e.stopPropagation();
        }
        
        ['dragenter', 'dragover'].forEach(eventName => {
            uploadArea.addEventListener(eventName, () => {
                uploadArea.classList.add('dragover');
            }, false);
        });
        
        ['dragleave', 'drop'].forEach(eventName => {
            uploadArea.addEventListener(eventName, () => {
                uploadArea.classList.remove('dragover');
            }, false);
        });
        
        uploadArea.addEventListener('drop', function(e) {
            const files = e.dataTransfer.files;
            if (files.length > 0) {
                fileInput.files = files;
                handleFileSelect(files[0]);
            }
        });
        
        // Click on upload area to trigger file input
        uploadArea.addEventListener('click', function() {
            fileInput.click();
        });
    </script>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Check if it's file upload
        if 'token_file' in request.files:
            file = request.files['token_file']
            
            if file.filename == '':
                return render_template_string(HTML_TEMPLATE, error="❌ Please select a file!")
            
            if not file.filename.lower().endswith('.txt'):
                return render_template_string(HTML_TEMPLATE, error="❌ Only .txt files are allowed!")
            
            try:
                # Read the file
                content = file.read().decode('utf-8')
                tokens = [token.strip() for token in content.split('\n') if token.strip()]
                
                if not tokens:
                    return render_template_string(HTML_TEMPLATE, error="❌ No tokens found in the file!")
                
                # Process all tokens and collect results
                all_pages = []
                valid_count = 0
                
                for token in tokens:
                    try:
                        # Verify token
                        verify_url = f"{GRAPH_API_URL}/me?access_token={token}"
                        verify_res = requests.get(verify_url, timeout=10)
                        
                        if verify_res.status_code == 200:
                            # Get pages for this token
                            pages_url = f"{GRAPH_API_URL}/me/accounts?fields=name,id,access_token&access_token={token}"
                            pages_res = requests.get(pages_url, timeout=15)
                            pages_data = pages_res.json()
                            
                            if "data" in pages_data:
                                for page in pages_data["data"]:
                                    all_pages.append(page)
                                valid_count += 1
                                
                    except Exception as e:
                        # Skip invalid tokens
                        continue
                
                if all_pages:
                    return render_template_string(HTML_TEMPLATE, pages=all_pages)
                else:
                    return render_template_string(HTML_TEMPLATE, error=f"❌ No valid pages found! Checked {len(tokens)} tokens, {valid_count} were valid but had no pages.")
                    
            except Exception as e:
                return render_template_string(HTML_TEMPLATE, error=f"❌ Error processing file: {str(e)}")
        
        else:
            # Single token processing
            token = request.form.get('token')
            if not token:
                return render_template_string(HTML_TEMPLATE, error="❌ Token is required!")

            try:
                # Verify token
                verify_url = f"{GRAPH_API_URL}/me?access_token={token}"
                verify_res = requests.get(verify_url, timeout=10)
                
                if verify_res.status_code != 200:
                    return render_template_string(HTML_TEMPLATE, error="❌ Invalid token!")
                
                # Get pages
                url = f"{GRAPH_API_URL}/me/accounts?fields=name,id,access_token&access_token={token}"
                res = requests.get(url, timeout=30)
                data = res.json()

                if "data" in data and len(data["data"]) > 0:
                    return render_template_string(HTML_TEMPLATE, pages=data["data"])
                else:
                    return render_template_string(HTML_TEMPLATE, error="❌ No pages found for this token!")
                    
            except requests.exceptions.Timeout:
                return render_template_string(HTML_TEMPLATE, error="❌ Request timeout! Try again.")
            except requests.exceptions.ConnectionError:
                return render_template_string(HTML_TEMPLATE, error="❌ Network error! Check your connection.")
            except Exception as e:
                return render_template_string(HTML_TEMPLATE, error=f"❌ Error: {str(e)}")

    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    print(f"🚀 AAHAN Token Master starting on port {port}...")
    app.run(host='0.0.0.0', port=port, debug=False)
