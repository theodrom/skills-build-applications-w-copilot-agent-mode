
import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

// Make REACT_APP_CODESPACE_NAME available for all components
if (!process.env.REACT_APP_CODESPACE_NAME) {
  // Try to infer from window.location if not set
  const match = window.location.hostname.match(/^(.*)-8000\.app\.github\.dev$/);
  if (match) {
    process.env.REACT_APP_CODESPACE_NAME = match[1];
  }
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

reportWebVitals();
