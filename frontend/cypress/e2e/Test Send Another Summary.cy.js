// Test the Summary Sent Page 
describe('Summary Sent Page', () => {
    // Visit the summary sent page before each test
    beforeEach(() => {
      cy.visit("/send_summary"); 
      // Add a waiting period 
      cy.wait(10000)
    });
    // Test the Send Summary Button
    it('should redirect to the send email page after clicking the "send another summary" button', () => {
      // Click the button labelled "Send Another Summary"
      cy.contains('button','Send Another Summary').click()
      // Verify that the URL contains "/email" after clicking the button
      cy.url().should('include', '/email')
    })
  });  