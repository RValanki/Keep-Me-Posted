describe('Sign Up Flow', () => {
    // Define the base URL if not set in Cypress config
    const baseUrl = 'http://localhost:5173';

    // Run before each test
    beforeEach(() => {
        cy.visit(`${baseUrl}/signup`); // Visit the sign-up page
    });

    it('should display the sign-up page', () => {
        cy.url().should('include', '/signup');
        cy.get('h1').should('contain', 'Sign Up');
    });

    it('should allow a user to sign up with normal credentials', () => {
        // Fill out the sign-up form
        cy.get('input[name="email"]').type('newuser@example.com');
        cy.get('input[name="password"]').type('Password123!');
        cy.get('input[name="verifyPassword"]').type('Password123!');
        
        // Click the sign-up button
        cy.get('button[type="submit"]').click();

        // Verify successful redirection or success message
        cy.url().should('include', '/welcome'); // Adjust based on actual post-sign-up page
        cy.get('.success-message').should('contain', 'Sign up successful');
    });

    it('should show validation messages for invalid normal sign-up inputs', () => {
        // Attempt to sign up with invalid inputs
        cy.get('input[name="email"]').type('invalid-email');
        cy.get('input[name="password"]').type('short');
        cy.get('input[name="verifyPassword"]').type('different');
        
        // Click the sign-up button
        cy.get('button[type="submit"]').click();
        
        // Check for validation messages
        cy.get('.email-error').should('contain', 'Please enter a valid email');
        cy.get('.password-error').should('contain', 'Password must be at least 8 characters');
        cy.get('.verify-password-error').should('contain', 'Passwords must match');
    });

    it('should redirect to Google for authentication when "Sign in with Google" is clicked', () => {
        // Click the Google sign-in button
        cy.get('button').contains('Sign in with Google').click();

        // Verify redirection to Google authentication (or check for the presence of Google sign-in UI)
        cy.url().should('include', 'accounts.google.com');
    });

    it('should handle Google sign-in successfully and redirect to the welcome page', () => {
        // Simulate successful Google sign-in
        cy.intercept('POST', '**/auth/google/callback', {
            statusCode: 200,
            body: { message: 'Sign in successful' },
        }).as('googleSignInRequest');

        // Trigger Google sign-in
        cy.get('button').contains('Sign in with Google').click();
        
        // Wait for the sign-in request to complete
        cy.wait('@googleSignInRequest');
        
        // Verify redirection to the welcome page
        cy.url().should('include', '/welcome');
    });

    it('should show error message for server errors during Google authentication', () => {
        // Simulate server error response for Google sign-in
        cy.intercept('POST', '**/auth/google/callback', {
            statusCode: 500,
            body: { message: 'Server error during Google authentication' },
        }).as('googleSignInRequest');

        // Trigger Google sign-in
        cy.get('button').contains('Sign in with Google').click();
        
        // Wait for the sign-in request to complete
        cy.wait('@googleSignInRequest');
        
        // Verify error message is displayed
        cy.get('.error-message').should('contain', 'Server error during Google authentication');
    });

    it('should redirect to the login page when clicking "Already have an account?" link', () => {
        cy.get('a[href="/login"]').click(); // Assuming the link is pointing to the login page
        cy.url().should('include', '/login');
    });

});
