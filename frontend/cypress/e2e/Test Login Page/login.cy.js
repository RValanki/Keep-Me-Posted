/**
 * The file contains the test cases for the login page.
 */

// Test the login page
describe("Access login page", () => {
    beforeEach(() => {
        cy.visit("/login");
    }
    );

    it("should have the correct page title", () => {
        cy.title().should("include", "Keep Me Posted");
    }
    );
}
);


// Test login with valid cerdentials
describe("Mocking Valid Login", () => {
    it("mock valid login with credentials", () => {
        // Visit the login page
        cy.visit("/login");

        // Intercept the backend login request to return a successful response
        cy.intercept("POST", 'http://127.0.0.1:8000/login', {
            statusCode: 200,
            body: {
                token: "1234",
                user: {
                    id: 1,
                    email: "test@example.com",
                    username: "test@example.com",

                },
            }
        }).as("loginRequest");

        // wait for the page to load
        cy.wait(200);

        // Fill in the login form
        cy.get("#email-input").should('be.visible').type("test@example.com");
        cy.get("#password-input").should('be.visible').type("password");
        cy.get("#login-button").click();

        // Wait for the mocked login request to complete
        cy.wait("@loginRequest")

        // Check that the user is redirected to the upload audio page
        cy.url().should("include", "/upload_audio");
    }
    );

});

// Test login with invalid cerdentials (wrong email or password)
describe("Mocking Invalid Login", () => {
    it("mock invalid login with credentials", () => {
        // Visit the login page
        cy.visit("/login");

        // Intercept the backend login request to return an error response
        cy.intercept("POST", 'http://127.0.0.1:8000/login', {
            statusCode: 404,
            body: {
                detail: "Not found!",
            }
        }).as("loginRequest");

        // wait for the page to load
        cy.wait(200);

        // Fill in the login form
        cy.get("#email-input").should('be.visible').type("test@example.com");
        cy.get("#password-input").should('be.visible').type("password");
        cy.get("#login-button").click();

        // Wait for the mocked login request to complete
        cy.wait("@loginRequest")

        // Check that the user is not redirected to the upload audio page
        cy.url().should("include", "/login");

        // Check that the error message is displayed
        cy.get('#email-input > #login-form-container > #validation-message').should('be.visible').contains('Incorrect Email or Password');
        cy.get('#password-input > #login-form-container > #validation-message').should('be.visible').contains('Incorrect Email or Password');

    });
});
