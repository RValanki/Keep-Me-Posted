// Test the home page

describe('Home Page', () => {
    // Define the base URL if not set in Cypress config
    const baseUrl = 'http://localhost:5173';
  
    // Run before each test
    beforeEach(() => {
      cy.visit(baseUrl); // Visit the home page
    });
  
    it('should redirect to login page', () => {
      cy.url().should('include', '/login');
    });
  
    it('should have the correct page title', () => {
      cy.title().should('include', 'Keep Me Posted'); // Check that the page title includes "Home"
    });
  
  });
  