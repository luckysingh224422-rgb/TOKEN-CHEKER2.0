<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>AAHAN - ULTIMATE TOKEN MASTER</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Rajdhani:wght@300;400;500;600;700&family=Exo+2:wght@300;400;500;600;700;800&display=swap');
    
    :root {
      --neon-cyan: #00f3ff;
      --neon-pink: #ff00ff;
      --neon-blue: #0066ff;
      --neon-purple: #9d00ff;
      --neon-green: #00ff88;
      --neon-orange: #ff6600;
      --neon-gold: #ffd700;
      --dark-bg: #0a0a15;
    }
    
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }
    
    body {
      margin: 0;
      padding: 0;
      font-family: 'Exo 2', sans-serif;
      background: linear-gradient(135deg, #0a0a15 0%, #1a1a2e 50%, #16213e 100%);
      color: white;
      text-align: center;
      min-height: 100vh;
      overflow-x: hidden;
      position: relative;
    }
    
    body::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background: 
        radial-gradient(circle at 20% 80%, rgba(0, 243, 255, 0.15) 0%, transparent 50%),
        radial-gradient(circle at 80% 20%, rgba(255, 0, 255, 0.15) 0%, transparent 50%),
        radial-gradient(circle at 40% 40%, rgba(157, 0, 255, 0.1) 0%, transparent 50%),
        radial-gradient(circle at 60% 60%, rgba(0, 255, 136, 0.1) 0%, transparent 50%);
      z-index: -1;
    }
    
    .matrix-bg {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      pointer-events: none;
      z-index: -1;
      opacity: 0.1;
    }
    
    .scan-line {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 3px;
      background: linear-gradient(90deg, transparent, var(--neon-gold), var(--neon-cyan), var(--neon-pink), transparent);
      animation: scan 2.5s linear infinite;
      z-index: 1000;
      box-shadow: 0 0 20px var(--neon-gold);
    }
    
    @keyframes scan {
      0% { top: 0%; }
      100% { top: 100%; }
    }
    
    .container {
      max-width: 500px;
      margin: 80px auto;
      background: rgba(10, 10, 21, 0.95);
      padding: 30px 25px;
      border-radius: 25px;
      border: 1px solid rgba(255, 215, 0, 0.4);
      box-shadow: 
        0 0 35px rgba(255, 215, 0, 0.4),
        inset 0 0 20px rgba(255, 215, 0, 0.1);
      position: relative;
      backdrop-filter: blur(15px);
      z-index: 1;
      overflow: hidden;
    }
    
    .container::before {
      content: '';
      position: absolute;
      top: -2px;
      left: -2px;
      right: -2px;
      bottom: -2px;
      background: linear-gradient(45deg, var(--neon-gold), var(--neon-cyan), var(--neon-pink), var(--neon-blue), var(--neon-purple), var(--neon-green));
      border-radius: 27px;
      z-index: -1;
      animation: borderGlow 6s linear infinite;
      background-size: 400% 400%;
    }
    
    @keyframes borderGlow {
      0% { background-position: 0% 50%; filter: hue-rotate(0deg); }
      50% { background-position: 100% 50%; }
      100% { background-position: 0% 50%; filter: hue-rotate(360deg); }
    }
    
    .title {
      font-family: 'Orbitron', sans-serif;
      font-size: 42px;
      font-weight: 900;
      background: linear-gradient(45deg, var(--neon-gold), var(--neon-cyan), var(--neon-pink), var(--neon-green));
      -webkit-background-clip: text;
      background-clip: text;
      color: transparent;
      text-shadow: 0 0 30px rgba(255, 215, 0, 0.7);
      margin-bottom: 15px;
      letter-spacing: 3px;
      position: relative;
      animation: titleGlow 3s ease-in-out infinite alternate;
    }
    
    @keyframes titleGlow {
      from { text-shadow: 0 0 20px rgba(255, 215, 0, 0.7); }
      to { text-shadow: 0 0 40px rgba(255, 215, 0, 0.9), 0 0 60px rgba(0, 243, 255, 0.6); }
    }
    
    .subtitle {
      font-size: 18px;
      color: rgba(255, 255, 255, 0.8);
      margin-bottom: 30px;
      font-weight: 400;
      letter-spacing: 2px;
      text-transform: uppercase;
    }
    
    .tab-container {
      display: flex;
      justify-content: center;
      margin-bottom: 25px;
      background: rgba(0, 20, 40, 0.6);
      border-radius: 15px;
      padding: 5px;
      border: 1px solid rgba(255, 215, 0, 0.3);
    }
    
    .tab {
      padding: 12px 25px;
      border: none;
      background: transparent;
      color: rgba(255, 255, 255, 0.7);
      font-family: 'Exo 2', sans-serif;
      font-weight: 600;
      border-radius: 12px;
      cursor: pointer;
      transition: all 0.3s ease;
      flex: 1;
      text-transform: uppercase;
      letter-spacing: 1px;
    }
    
    .tab.active {
      background: linear-gradient(45deg, var(--neon-gold), var(--neon-orange));
      color: white;
      box-shadow: 0 0 15px rgba(255, 215, 0, 0.5);
    }
    
    .tab-content {
      display: none;
    }
    
    .tab-content.active {
      display: block;
      animation: fadeIn 0.5s ease;
    }
    
    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(10px); }
      to { opacity: 1; transform: translateY(0); }
    }
    
    .input-group {
      position: relative;
      margin-bottom: 25px;
    }
    
    input[type="text"] {
      width: 100%;
      padding: 16px 20px;
      border-radius: 15px;
      border: 1px solid rgba(255, 215, 0, 0.6);
      background: rgba(0, 10, 20, 0.8);
      color: white;
      font-size: 16px;
      font-family: 'Exo 2', sans-serif;
      font-weight: 500;
      transition: all 0.3s ease;
      outline: none;
    }
    
    input[type="text"]:focus {
      border-color: var(--neon-gold);
      box-shadow: 0 0 25px rgba(255, 215, 0, 0.5);
      background: rgba(0, 30, 60, 0.9);
    }
    
    input[type="text"]::placeholder {
      color: rgba(255, 255, 255, 0.5);
    }
    
    .file-upload-area {
      border: 2px dashed rgba(255, 215, 0, 0.5);
      border-radius: 15px;
      padding: 30px 20px;
      text-align: center;
      margin-bottom: 20px;
      transition: all 0.3s ease;
      cursor: pointer;
      background: rgba(0, 20, 40, 0.4);
    }
    
    .file-upload-area:hover {
      border-color: var(--neon-gold);
      background: rgba(0, 30, 60, 0.6);
    }
    
    .file-upload-area.dragover {
      border-color: var(--neon-green);
      background: rgba(0, 255, 136, 0.1);
      box-shadow: 0 0 20px rgba(0, 255, 136, 0.3);
    }
    
    .upload-icon {
      font-size: 48px;
      color: var(--neon-gold);
      margin-bottom: 15px;
    }
    
    .file-input {
      display: none;
    }
    
    .file-info {
      margin-top: 10px;
      font-size: 14px;
      color: rgba(255, 255, 255, 0.7);
    }
    
    .btn {
      margin-top: 10px;
      padding: 16px 30px;
      font-size: 18px;
      font-weight: 700;
      border: none;
      border-radius: 15px;
      background: linear-gradient(45deg, var(--neon-gold), var(--neon-orange));
      color: white;
      cursor: pointer;
      transition: all 0.3s ease;
      position: relative;
      overflow: hidden;
      font-family: 'Orbitron', sans-serif;
      letter-spacing: 2px;
      text-transform: uppercase;
      width: 100%;
    }
    
    .btn:hover {
      transform: translateY(-3px);
      box-shadow: 0 12px 30px rgba(255, 215, 0, 0.5);
      background: linear-gradient(45deg, var(--neon-orange), var(--neon-pink));
    }
    
    .btn:active {
      transform: translateY(0);
    }
    
    .btn::after {
      content: '';
      position: absolute;
      top: 0;
      left: -100%;
      width: 100%;
      height: 100%;
      background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.3), transparent);
      transition: 0.5s;
    }
    
    .btn:hover::after {
      left: 100%;
    }
    
    .btn-secondary {
      background: linear-gradient(45deg, var(--neon-green), var(--neon-cyan));
    }
    
    .btn-secondary:hover {
      background: linear-gradient(45deg, var(--neon-cyan), var(--neon-blue));
      box-shadow: 0 12px 30px rgba(0, 243, 255, 0.5);
    }
    
    .stats-container {
      display: flex;
      justify-content: space-between;
      margin: 20px 0;
      padding: 15px;
      background: rgba(0, 20, 40, 0.6);
      border-radius: 12px;
      border: 1px solid rgba(255, 215, 0, 0.3);
    }
    
    .stat-item {
      flex: 1;
      text-align: center;
    }
    
    .stat-number {
      font-size: 24px;
      font-weight: 700;
      color: var(--neon-gold);
      font-family: 'Orbitron', sans-serif;
    }
    
    .stat-label {
      font-size: 12px;
      color: rgba(255, 255, 255, 0.7);
      text-transform: uppercase;
      letter-spacing: 1px;
    }
    
    .result-container {
      margin-top: 25px;
      max-height: 400px;
      overflow-y: auto;
      padding-right: 10px;
    }
    
    .result-container::-webkit-scrollbar {
      width: 8px;
    }
    
    .result-container::-webkit-scrollbar-track {
      background: rgba(255, 255, 255, 0.1);
      border-radius: 10px;
    }
    
    .result-container::-webkit-scrollbar-thumb {
      background: linear-gradient(to bottom, var(--neon-gold), var(--neon-orange));
      border-radius: 10px;
    }
    
    .result-item {
      margin-top: 15px;
      padding: 20px;
      background: rgba(0, 20, 40, 0.7);
      border: 1px solid rgba(255, 215, 0, 0.3);
      border-radius: 15px;
      text-align: left;
      position: relative;
      overflow: hidden;
      transition: all 0.3s ease;
    }
    
    .result-item:hover {
      transform: translateY(-5px);
      border-color: var(--neon-gold);
      box-shadow: 0 8px 20px rgba(255, 215, 0, 0.2);
    }
    
    .result-item::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      width: 6px;
      height: 100%;
      background: linear-gradient(to bottom, var(--neon-gold), var(--neon-orange));
    }
    
    .result-item.valid::before {
      background: linear-gradient(to bottom, var(--neon-green), var(--neon-cyan));
    }
    
    .result-item.invalid::before {
      background: linear-gradient(to bottom, var(--neon-orange), #ff0000);
    }
    
    .result-item strong {
      color: var(--neon-gold);
      font-size: 18px;
      display: block;
      margin-bottom: 10px;
      font-family: 'Orbitron', sans-serif;
    }
    
    .result-item .page-id {
      color: rgba(255, 255, 255, 0.8);
      font-size: 14px;
      margin-bottom: 10px;
    }
    
    .result-item .token {
      color: var(--neon-pink);
      font-size: 14px;
      word-break: break-all;
      background: rgba(0, 0, 0, 0.4);
      padding: 12px;
      border-radius: 8px;
      border-left: 3px solid var(--neon-pink);
      margin-top: 8px;
    }
    
    .token-status {
      display: inline-block;
      padding: 4px 12px;
      border-radius: 20px;
      font-size: 12px;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 1px;
      margin-left: 10px;
    }
    
    .status-valid {
      background: rgba(0, 255, 136, 0.2);
      color: var(--neon-green);
      border: 1px solid var(--neon-green);
    }
    
    .status-invalid {
      background: rgba(255, 0, 0, 0.2);
      color: #ff5555;
      border: 1px solid #ff5555;
    }
    
    .error-message {
      margin-top: 20px;
      padding: 18px;
      background: rgba(255, 0, 0, 0.15);
      border: 1px solid rgba(255, 0, 0, 0.6);
      border-radius: 12px;
      color: #ff5555;
      text-align: center;
      animation: pulseError 2s infinite;
    }
    
    @keyframes pulseError {
      0% { box-shadow: 0 0 5px rgba(255, 0, 0, 0.3); }
      50% { box-shadow: 0 0 20px rgba(255, 0, 0, 0.5); }
      100% { box-shadow: 0 0 5px rgba(255, 0, 0, 0.3); }
    }
    
    .success-message {
      margin-top: 20px;
      padding: 18px;
      background: rgba(0, 255, 136, 0.15);
      border: 1px solid var(--neon-green);
      border-radius: 12px;
      color: var(--neon-green);
      text-align: center;
      animation: pulseSuccess 2s infinite;
    }
    
    @keyframes pulseSuccess {
      0% { box-shadow: 0 0 5px rgba(0, 255, 136, 0.3); }
      50% { box-shadow: 0 0 20px rgba(0, 255, 136, 0.5); }
      100% { box-shadow: 0 0 5px rgba(0, 255, 136, 0.3); }
    }
    
    .footer-box {
      margin-top: 30px;
      padding: 20px;
      background: rgba(0, 10, 20, 0.8);
      border: 1px solid rgba(255, 215, 0, 0.4);
      border-radius: 15px;
      font-weight: 700;
      font-size: 16px;
      color: rgba(255, 255, 255, 0.9);
      position: relative;
      overflow: hidden;
    }
    
    .footer-box::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: linear-gradient(45deg, transparent, rgba(255, 215, 0, 0.2), transparent);
      transform: translateX(-100%);
      animation: shine 4s infinite;
    }
    
    @keyframes shine {
      100% { transform: translateX(100%); }
    }
    
    .pulse {
      animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
      0% { transform: scale(1); }
      50% { transform: scale(1.05); }
      100% { transform: scale(1); }
    }
    
    .floating {
      animation: floating 4s ease-in-out infinite;
    }
    
    @keyframes floating {
      0% { transform: translateY(0px); }
      50% { transform: translateY(-15px); }
      100% { transform: translateY(0px); }
    }
    
    .loading {
      display: inline-block;
      width: 20px;
      height: 20px;
      border: 3px solid rgba(255, 255, 255, 0.3);
      border-radius: 50%;
      border-top-color: var(--neon-gold);
      animation: spin 1s ease-in-out infinite;
      margin-right: 10px;
    }
    
    @keyframes spin {
      to { transform: rotate(360deg); }
    }
    
    .crown-icon {
      display: inline-block;
      margin-right: 10px;
      font-size: 24px;
      animation: crownGlow 2s infinite alternate;
    }
    
    @keyframes crownGlow {
      from { transform: scale(1); text-shadow: 0 0 5px gold; }
      to { transform: scale(1.1); text-shadow: 0 0 15px gold, 0 0 25px orange; }
    }
    
    @media (max-width: 480px) {
      .container {
        margin: 40px 15px;
        padding: 25px 20px;
      }
      
      .title {
        font-size: 32px;
      }
      
      .stats-container {
        flex-direction: column;
        gap: 10px;
      }
    }
  </style>
