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
    <title>👑 AAHAN - ULTIMATE TOKEN MASTER</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Rajdhani:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --neon-gold: #ffd700;
            --neon-cyan: #00f3ff;
            --neon-pink: #ff00ff;
            --neon-green: #00ff88;
            --neon-purple: #9d00ff;
            --dark-bg: #0a0a15;
        }
        
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Rajdhani', sans-serif;
            background: linear-gradient(135deg, #0a0a15 0%, #1a1a2e 50%, #16213e 100%);
            color: white;
            min-height: 100vh;
            overflow-x: hidden;
        }
        
        .scan-line {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 3px;
            background: linear-gradient(90deg, transparent, var(--neon-gold), var(--neon-cyan), transparent);
            animation: scan 3s linear infinite;
            z-index: 1000;
            box-shadow: 0 0 20px var(--neon-gold);
        }
        
        @keyframes scan {
            0% { top: 0%; }
            100% { top: 100%; }
        }
        
        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 30px 20px;
            position: relative;
        }
        
        .header {
            text-align: center;
            margin-bottom: 40px;
            position: relative;
        }
        
        .title {
            font-family: 'Orbitron', sans-serif;
            font-size: 3.5em;
            font-weight: 900;
            background: linear-gradient(45deg, var(--neon-gold), var(--neon-cyan), var(--neon-pink));
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
            text-shadow: 0 0 30px rgba(255, 215, 0, 0.5);
            margin-bottom: 10px;
            animation: titleGlow 2s ease-in-out infinite alternate;
        }
        
        @keyframes titleGlow {
            from { text-shadow: 0 0 20px rgba(255, 215, 0, 0.7); }
            to { text-shadow: 0 0 40px rgba(255, 215, 0, 0.9), 0 0 60px rgba(0, 243, 255, 0.6); }
        }
        
        .subtitle {
            font-size: 1.2em;
            color: var(--neon-cyan);
            margin-bottom: 10px;
            font-weight: 600;
            letter-spacing: 2px;
        }
        
        .mode-selector {
            display: flex;
            justify-content: center;
            gap: 20px;
            margin-bottom: 40px;
        }
        
        .mode-btn {
            padding: 20px 40px;
            font-size: 1.2em;
            font-weight: 700;
            border: 2px solid var(--neon-gold);
            background: rgba(255, 215, 0, 0.1);
            color: var(--neon-gold);
            border-radius: 15px;
            cursor: pointer;
            transition: all 0.3s ease;
            font-family: 'Orbitron', sans-serif;
            letter-spacing: 1px;
            position: relative;
            overflow: hidden;
        }
        
        .mode-btn:hover {
            background: rgba(255, 215, 0, 0.2);
            transform: translateY(-5px);
            box-shadow: 0 10px 25px rgba(255, 215, 0, 0.3);
        }
        
        .mode-btn.active {
            background: linear-gradient(45deg, var(--neon-gold), var(--neon-orange));
            color: black;
            border-color: transparent;
            box-shadow: 0 0 30px rgba(255, 215, 0, 0.5);
        }
        
        .content-area {
            background: rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(15px);
            border: 1px solid rgba(255, 215, 0, 0.3);
            border-radius: 20px;
            padding: 40px;
            margin-bottom: 30px;
            box-shadow: 0 0 50px rgba(255, 215, 0, 0.1);
            position: relative;
            overflow: hidden;
        }
        
        .content-area::before {
            content: '';
            position: absolute;
            top: -2px;
            left: -2px;
            right: -2px;
            bottom: -2px;
            background: linear-gradient(45deg, var(--neon-gold), var(--neon-cyan), var(--neon-pink), var(--neon-purple));
            border-radius: 22px;
            z-index: -1;
            animation: borderGlow 4s linear infinite;
            background-size: 400% 400%;
        }
        
        @keyframes borderGlow {
            0% { background-position: 0% 50%; filter: hue-rotate(0deg); }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; filter: hue-rotate(360deg); }
        }
        
        .mode-content {
            display: none;
            animation: fadeIn 0.5s ease;
        }
        
        .mode-content.active {
            display: block;
        }
        
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        .input-group {
            margin-bottom: 25px;
        }
        
        .input-label {
            display: block;
            color: var(--neon-cyan);
            margin-bottom: 10px;
            font-weight: 600;
            font-size: 1.1em;
        }
        
        input[type="text"] {
            width: 100%;
            padding: 18px 20px;
            border: 2px solid var(--neon-cyan);
            border-radius: 12px;
            background: rgba(0, 0, 0, 0.6);
            color: white;
            font-size: 1.1em;
            font-family: 'Rajdhani', sans-serif;
            transition: all 0.3s ease;
            outline: none;
        }
        
        input[type="text"]:focus {
            border-color: var(--neon-gold);
            box-shadow: 0 0 25px rgba(255, 215, 0, 0.4);
            background: rgba(0, 0, 0, 0.8);
        }
        
        .file-upload-area {
            border: 3px dashed var(--neon-cyan);
            border-radius: 15px;
            padding: 50px 30px;
            text-align: center;
            cursor: pointer;
            transition: all 0.3s ease;
            background: rgba(0, 243, 255, 0.05);
            position: relative;
            overflow: hidden;
        }
        
        .file-upload-area:hover {
            border-color: var(--neon-gold);
            background: rgba(255, 215, 0, 0.05);
            transform: translateY(-5px);
        }
        
        .file-upload-area.dragover {
            border-color: var(--neon-green);
            background: rgba(0, 255, 136, 0.1);
            box-shadow: 0 0 30px rgba(0, 255, 136, 0.3);
        }
        
        .upload-icon {
            font-size: 4em;
            margin-bottom: 20px;
            color: var(--neon-cyan);
        }
        
        .file-input {
            position: absolute;
            width: 100%;
            height: 100%;
            top: 0;
            left: 0;
            opacity: 0;
            cursor: pointer;
        }
        
        .submit-btn {
            width: 100%;
            padding: 20px;
            background: linear-gradient(45deg, var(--neon-gold), var(--neon-orange));
            color: black;
            border: none;
            border-radius: 12px;
            font-size: 1.3em;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.3s ease;
            font-family: 'Orbitron', sans-serif;
            letter-spacing: 2px;
            text-transform: uppercase;
            position: relative;
            overflow: hidden;
        }
        
        .submit-btn:hover {
            transform: translateY(-3px);
            box-shadow: 0 15px 35px rgba(255, 215, 0, 0.4);
        }
        
        .submit-btn:disabled {
            background: #666;
            cursor: not-allowed;
            transform: none;
            box-shadow: none;
        }
        
        .stats-container {
            display: flex;
            justify-content: space-between;
            margin: 30px 0;
            padding: 25px;
            background: rgba(0, 0, 0, 0.4);
            border-radius: 15px;
            border: 1px solid var(--neon-cyan);
        }
        
        .stat-item {
            text-align: center;
            flex: 1;
        }
        
        .stat-number {
            font-size: 2.5em;
            font-weight: 900;
            color: var(--neon-gold);
            font-family: 'Orbitron', sans-serif;
            text-shadow: 0 0 10px rgba(255, 215, 0, 0.5);
        }
        
        .stat-label {
            font-size: 1em;
            color: var(--neon-cyan);
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        
        .progress-container {
            margin: 25px 0;
        }
        
        .progress-bar {
            width: 100%;
            height: 12px;
            background: rgba(0, 0, 0, 0.4);
            border-radius: 10px;
            overflow: hidden;
            border: 1px solid var(--neon-cyan);
        }
        
        .progress-fill {
            height: 100%;
            background: linear-gradient(90deg, var(--neon-cyan), var(--neon-gold), var(--neon-pink));
            transition: width 0.3s ease;
            width: 0%;
        }
        
        .result-item {
            background: rgba(0, 0, 0, 0.4);
            padding: 25px;
            margin: 20px 0;
            border-radius: 15px;
            border-left: 5px solid var(--neon-gold);
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }
        
        .result-item:hover {
            transform: translateX(10px);
            box-shadow: 0 10px 25px rgba(255, 215, 0, 0.2);
        }
        
        .result-item.valid {
            border-left-color: var(--neon-green);
        }
        
        .result-item.invalid {
            border-left-color: #ff4444;
        }
        
        .token-status {
            display: inline-block;
            padding: 5px 15px;
            border-radius: 20px;
            font-size: 0.9em;
            font-weight: 700;
            margin-left: 15px;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        
        .status-valid {
            background: var(--neon-green);
            color: black;
        }
        
        .status-invalid {
            background: #ff4444;
            color: white;
        }
        
        .error-message {
            background: rgba(255, 0, 0, 0.1);
            border: 1px solid #ff4444;
            color: #ff4444;
            padding: 20px;
            border-radius: 12px;
            margin: 20px 0;
            text-align: center;
            animation: pulseError 2s infinite;
        }
        
        @keyframes pulseError {
            0% { box-shadow: 0 0 10px rgba(255, 0, 0, 0.3); }
            50% { box-shadow: 0 0 20px rgba(255, 0, 0, 0.5); }
            100% { box-shadow: 0 0 10px rgba(255, 0, 0, 0.3); }
        }
        
        .success-message {
            background: rgba(0, 255, 136, 0.1);
            border: 1px solid var(--neon-green);
            color: var(--neon-green);
            padding: 20px;
            border-radius: 12px;
            margin: 20px 0;
            text-align: center;
            animation: pulseSuccess 2s infinite;
        }
        
        @keyframes pulseSuccess {
            0% { box-shadow: 0 0 10px rgba(0, 255, 136, 0.3); }
            50% { box-shadow: 0 0 20px rgba(0, 255, 136, 0.5); }
            100% { box-shadow: 0 0 10px rgba(0, 255, 136, 0.3); }
        }
        
        .loading {
            display: inline-block;
            width: 25px;
            height: 25px;
            border: 3px solid rgba(255, 255, 255, 0.3);
            border-radius: 50%;
            border-top-color: var(--neon-gold);
            animation: spin 1s ease-in-out infinite;
            margin-right: 15px;
        }
        
        @keyframes spin {
            to { transform: rotate(360deg); }
        }
        
        .footer {
            text-align: center;
            margin-top: 40px;
            padding: 20px;
            background: rgba(255, 215, 0, 0.1);
            border-radius: 15px;
            border: 1px solid var(--neon-gold);
            font-weight: 700;
            font-size: 1.1em;
            color: var(--neon-gold);
        }
        
        .floating {
            animation: floating 3s ease-in-out infinite;
        }
        
        @keyframes floating {
            0% { transform: translateY(0px); }
            50% { transform: translateY(-10px); }
            100% { transform: translateY(0px); }
        }
        
        @media (max-width: 768px) {
            .container {
                padding: 20px 15px;
            }
            
            .title {
                font-size: 2.5em;
            }
            
            .mode-selector {
                flex-direction: column;
                gap: 15px;
            }
            
            .content-area {
                padding: 25px 20px;
            }
        }
    </style>
</head>
<body>
    <div class="scan-line"></div>
    
    <div class="container">
        <div class="header floating">
            <div class="title">👑 AAHAN 👑</div>
            <div class="subtitle">ULTIMATE FACEBOOK TOKEN MASTER</div>
        </div>
        
        <div class="mode-selector">
            <button class="mode-btn active" onclick="switchMode('single')">
                🔑 SINGLE TOKEN
            </button>
            <button class="mode-btn" onclick="switchMode('multi')">
                📁 MULTI TOKEN CHECKER
            </button>
        </div>
        
        <div class="content-area">
            <!-- Single Token Mode -->
            <div id="single-mode" class="mode-content active">
                <form method="POST">
                    <div class="input-group">
                        <label class="input-label">Enter Your Facebook Access Token:</label>
                        <input type="text" name="token" placeholder="EAAB... (Paste your token here)" required>
                    </div>
                    <button type="submit" class="submit-btn">
                        🚀 EXTRACT PAGE TOKENS
                    </button>
                </form>
            </div>
            
            <!-- Multi Token Mode -->
            <div id="multi-mode" class="mode-content">
                <form id="multiTokenForm" method="POST" enctype="multipart/form-data">
                    <div class="input-group">
                        <label class="input-label">Upload Tokens File (.txt):</label>
                        <div class="file-upload-area" id="fileUploadArea">
                            <div class="upload-icon">📁</div>
                            <h3>CLICK TO UPLOAD OR DRAG & DROP</h3>
                            <p>Supported format: .txt file with one token per line</p>
                            <p style="color: var(--neon-cyan); font-size: 0.9em; margin-top: 10px;">
                                Maximum file size: 16MB
                            </p>
                            <input type="file" id="fileInput" class="file-input" name="token_file" accept=".txt" required>
                        </div>
                    </div>
                    
                    <div id="filePreview" style="display: none;">
                        <div class="success-message" id="fileSuccess"></div>
                    </div>
                    
                    <button type="submit" class="submit-btn" id="processBtn" style="display: none;">
                        ⚡ PROCESS MULTIPLE TOKENS
                    </button>
                </form>
                
                <div class="stats-container" id="statsContainer" style="display: none;">
                    <div class="stat-item">
                        <div class="stat-number" id="totalTokens">0</div>
                        <div class="stat-label">Total Tokens</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-number" id="validTokens">0</div>
                        <div class="stat-label">Valid Tokens</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-number" id="invalidTokens">0</div>
                        <div class="stat-label">Invalid Tokens</div>
                    </div>
                </div>
                
                <div class="progress-container" id="progressContainer" style="display: none;">
                    <div class="progress-bar">
                        <div class="progress-fill" id="progressFill"></div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Results Section -->
        {% if pages %}
            <div class="content-area">
                <h3 style="color: var(--neon-green); text-align: center; margin-bottom: 25px; font-size: 1.5em;">
                    ✅ TOKEN ANALYSIS COMPLETE
                </h3>
                {% for page in pages %}
                    <div class="result-item valid">
                        <strong style="color: var(--neon-cyan); font-size: 1.3em;">
                            {{ page.name }} <span class="token-status status-valid">VALID</span>
                        </strong><br>
                        <div style="margin: 10px 0;">
                            <span style="color: var(--neon-gold);">Page ID:</span> {{ page.id }}
                        </div>
                        <div style="background: rgba(0,0,0,0.6); padding: 15px; border-radius: 8px; margin-top: 10px;">
                            <span style="color: var(--neon-gold);">Access Token:</span><br>
                            <code style="color: var(--neon-pink); word-break: break-all; font-size: 0.9em;">
                                {{ page.access_token }}
                            </code>
                        </div>
                    </div>
                {% endfor %}
            </div>
        {% endif %}

        {% if error %}
            <div class="error-message">
                ❌ {{ error }}
            </div>
        {% endif %}

        <div class="footer">
            🔥 THE UNSTOPPABLE LEGEND AAHAN HERE ❣️ | ULTIMATE TOKEN MASTER 🔥
        </div>
    </div>

    <script>
        function switchMode(mode) {
            // Update active button
            document.querySelectorAll('.mode-btn').forEach(btn => {
                btn.classList.remove('active');
            });
            event.target.classList.add('active');
            
            // Show selected mode content
            document.querySelectorAll('.mode-content').forEach(content => {
                content.classList.remove('active');
            });
            document.getElementById(mode + '-mode').classList.add('active');
            
            // Reset multi-mode when switching away
            if (mode !== 'multi') {
                resetMultiMode();
            }
        }
        
        function resetMultiMode() {
            document.getElementById('filePreview').style.display = 'none';
            document.getElementById('processBtn').style.display = 'none';
            document.getElementById('statsContainer').style.display = 'none';
            document.getElementById('progressContainer').style.display = 'none';
            document.getElementById('fileInput').value = '';
        }
        
        // File upload handling
        const fileInput = document.getElementById('fileInput');
        const fileUploadArea = document.getElementById('fileUploadArea');
        
        fileInput.addEventListener('change', function(e) {
            if (this.files.length > 0) {
                handleFileSelect(this.files[0]);
            }
        });
        
        function handleFileSelect(file) {
            if (!file) return;
            
            if (file.type !== 'text/plain') {
                alert('❌ Please select a valid .txt file');
                return;
            }
            
            if (file.size > 16 * 1024 * 1024) {
                alert('❌ File size too large. Maximum 16MB allowed.');
                return;
            }
            
            const reader = new FileReader();
            reader.onload = function(e) {
                const content = e.target.result;
                const tokens = content.split('\n')
                    .map(token => token.trim())
                    .filter(token => token.length > 0 && token.length > 10);
                
                if (tokens.length === 0) {
                    alert('❌ No valid tokens found in the file');
                    return;
                }
                
                // Show file preview
                document.getElementById('filePreview').style.display = 'block';
                document.getElementById('fileSuccess').innerHTML = 
                    `✅ <strong>${file.name}</strong> loaded successfully!<br>
                     📊 <strong>${tokens.length}</strong> tokens found for processing`;
                
                // Show process button
                document.getElementById('processBtn').style.display = 'block';
                
                // Store tokens for processing
                window.uploadedTokens = tokens;
            };
            
            reader.onerror = function() {
                alert('❌ Error reading file');
            };
            
            reader.readAsText(file);
        }
        
        // Drag and drop functionality
        ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
            fileUploadArea.addEventListener(eventName, preventDefaults, false);
        });
        
        function preventDefaults(e) {
            e.preventDefault();
            e.stopPropagation();
        }
        
        ['dragenter', 'dragover'].forEach(eventName => {
            fileUploadArea.addEventListener(eventName, () => {
                fileUploadArea.classList.add('dragover');
            }, false);
        });
        
        ['dragleave', 'drop'].forEach(eventName => {
            fileUploadArea.addEventListener(eventName, () => {
                fileUploadArea.classList.remove('dragover');
            }, false);
        });
        
        fileUploadArea.addEventListener('drop', function(e) {
            const files = e.dataTransfer.files;
            if (files.length > 0) {
                fileInput.files = files;
                handleFileSelect(files[0]);
            }
        });
        
        // Form submission for multi-token processing
        document.getElementById('multiTokenForm').addEventListener('submit', function(e) {
            e.preventDefault();
            
            if (!window.uploadedTokens || window.uploadedTokens.length === 0) {
                alert('❌ Please upload a tokens file first');
                return;
            }
            
            processMultipleTokens();
        });
        
        function processMultipleTokens() {
            const tokens = window.uploadedTokens;
            const processBtn = document.getElementById('processBtn');
            const progressFill = document.getElementById('progressFill');
            const statsContainer = document.getElementById('statsContainer');
            const progressContainer = document.getElementById('progressContainer');
            
            // Show stats and progress
            statsContainer.style.display = 'flex';
            progressContainer.style.display = 'block';
            
            // Update stats
            document.getElementById('totalTokens').textContent = tokens.length;
            document.getElementById('validTokens').textContent = '0';
            document.getElementById('invalidTokens').textContent = '0';
            
            // Disable button and show loading
            processBtn.disabled = true;
            processBtn.innerHTML = '<span class="loading"></span> PROCESSING TOKENS...';
            
            let validCount = 0;
            let invalidCount = 0;
            let processedCount = 0;
            
            // Create results container if not exists
            let resultsContainer = document.getElementById('multiResults');
            if (!resultsContainer) {
                resultsContainer = document.createElement('div');
                resultsContainer.id = 'multiResults';
                document.getElementById('multi-mode').appendChild(resultsContainer);
            }
            resultsContainer.innerHTML = '';
            
            // Process tokens sequentially
            tokens.forEach((token, index) => {
                setTimeout(() => {
                    checkToken(token).then(result => {
                        processedCount++;
                        
                        // Update progress
                        const progress = (processedCount / tokens.length) * 100;
                        progressFill.style.width = progress + '%';
                        
                        if (result.valid) {
                            validCount++;
                            document.getElementById('validTokens').textContent = validCount;
                        } else {
                            invalidCount++;
                            document.getElementById('invalidTokens').textContent = invalidCount;
                        }
                        
                        // If all tokens processed
                        if (processedCount === tokens.length) {
                            processBtn.innerHTML = '✅ PROCESSING COMPLETED';
                            processBtn.style.background = 'linear-gradient(45deg, var(--neon-green), var(--neon-cyan))';
                            
                            // Show summary
                            const summary = document.createElement('div');
                            summary.className = 'success-message';
                            summary.innerHTML = `
                                <strong>🎉 BATCH PROCESSING COMPLETED!</strong><br>
                                <div style="margin-top: 10px;">
                                    📊 <strong>Total:</strong> ${tokens.length} | 
                                    ✅ <strong style="color: var(--neon-green);">Valid:</strong> ${validCount} | 
                                    ❌ <strong style="color: #ff4444;">Invalid:</strong> ${invalidCount} |
                                    📈 <strong>Success Rate:</strong> ${((validCount/tokens.length)*100).toFixed(1)}%
                                </div>
                            `;
                            resultsContainer.appendChild(summary);
                        }
                    });
                }, index * 2000); // 2 second delay between requests
            });
        }
        
        function checkToken(token) {
            return fetch('/check-token', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ token: token })
            })
            .then(response => response.json())
            .catch(error => {
                return { valid: false, error: 'Network error' };
            });
        }
        
        // Add floating particles effect
        function createParticles() {
            const colors = ['#ffd700', '#00f3ff', '#ff00ff', '#9d00ff'];
            for(let i = 0; i < 15; i++) {
                setTimeout(() => {
                    const particle = document.createElement('div');
                    particle.style.position = 'fixed';
                    particle.style.width = Math.random() * 6 + 2 + 'px';
                    particle.style.height = particle.style.width;
                    particle.style.background = colors[Math.floor(Math.random() * colors.length)];
                    particle.style.borderRadius = '50%';
                    particle.style.top = Math.random() * 100 + 'vh';
                    particle.style.left = Math.random() * 100 + 'vw';
                    particle.style.opacity = Math.random() * 0.4 + 0.1;
                    particle.style.zIndex = '0';
                    particle.style.pointerEvents = 'none';
                    particle.style.boxShadow = `0 0 ${Math.random() * 10 + 5}px currentColor`;
                    document.body.appendChild(particle);
                    
                    // Animate particle
                    animateParticle(particle);
                }, i * 200);
            }
        }
        
        function animateParticle(element) {
            let x = parseFloat(element.style.left);
            let y = parseFloat(element.style.top);
            let xSpeed = (Math.random() - 0.5) * 0.5;
            let ySpeed = (Math.random() - 0.5) * 0.5;
            
            function move() {
                x += xSpeed;
                y += ySpeed;
                
                if(x < 0 || x > 100) xSpeed *= -1;
                if(y < 0 || y > 100) ySpeed *= -1;
                
                element.style.left = x + 'vw';
                element.style.top = y + 'vh';
                
                requestAnimationFrame(move);
            }
            move();
        }
        
        // Initialize
        document.addEventListener('DOMContentLoaded', function() {
            createParticles();
        });
    </script>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Check if it's single token or file upload
        if 'token_file' in request.files:
            # Multi-token file upload
            file = request.files['token_file']
            
            if file.filename == '':
                return render_template_string(HTML_TEMPLATE, error="❌ No file selected")
            
            if not file.filename.endswith('.txt'):
                return render_template_string(HTML_TEMPLATE, error="❌ Only .txt files are allowed")
            
            try:
                content = file.read().decode('utf-8')
                tokens = [token.strip() for token in content.split('\n') if token.strip()]
                
                if not tokens:
                    return render_template_string(HTML_TEMPLATE, error="❌ No valid tokens found in the file")
                
                # Process first few tokens to show capability
                sample_tokens = tokens[:5]  # Process first 5 tokens as sample
                results = []
                valid_count = 0
                invalid_count = 0
                
                for token in sample_tokens:
                    try:
                        verify_url = f"{GRAPH_API_URL}/me?fields=name,id&access_token={token}"
                        verify_res = requests.get(verify_url, timeout=10)
                        
                        if verify_res.status_code == 200:
                            user_data = verify_res.json()
                            valid_count += 1
                            
                            pages_url = f"{GRAPH_API_URL}/me/accounts?fields=name,id,access_token&access_token={token}"
                            pages_res = requests.get(pages_url, timeout=15)
                            pages_data = pages_res.json()
                            
                            pages = pages_data.get('data', [])
                            
                            results.append({
                                'name': user_data.get('name', 'Unknown User'),
                                'id': user_data.get('id', 'N/A'),
                                'access_token': token[:50] + '...' if len(token) > 50 else token,
                                'pages': pages
                            })
                        else:
                            invalid_count += 1
                            
                    except:
                        invalid_count += 1
                
                # For demo, we'll just show sample results
                return render_template_string(HTML_TEMPLATE, 
                    pages=results[:3],  # Show first 3 valid results
                    error=f"Sample processing: {valid_count} valid, {invalid_count} invalid out of {len(sample_tokens)} tokens checked"
                )
                
            except Exception as e:
                return render_template_string(HTML_TEMPLATE, error=f"❌ File processing error: {str(e)}")
        
        else:
            # Single token processing
            token = request.form.get('token')
            if not token:
                return render_template_string(HTML_TEMPLATE, error="❌ Token is required")

            try:
                verify_url = f"{GRAPH_API_URL}/me?access_token={token}"
                verify_res = requests.get(verify_url, timeout=10)
                
                if verify_res.status_code != 200:
                    return render_template_string(HTML_TEMPLATE, error="❌ Invalid token or network error")
                
                url = f"{GRAPH_API_URL}/me/accounts?fields=name,id,access_token&access_token={token}"
                res = requests.get(url, timeout=30)
                data = res.json()

                if "data" in data and len(data["data"]) > 0:
                    return render_template_string(HTML_TEMPLATE, pages=data["data"])
                else:
                    error_msg = data.get("error", {}).get("message", "❌ No pages found or invalid token permissions.")
                    return render_template_string(HTML_TEMPLATE, error=error_msg)
                    
            except requests.exceptions.Timeout:
                return render_template_string(HTML_TEMPLATE, error="❌ Request timeout - try again")
            except requests.exceptions.ConnectionError:
                return render_template_string(HTML_TEMPLATE, error="❌ Network connection error")
            except Exception as e:
                return render_template_string(HTML_TEMPLATE, error=f"❌ Error: {str(e)}")

    return render_template_string(HTML_TEMPLATE)

