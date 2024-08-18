/**
 * The file contains the test cases for the emailing page.
 */

// Access email page test cases
describe("Access email page", () => {
  beforeEach(() => {
    cy.visit("/email");
    cy.contains("Add Recipients").should("be.visible"); // Check for "Add Recipients" Label
    cy.get('input[type="email"]').should("be.visible"); // Check for Email Input
  });
});

// Test valid recipient add
describe("Valid Email Input", () => {
  it("should allow adding a valid email and update the ContactsStore", () => {
    // Visit the email page
    cy.visit("/email");

    // Mock the ContactsStore update function
    cy.window().then((win) => {
      // Spy on the ContactsStore update method
      cy.spy(win.ContactsStore, "update").as("updateSpy");
    });

    // Enter a valid email
    const validEmail = "test@example.com";
    cy.get('input[type="email"]').type(validEmail);

    // Click the "Add recipient" button
    cy.contains("Add recipient").click();

    // Check that ContactsStore.update was called with the correct arguments
    cy.get("@updateSpy").should("have.been.calledOnce");
    cy.get("@updateSpy").should(
      "have.been.calledWith",
      Cypress.sinon.match.func
    );
  });
});

// Test invalid recipient add
describe("Invalid Email Access", () => {
  it("should display an error message for an invalid email", () => {
    // Visit the email page
    cy.visit("/email");

    // Enter an invalid email
    const invalidEmail = "invalid-email";
    cy.get('input[type="email"]').type(invalidEmail);

    // Click the "Add recipient" button
    cy.contains("Add recipient").click();

    // Check that the error message is displayed
    cy.get('[data-testid="error-message"]').should(
      "contain",
      "Please enter a valid email address"
    );

    // Verify that ContactsStore.update was not called
    cy.window().then((win) => {
      cy.spy(win.ContactsStore, "update").should("not.have.been.called");
    });
  });
});
