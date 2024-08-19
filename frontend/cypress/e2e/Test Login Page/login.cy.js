/**
 * The file contains the test cases for the login page.
 */


describe("Test login page", () => {
    beforeEach(() => {
        cy.visit("/login");
        cy.wait(1000);
    });


    it("should have the correct page title", () => {
        cy.title().should("include", "Keep Me Posted");
    });

    it("should show error message if credentials are invalid", () => {
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
        cy.wait(300);
        cy.get("#password-input").should('be.visible').type("password");
        cy.wait(300);
        cy.get("#login-button").click();

        // Wait for the mocked login request to complete
        cy.wait("@loginRequest", { timeout: 10000 });

        // Check that the user is not redirected to the upload audio page
        cy.url().should("include", "/login");

        // Check that the error message is displayed
        cy.get('#email-input > #login-form-container > #validation-message').should('be.visible').contains('Incorrect Email or Password');
        cy.get('#password-input > #login-form-container > #validation-message').should('be.visible').contains('Incorrect Email or Password');

    });

    it("should pass if credentials are valid", () => {

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
        cy.wait(300);
        cy.get("#password-input").should('be.visible').type("password");
        cy.wait(300);
        cy.get("#login-button").click();


        // Wait for the mocked login request to complete
        cy.wait("@loginRequest", { timeout: 10000 });

        // Wait for the page to load
        cy.wait(2000);
        // Check that the user is redirected to the upload audio page
        cy.url().should("include", "/upload_audio");
    });

    it("should show error message if email is invalid", () => {
        cy.visit("/login");

        cy.wait(200);

        cy.get("#email-input").should('be.visible').type("test@example");
        cy.get("#password-input").should('be.visible').type("password");
        cy.get("#login-button").click();

        cy.get('#email-input > #login-form-container > #validation-message').should('be.visible').contains('Please Enter Valid Email');
    });

    it("should show error message if email is missing", () => {
        cy.visit("/login");

        cy.wait(200);

        cy.get("#password-input").should('be.visible').type("password");
        cy.get("#login-button").click();

        cy.wait(200);
        cy.get('#email-input > #login-form-container > #validation-message').should('be.visible').contains('Please Enter Email');

    });

    it("should show error message if password is missing", () => {
        cy.visit("/login");

        cy.wait(200);

        cy.get("#email-input").should('be.visible').type("test@example.com");
        cy.get("#login-button").click();

        cy.wait(200);
        cy.get('#password-input > #login-form-container > #validation-message').should('be.visible').contains('Please Enter Password');

    });
});