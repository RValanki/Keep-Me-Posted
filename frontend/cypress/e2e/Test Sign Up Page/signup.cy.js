describe('Sign Up Flow', () => {
  const baseUrl = 'http://localhost:5173'; // Adjust based on your setup
  const apiUrl = 'http://127.0.0.1:8000/signup'; // Your API endpoint

  beforeEach(() => {
    cy.visit(`${baseUrl}/signup`);
  });

  it('should display validation message for invalid email format', () => {
    cy.get('input[placeholder="name@email.com"]').type('invalid-email'); // Input invalid email
    cy.get('input[placeholder="••••••••"]').first().type('ValidPass123!'); // Input valid password
    cy.get('input[placeholder="••••••••"]').last().type('ValidPass123!'); // Input valid password
    cy.get('button').contains('Sign Up').click(); // Attempt to submit

    // Check for the specific error message related to invalid email
    cy.contains('Please Enter Valid Email').should('be.visible');
  });

  it('should display validation message for weak password', () => {
    cy.get('input[placeholder="name@email.com"]').type('test@example.com');
    cy.get('input[placeholder="••••••••"]').first().type('weakpass');
    cy.get('input[placeholder="••••••••"]').last().type('weakpass');
    cy.get('button').contains('Sign Up').click();

    cy.contains('Password must contain at least 8 characters, capital letters, and a special character').should('be.visible');
  });

  it('should display validation message for non-matching passwords', () => {
    cy.get('input[placeholder="name@email.com"]').type('test@example.com');
    cy.get('input[placeholder="••••••••"]').first().type('ValidPass123!');
    cy.get('input[placeholder="••••••••"]').last().type('DifferentPass123!');
    cy.get('button').contains('Sign Up').click();

    cy.contains('Password does not match').should('be.visible');
  });

  it('should successfully submit the form with valid inputs', () => {
    cy.intercept('POST', apiUrl).as('postSignUp');

    cy.get('input[placeholder="name@email.com"]').type('test@example.com');
    cy.get('input[placeholder="••••••••"]').first().type('ValidPass123!');
    cy.get('input[placeholder="••••••••"]').last().type('ValidPass123!');
    cy.get('button').contains('Sign Up').click();

    cy.wait('@postSignUp').its('response.body').should((body) => {
      expect(body).to.have.property('token');
      expect(body).to.have.property('user');
    })

    cy.url().should("include", "/login");
  });

  it('should display an error if the email is already in use', () => {
    cy.intercept('POST', apiUrl, {
      statusCode: 400,
      body: { error: 'This email address is already in use' },
    }).as('postSignUp');

    cy.get('input[placeholder="name@email.com"]').type('existing@example.com');
    cy.get('input[placeholder="••••••••"]').first().type('ValidPass123!');
    cy.get('input[placeholder="••••••••"]').last().type('ValidPass123!');
    cy.get('button').contains('Sign Up').click();

    cy.wait('@postSignUp');
    cy.contains('This email address is already in use').should('be.visible');
  });
});
