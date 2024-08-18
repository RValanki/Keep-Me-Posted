// cypress/integration/oauth.spec.js

describe('Home Page', () => {
    // Define the base URL if not set in Cypress config
    const baseUrl = 'http://localhost:5173';
  
    // Run before each test
    beforeEach(() => {
        cy.visit(baseUrl + "/login"); // Visit the login page
    });

    it('should display the Google sign-in button', () => {
        // Check if the Google sign-in button is visible
        cy.get('#google-button').should('be.visible').and("exist");
    });
});

describe('OAuth2 Login Flow', () => {
    // Define the base URL if not set in Cypress config
    const baseUrl = 'http://localhost:5173';
  
    // Run before each test
    beforeEach(() => {
        cy.visit(baseUrl + "/login"); // Visit the login page
    });

    it('should display the Google sign-in button', () => {
        // Check if the Google sign-in button is visible
        cy.get('#google-button').should('be.visible').and("exist");
    });

    it('should handle OAuth2 callback and redirect to /upload_audio', () => {
        // Mock the OAuth2 flow by intercepting the GET request to the callback URL

        // Find the button by its id and click it
        cy.get('#google-button').click();

        // Mock the OAuth2 token exchange process
        cy.intercept('GET', '**/oauth**', (req) => {
            const fakeTokenResponse = {
                tokens: {
                    access_token: 'fake_access_token',
                    refresh_token: 'fake_refresh_token',
                },
            };

            // Simulate fetching the token
            req.reply((res) => {
                res.send(fakeTokenResponse);
            });
        }).as('oauthRequest');

        // Simulate the callback with the code
        cy.visit(baseUrl + '/oauth?code=fake_auth_code');

        // // Mock the user info request to Google API
        // cy.intercept('GET', 'https://www.googleapis.com/oauth2/v3/userinfo?access_token=fake_access_token', {
        //     statusCode: 200,
        //     body: {
        //         email: 'test@example.com',
        //     },
        // }).as('userInfoRequest');

        // // Ensure the user info request was made
        // cy.wait('@userInfoRequest').its('response.statusCode').should('eq', 200);

        // Ensure the OAuth2 token exchange request was made
        cy.wait('@oauthRequest').its('response.statusCode').should('eq', 303);

        // Ensure the user is redirected to the correct page after authentication
        cy.url().should('include', '/upload_audio');

    });

    // it('should display an error message on OAuth2 failure', () => {
    //     // Mock an error during OAuth2 token exchange
    //     cy.intercept('GET', '**/oauth**', {
    //         statusCode: 400,
    //         body: { error: 'invalid_grant' },
    //     }).as('oauthErrorRequest');

    //     // Click the Google sign-in button
    //     cy.get('#google-button').click();

    //     // Simulate the callback with an invalid code using cy.request()
    //     cy.request({
    //         url: '/oauth?code=invalid_code',
    //         failOnStatusCode: false // This prevents Cypress from failing the test on non-2xx status codes
    //     }).then((response) => {
    //         // Ensure the OAuth2 token exchange request failed
    //         expect(response.status).to.eq(400);
    //         // Check for an error message in the response
    //         cy.get('.error-message').should('be.visible').and('contain', 'Authentication failed');
    //     });
    //     // Ensure the OAuth2 token exchange request failed
    //     cy.wait('@oauthErrorRequest').its('response.statusCode').should('eq', 400);

    //     // Check for an error message on the page
    //     cy.get('.error-message').should('be.visible').and('contain', 'Authentication failed');
    // });
});
