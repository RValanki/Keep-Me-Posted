// Test the Skip Login Functionality  
describe('Login Page', () => {
    // Visit the login page before each test
    beforeEach(() => {
      // Defining the base URL 
      const baseUrl = 'http://localhost:5173';
      cy.visit(baseUrl+"/login"); 
    });
    // Test the Continue Without an Account Button
    it('should redirect to the upload audio page after clicking the "Continue Without an Account" button', () => {
      // Add a waiting period 
      cy.wait(10000)
      // Click the button labelled "Continue Without an Account"
      cy.contains('Continue Without an Account').click()

      // Wait for the page to load
      cy.wait(2000)
      
      // Verify that the URL contains "/upload_audio" after clicking the button
      cy.url().should('include', '/upload_audio')
    })
  });