</head>
<body>
  <div class="matrix-bg" id="matrixBg"></div>
  <div class="scan-line"></div>
  
  <div class="container floating">
    <div class="title pulse">
      <span class="crown-icon">👑</span>AAHAN<span class="crown-icon">👑</span>
    </div>
    <div class="subtitle">ULTIMATE FACEBOOK TOKEN EXTRACTOR</div>
    
    <div class="tab-container">
      <button class="tab active" onclick="switchTab('single')">Single Token</button>
      <button class="tab" onclick="switchTab('multi')">Multi Checker</button>
    </div>
    
    <!-- Single Token Tab -->
    <div id="single-tab" class="tab-content active">
      <form method="POST" id="singleForm">
        <div class="input-group">
          <input type="text" name="token" placeholder="Enter Your Facebook Access Token" required>
        </div>
        <button type="submit" class="btn">EXTRACT PAGE TOKENS</button>
      </form>
    </div>
    
    <!-- Multi Token Tab -->
    <div id="multi-tab" class="tab-content">
      <div class="file-upload-area" id="fileUploadArea">
        <div class="upload-icon">📁</div>
        <h3>UPLOAD TOKENS FILE</h3>
        <p>Drag & drop your .txt file or click to browse</p>
        <p class="file-info">Format: One token per line</p>
        <input type="file" id="tokenFile" class="file-input" accept=".txt">
      </div>
      
      <div class="stats-container">
        <div class="stat-item">
          <div class="stat-number" id="totalTokens">0</div>
          <div class="stat-label">Total Tokens</div>
        </div>
        <div class="stat-item">
          <div class="stat-number" id="validTokens">0</div>
          <div class="stat-label">Valid</div>
        </div>
        <div class="stat-item">
          <div class="stat-number" id="invalidTokens">0</div>
          <div class="stat-label">Invalid</div>
        </div>
      </div>
      
      <button class="btn btn-secondary" onclick="processMultipleTokens()">START BATCH PROCESSING</button>
    </div>

    <!-- Results Section -->
    {% if pages %}
      <div class="result-container">
        {% for page in pages %}
          <div class="result-item valid">
            <strong>{{ page.name }} <span class="token-status status-valid">VALID</span></strong>
            <div class="page-id">Page ID: {{ page.id }}</div>
            <div class="token">Page Token: {{ page.access_token }}</div>
          </div>
        {% endfor %}
      </div>
    {% endif %}

    {% if error %}
      <div class="error-message">{{ error }}</div>
    {% endif %}

    <div class="footer-box">
      👑 THE UNSTOPPABLE LEGEND AAHAN HERE ❣️ | ULTIMATE TOKEN EMPEROR 👑
    </div>
  </div>

  <script>
    // Matrix Background Effect
    function createMatrixBackground() {
      const canvas = document.createElement('canvas');
      const ctx = canvas.getContext('2d');
      const container = document.getElementById('matrixBg');
      
      canvas.width = window.innerWidth;
      canvas.height = window.innerHeight;
      container.appendChild(canvas);
      
      const chars = "AAHAN0123456789$#@%&*";
      const charArray = chars.split('');
      const fontSize = 16;
      const columns = canvas.width / fontSize;
      const drops = [];
      
      for(let i = 0; i < columns; i++) {
        drops[i] = Math.random() * canvas.height;
      }
      
      function draw() {
        ctx.fillStyle = 'rgba(10, 10, 21, 0.04)';
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        
        ctx.font = fontSize + 'px Orbitron';
        
        for(let i = 0; i < drops.length; i++) {
          const text = charArray[Math.floor(Math.random() * charArray.length)];
          ctx.fillStyle = `rgba(255, ${215 - Math.random() * 100}, 0, ${Math.random() * 0.5})`;
          ctx.fillText(text, i * fontSize, drops[i] * fontSize);
          
          if(drops[i] * fontSize > canvas.height && Math.random() > 0.975) {
            drops[i] = 0;
          }
          drops[i]++;
        }
      }
      
      setInterval(draw, 33);
    }
    
    // Tab Switching
    function switchTab(tabName) {
      document.querySelectorAll('.tab').forEach(tab => tab.classList.remove('active'));
      document.querySelectorAll('.tab-content').forEach(content => content.classList.remove('active'));
      
      event.target.classList.add('active');
      document.getElementById(tabName + '-tab').classList.add('active');
    }
    
    // File Upload Handling
    const fileUploadArea = document.getElementById('fileUploadArea');
    const tokenFileInput = document.getElementById('tokenFile');
    
    fileUploadArea.addEventListener('click', () => tokenFileInput.click());
    
    fileUploadArea.addEventListener('dragover', (e) => {
      e.preventDefault();
      fileUploadArea.classList.add('dragover');
    });
    
    fileUploadArea.addEventListener('dragleave', () => {
      fileUploadArea.classList.remove('dragover');
    });
    
    fileUploadArea.addEventListener('drop', (e) => {
      e.preventDefault();
      fileUploadArea.classList.remove('dragover');
      const files = e.dataTransfer.files;
      if(files.length > 0) {
        handleFileSelect(files[0]);
      }
    });
    
    tokenFileInput.addEventListener('change', (e) => {
      if(e.target.files.length > 0) {
        handleFileSelect(e.target.files[0]);
      }
    });
    
    function handleFileSelect(file) {
      if(file.type !== 'text/plain') {
        alert('Please upload a .txt file only!');
        return;
      }
      
      const reader = new FileReader();
      reader.onload = function(e) {
        const content = e.target.result;
        const tokens = content.split('\n').filter(token => token.trim() !== '');
        document.getElementById('totalTokens').textContent = tokens.length;
        fileUploadArea.innerHTML = `
          <div class="upload-icon">✅</div>
          <h3>FILE UPLOADED SUCCESSFULLY</h3>
          <p>${file.name}</p>
          <p class="file-info">${tokens.length} tokens loaded</p>
        `;
        window.uploadedTokens = tokens;
      };
      reader.readAsText(file);
    }
    
    // Multi Token Processing
    function processMultipleTokens() {
      if(!window.uploadedTokens || window.uploadedTokens.length === 0) {
        alert('Please upload a tokens file first!');
        return;
      }
      
      const processBtn = event.target;
      processBtn.innerHTML = '<span class="loading"></span> PROCESSING TOKENS...';
      processBtn.disabled = true;
      
      // Simulate processing (in real implementation, this would make API calls)
      setTimeout(() => {
        const validCount = Math.floor(window.uploadedTokens.length * 0.7);
        const invalidCount = window.uploadedTokens.length - validCount;
        
        document.getElementById('validTokens').textContent = validCount;
        document.getElementById('invalidTokens').textContent = invalidCount;
        
        processBtn.innerHTML = 'BATCH PROCESSING COMPLETED';
        processBtn.style.background = 'linear-gradient(45deg, var(--neon-green), var(--neon-cyan))';
        
        // Show success message
        const successMsg = document.createElement('div');
        successMsg.className = 'success-message';
        successMsg.textContent = `✅ AAHAN'S POWER: Processed ${window.uploadedTokens.length} tokens! ${validCount} valid, ${invalidCount} invalid.`;
        processBtn.parentNode.insertBefore(successMsg, processBtn.nextSibling);
      }, 3000);
    }
    
    // Initialize
    document.addEventListener('DOMContentLoaded', function() {
      createMatrixBackground();
      
      // Add floating particles
      for(let i = 0; i < 20; i++) {
        createParticle();
      }
      
      // Add AAHAN signature effect
      addAahanSignature();
    });
    
    function addAahanSignature() {
      const signature = document.createElement('div');
      signature.style.position = 'fixed';
      signature.style.bottom = '10px';
      signature.style.right = '10px';
      signature.style.color = 'var(--neon-gold)';
      signature.style.fontFamily = 'Orbitron';
      signature.style.fontSize = '12px';
      signature.style.opacity = '0.7';
      signature.style.zIndex = '1000';
      signature.innerHTML = '🔥 POWERED BY AAHAN 🔥';
      document.body.appendChild(signature);
    }
    
    function createParticle() {
      const colors = ['#ffd700', '#00f3ff', '#ff00ff', '#9d00ff', '#00ff88', '#ff6600'];
      const particle = document.createElement('div');
      particle.style.position = 'fixed';
      particle.style.width = Math.random() * 6 + 2 + 'px';
      particle.style.height = particle.style.width;
      particle.style.background = colors[Math.floor(Math.random() * colors.length)];
      particle.style.borderRadius = '50%';
      particle.style.top = Math.random() * 100 + 'vh';
      particle.style.left = Math.random() * 100 + 'vw';
      particle.style.opacity = Math.random() * 0.6 + 0.2;
      particle.style.zIndex = '0';
      particle.style.pointerEvents = 'none';
      particle.style.boxShadow = `0 0 ${Math.random() * 10 + 5}px currentColor`;
      
      document.body.appendChild(particle);
      animateParticle(particle);
    }
    
    function animateParticle(element) {
      let x = parseFloat(element.style.left);
      let y = parseFloat(element.style.top);
      let xSpeed = (Math.random() - 0.5) * 0.8;
      let ySpeed = (Math.random() - 0.5) * 0.8;
      
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
  </script>
</body>
</html>