@app.route('/check-token', methods=['POST'])
def check_token():
    """API endpoint for checking individual tokens"""
    data = request.get_json()
    token = data.get('token')
    
    if not token:
        return jsonify({"valid": False, "error": "No token provided"})
    
    try:
        verify_url = f"{GRAPH_API_URL}/me?fields=name,id&access_token={token}"
        verify_res = requests.get(verify_url, timeout=10)
        
        if verify_res.status_code != 200:
            return jsonify({
                "valid": False, 
                "error": verify_res.json().get('error', {}).get('message', 'Invalid token')
            })
        
        user_data = verify_res.json()
        
        pages_url = f"{GRAPH_API_URL}/me/accounts?fields=name,id,access_token&access_token={token}"
        pages_res = requests.get(pages_url, timeout=15)
        pages_data = pages_res.json()
        
        pages = []
        if "data" in pages_data:
            pages = pages_data["data"]
        
        return jsonify({
            "valid": True,
            "user_name": user_data.get('name'),
            "user_id": user_data.get('id'),
            "pages": pages
        })
        
    except requests.exceptions.Timeout:
        return jsonify({"valid": False, "error": "Request timeout"})
    except requests.exceptions.ConnectionError:
        return jsonify({"valid": False, "error": "Network error"})
    except Exception as e:
        return jsonify({"valid": False, "error": str(e)})

@app.route('/health')
def health():
    return jsonify({"status": "healthy", "message": "AAHAN Token Checker is running"})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    print(f"🚀 Starting AAHAN Ultimate Token Master on port {port}...")
    app.run(host='0.0.0.0', port=port, debug=False)
