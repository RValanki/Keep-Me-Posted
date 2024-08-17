// Test the Skip Login Functionality  
describe('Login Page', () => {
    // Visit the summary sent page before each test
    beforeEach(() => {
      // Defining the base URL 
      const baseUrl = 'http://localhost:5173';
      cy.visit(baseUrl+"/login"); 
    });
    // Test the Continue Without an Account Button
    it('should redirect to the upload audio page after clicking the "Continue Without an Account" button', () => {
      // Add a waiting period 
      cy.wait(10000)
      // Click the button labelled "Send Another Summary"
      cy.contains('Continue Without an Account').click()
      // Verify that the URL contains "/email" after clicking the button
      cy.url().should('include', '/upload_audio')
    })
  });
  