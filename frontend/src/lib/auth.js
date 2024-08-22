import { backendURL } from "../api-functions/base-URL";


export async function getAuthFromCookies(cookieHeader) {
    const cookies = new URLSearchParams(cookieHeader?.replace('; ', '&') || '');
    const authToken = cookies.get('auth_token');

    // Check if the token is valid
    const isAuthenticated = authToken ? await verifyToken(authToken) : false;
    return { isAuthenticated };
}

async function verifyToken(token) {
    try {
        // Send a POST request to the backend to verify the token
        const response = await fetch(`${backendURL}/verify_token`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ token }),
        });

        if (response.ok) {
            const data = await response.json();
            
            // Return true if the token is valid
            return data.message === 'Token is valid.'; 
        } else {
            console.error('Token verification failed');
        }
    } catch (e) {
        console.error('Error during token verification:', e);
    }
    return false;
}

