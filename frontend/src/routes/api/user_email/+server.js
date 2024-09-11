// src/routes/api/user_email/+server.js
import { Readable } from 'stream';

export async function GET({ request }) {
  const cookies = request.headers.get('cookie') || '';
  console.log('Received cookies:', cookies);
  
  // Function to find and decode a cookie by name
  function getCookieValue(cookieName) {
    const cookie = cookies.split('; ').find(row => row.startsWith(`${cookieName}=`));
    const encodedValue = cookie ? cookie.split('=')[1] : null;
    return encodedValue ? decodeURIComponent(encodedValue) : null;
  }
  
  // Get and decode the userEmail and accessToken cookies
  const userEmail = getCookieValue('userEmail');
  const accessToken = getCookieValue('accessToken');
  
  console.log('Decoded user email:', userEmail);
  console.log('Decoded access token:', accessToken);
  
  // Create a readable stream
  const readable = new Readable({
    read() {
      // Push the user email and access token as a JSON object
      this.push(JSON.stringify({ userEmail, accessToken }));
      this.push(null); // Signal the end of the stream
    }
  });

  return new Response(readable, {
    headers: { 'Content-Type': 'application/json' }
  });
}
