describe('Sign Up Page', () => {
  
    beforeEach(() => {
      // Navigate to the sign-up page before each test
      cy.visit('http://localhost:5173/signup'); // Adjust the URL if needed
    });
  
    it('should display validation error for invalid email', () => {
      cy.get('input[name="email"]')
        .type('invalid-email')
        .blur(); // Trigger validation
  
      cy.contains('Please Enter Valid Email').should('be.visible'); // Check for validation error
    });
  
    it('should display validation error for weak password', () => {
      cy.get('input[name="password"]')
        .type('weakpass')
        .blur(); // Trigger validation
  
      cy.contains('Password must contain at least 8 characters, capital letters, and a special character')
        .should('be.visible'); // Check for validation error
    });
  
    it('should display validation error if passwords do not match', () => {
      cy.get('input[name="password"]')
        .type('ValidPass123!');
  
      cy.get('input[name="verifyPassword"]')
        .type('DifferentPass123!')
        .blur(); // Trigger validation
  
      cy.contains('Password does not match').should('be.visible'); // Check for validation error
    });
  
    it('should sign up successfully with valid credentials', () => {
      cy.get('input[name="email"]')
        .type('valid.email@example.com');
  
      cy.get('input[name="password"]')
        .type('ValidPass123!');
  
      cy.get('input[name="verifyPassword"]')
        .type('ValidPass123!');
  
      cy.get('button[type="submit"]')  // Target the "Sign Up" button
        .contains('Sign Up')
        .click();
  
      // Assuming successful signup redirects to the login page
      cy.url().should('include', '/login'); 
    });
  
    it('should initiate Google sign up', () => {
      cy.get('button[type="button"]')
        .contains('Sign Up with Google')
        .should('be.visible')
        .click(); // Click the Google Sign-Up button
  
      // Check if the redirection to Google OAuth happens
      cy.url().should('include', 'accounts.google.com');
    });
  
  });
  