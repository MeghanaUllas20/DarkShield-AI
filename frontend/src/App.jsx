// src/App.jsx
import React, { useState, useRef } from 'react';
import './App.css'; 

export default function App() {
  const [url, setUrl] = useState('');
  const [text, setText] = useState('');
  const [imageBase64, setImageBase64] = useState(null);
  const [imagePreview, setImagePreview] = useState(null);
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  
  const fileInputRef = useRef(null);

  // Pointing to your live backend!
  const API_URL = 'https://darksheild-ai.onrender.com/api/v1/analyze';

  const handleImageChange = (e) => {
    const file = e.target.files[0];
    if (!file) return;

    setImagePreview(URL.createObjectURL(file));

    const reader = new FileReader();
    reader.onloadend = () => setImageBase64(reader.result);
    reader.readAsDataURL(file);
  };

  const handleScan = async (e) => {
    e.preventDefault();
    if (!url && !text && !imageBase64) return alert("Provide a URL, Text, or Image.");
    
    setLoading(true);
    setResult(null);

    try {
      const response = await fetch(API_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ 
          url: url || null, 
          text: text || null, 
          screenshot_base64: imageBase64 || null 
        })
      });
      const data = await response.json();
      setResult(data);
    } catch (error) {
      alert("Error connecting to DarkShield AI.");
    } finally {
      setLoading(false);
    }
  };

  const getRiskColor = (score) => score > 70 ? 'var(--danger)' : score > 30 ? 'var(--warning)' : 'var(--safe)';
  const getTrustColor = (score) => score > 70 ? 'var(--safe)' : score > 30 ? 'var(--warning)' : 'var(--danger)';

  return (
    <div className="container">
      <header className="header">
        <h1>DarkShield.ai</h1>
        <p>Cyber Threat & Dark Patterns Scanner</p>
      </header>

      <div className="dashboard">
        {/* LEFT PANEL */}
        <div className="glass-panel">
          <form onSubmit={handleScan}>
            <div className="input-group">
              <label>Target URL</label>
              <input 
                type="url" className="input-field" placeholder="https://suspicious-site.com"
                value={url} onChange={(e) => setUrl(e.target.value)} 
              />
            </div>

            <div className="input-group">
              <label>Text Body</label>
              <textarea 
                className="input-field" rows="4" placeholder="Paste suspicious website's text here..."
                value={text} onChange={(e) => setText(e.target.value)} 
              />
            </div>

            <div className="input-group">
              <label>Visuals (Screenshot)</label>
              <div className="file-drop" onClick={() => fileInputRef.current.click()}>
                {!imagePreview ? (
                  <p style={{ margin: 0, color: 'var(--text-muted)' }}>Click to upload screenshot</p>
                ) : (
                  <img src={imagePreview} alt="Preview" className="preview-img" />
                )}
                <input 
                  type="file" accept="image/*" style={{ display: 'none' }} 
                  ref={fileInputRef} onChange={handleImageChange} 
                />
              </div>
            </div>

            <button type="submit" className="btn-scan" disabled={loading}>
              {loading ? 'Analyzing Website Data...' : 'Start Scan'}
            </button>
          </form>
        </div>

        {/* RIGHT PANEL */}
        <div className="glass-panel">
          {!loading && !result && (
            <div style={{ textAlign: 'center', color: 'var(--text-muted)', marginTop: '5rem' }}>
              <h2 style={{ color: 'var(--text-main)' }}>Awaiting Input</h2>
              <p>Enter any Input to begin analysis.</p>
            </div>
          )}

          {loading && (
            <div className="loader-container">
              <div className="radar"></div>
              <p style={{ color: 'var(--primary)', letterSpacing: '2px', fontWeight: 'bold', fontSize: '0.8rem' }}>Ai is Working...</p>
            </div>
          )}

          {result && !loading && (
            <div className="results-container">
              
              <div className="scores-grid">
                {/* Risk Score */}
                <div className="score-card">
                  <h3>Threat Risk</h3>
                  <p className="score-value" style={{ color: getRiskColor(result.risk_score.overall) }}>
                    {result.risk_score.overall}
                  </p>
                  <div className="bar-track">
                    <div className="bar-fill" style={{ width: `${result.risk_score.overall}%`, backgroundColor: getRiskColor(result.risk_score.overall) }}></div>
                  </div>
                </div>

                {/* Trust Score */}
                <div className="score-card">
                  <h3>Trust Index</h3>
                  <p className="score-value" style={{ color: getTrustColor(result.trust_score.overall) }}>
                    {result.trust_score.overall}
                  </p>
                  <div className="bar-track">
                    <div className="bar-fill" style={{ width: `${result.trust_score.overall}%`, backgroundColor: getTrustColor(result.trust_score.overall) }}></div>
                  </div>
                </div>
              </div>

              {/* Detected Patterns */}
              <div>
                <h3 style={{ color: 'var(--text-muted)', borderBottom: '1px solid rgba(255,255,255,0.1)', paddingBottom: '0.5rem', marginBottom: '1rem' }}>
                  Detected Anomalies
                </h3>
                
                {result.detected_patterns.length === 0 ? (
                  <p style={{ color: 'var(--safe)', background: 'rgba(16, 185, 129, 0.1)', padding: '1rem', borderRadius: '8px', border: '1px solid rgba(16, 185, 129, 0.2)' }}>
                    ✅ Target appears clean. No manipulation detected.
                  </p>
                ) : (
                  result.detected_patterns.map((p, index) => (
                    <div className="pattern-item" key={index} style={{ borderLeftColor: p.severity === 'high' ? 'var(--danger)' : 'var(--warning)' }}>
                      <h4 style={{ color: p.severity === 'high' ? '#fca5a5' : '#fde047' }}>
                        {p.pattern_name.replace(/_/g, ' ')} ({p.severity})
                      </h4>
                      <p>"{p.evidence[0]}"</p>
                    </div>
                  ))
                )}
              </div>

            </div>
          )}
        </div>
      </div>
    </div>
  );
}