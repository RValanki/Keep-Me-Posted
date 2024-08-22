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
        cy.get('button').contains("Add Recipient").should("be.visible"); // Check for "Add Recipient" Button
        cy.get('input[type="email"]').should("be.visible"); // Check for Email Input
    }
    );

    });
  
// Test valid recipient add
describe("Valid recipient add", () => {
    beforeEach(() => {
      cy.visit("/email");

    });
  
    it("should call update on adding a valid email", () => {
      cy.get('input[type="email"]').type("success@gmail.com");
      cy.get('input[type="email"]').type("testsuccess@gmail.com").should('have.value', 'testsuccess@gmail.com');
      cy.wait(1000);
      cy.get('button').contains('Add Recipient').click();

      // Check that valid email was added
      cy.contains("testsuccess@gmail.com").should("be.visible");
    });

  });

// Test invalid recipient add
describe("Invalid recipient add", () => {
    beforeEach(() => {
      cy.visit("/email");

    });
  
    it("should call update on adding a valid email", () => {
      cy.get('input[type="email"]').type("testfail");
      cy.get('input[type="email"]').type("testfail").should('have.value', 'testfail');
      cy.wait(1000);
      cy.get('button').contains('Add Recipient').click();
  
      // Check that invalid email was not added
      cy.contains("testfail").should("not.exist");
    });

  });
  
  
