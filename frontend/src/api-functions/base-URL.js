export const backendURL = import.meta.env.MODE !== 'production'
  ? "http://127.0.0.1:8000"  // Development URL
  : "https://keep-me-posted-server-2.onrender.com";  // Production URL

export const frontendURL = import.meta.env.MODE !== 'production'
  ? "http://127.0.0.1:5173"  // Development URL
  : "https://keep-me-posted-ai.vercel.app";  // Production URL
