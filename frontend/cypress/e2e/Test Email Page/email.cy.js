/**
 * The file contains the test cases for the emailing page.
 */

// Test Access email page test cases
describe("Access email page", () => {
    beforeEach(() => {
        cy.visit("/email");
    });

    it("contain correct fields", () => {
        cy.contains("Add Recipients").should("be.visible"); // Check for "Add Recipients" Label
        cy.get('input[type="email"]').should("be.visible"); // Check for Email Input
    }
    );
    });
  
// Test valid recipient add
describe("Mocking ContactsStore", () => {
    beforeEach(() => {
      cy.visit("/email");
  
      // Mock the ContactsStore with a spy
      cy.window().then((win) => {
        const mockContactsStore = {
          update: cy.spy().as("mockUpdate"), // Spy on the update method
        };

      // Replace the actual ContactsStore with the mock
      win.ContactsStore = mockContactsStore;

      // Capture console logs
      cy.spy(win.console, 'log').as('consoleLog');
      });
    });
  
    it("should call update on adding a valid email", () => {
      const validEmail = "test@example.com";
      
      cy.get('input[type="email"]').type(validEmail);
      cy.contains("Add recipient").click();

      // Verify console log
      cy.get('@consoleLog').should('be.calledWith', 5);
  
      // Check that the update method was called
      cy.get("@mockUpdate").should("have.been.calledOnce");
    });
  });
  
