// src/routes/api/user_email/+server.js
import { Readable } from 'stream';

export async function GET({ request }) {
  const cookies = request.headers.get('cookie') || '';
  console.log('Received cookies:', cookies);
  
  // Find and decode the userEmail cookie
  const userEmailCookie = cookies.split('; ').find(row => row.startsWith('userEmail='));
  const encodedUserEmail = userEmailCookie ? userEmailCookie.split('=')[1] : null;
  const userEmail = encodedUserEmail ? decodeURIComponent(encodedUserEmail) : null;
  
  console.log('Decoded user email:', userEmail);
  
  // Create a readable stream
  const readable = new Readable({
    read() {
      // Push the user email as a JSON object
      this.push(JSON.stringify({ userEmail }));
      this.push(null); // Signal the end of the stream
    }
  });

  return new Response(readable, {
    headers: { 'Content-Type': 'application/json' }
  });
}
