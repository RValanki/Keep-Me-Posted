// src/hooks.server.js
import { getAuthFromCookies } from '$lib/auth';

export async function handle({ event, resolve }) {
    /*
    This hook runs on the server before handling the request and can be used to
    implement route protection, redirects, and other server-side logic.

    The hook checks the authentication status of the user based on the cookies
    sent with the request. If the user is not authenticated and tries to access
    a protected route, they are redirected to the login page.
    */
    if (import.meta.env.MODE !== 'production') {
        return await resolve(event);
    }

    try {
        // Extract cookies from the request
        const cookieHeader = event.request.headers.get('cookie') || '';
        
        // Check authentication status based on cookies
        const { isAuthenticated } = await getAuthFromCookies(cookieHeader);

        // Define protected routes
        const protectedRoutes = [
            '/upload_audio',
            '/generate_summary',
            '/email',
            'send_summary'
        ];

        // Define routes that should not be accessible for logged-in users
        const restrictedRoutes = [
            '/login',
            '/signup'
        ];

        // Redirect to login if the user is not authenticated
        if (!isAuthenticated && protectedRoutes.some(route => event.url.pathname.startsWith(route))) {
            console.log('Redirecting to login');

            return new Response(null, {
                status: 302,
                headers: {
                    Location: '/login' // Redirect to the login page
                }
            });
        }

        // Redirect to upload_audio if the user is authenticated
        if (isAuthenticated && restrictedRoutes.some(route => event.url.pathname.startsWith(route)) ) {
            console.log('Redirecting to upload_audio');

            return new Response(null, {
                status: 302,
                headers: {
                    Location: '/upload_audio' // Redirect to the upload_audio page
                }
            });
        }
        
        return await resolve(event);
    } catch (error) {
        console.error('Error in handle hook:', error);
        return new Response('Internal Server Error', { status: 500 });
    }
}
