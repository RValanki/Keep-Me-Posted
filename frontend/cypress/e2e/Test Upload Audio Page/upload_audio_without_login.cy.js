/**
 * File by: Ayesha Tariq
 * File name: uploadAudio.cy.js
 * This file utilises cypress module to perform front-end testing
 * This page consists of tests that test all functionality and features that exist on the upload_audio page.
 */
import 'cypress-file-upload'
//Testing audio upload page

describe('Audio Upload Page without login', () => {
  
    beforeEach(() => {
      cy.visit('http://localhost:5173/upload_audio'); // Visit the upload audio page page
    });
    //test if the link includes the correct name
    it('should redirect to upload_audio page', () => {
        cy.url().should('include', '/upload_audio');
      });
    
    it('should have the correct page title', () => {
    cy.title().should('include', 'Upload Meeting Audio'); // Checking that the title of page is correct
    });
    //checking that the subheading of the page is correct
    it('should have the correct subheading', () => {
        cy.get(".subheading.mb-16.mt-4").should('contain.text','Upload your meeting audio for us to summarise.');
        });
        //checking if an audio upload button exists on the page
    it('should have audio upload button', () => {
        cy.get('div[role="button"].dropzone.svelte-817dg2').should('exist');
    });
    //mocking click of the button
    it('should click audio upload button', () => {
        cy.get('div[role="button"].dropzone.svelte-817dg2').click();
    }); 

    });