import { defineConfig } from "cypress";
import fileUpload from "cypress-file-upload";


export default defineConfig({
  projectId: '2ciyzj',
  e2e: {
    setupNodeEvents(on, config) {
      // implement node event listeners here
      on('file:preprocessor', fileUpload()); // Registering the file upload plugin
    },
    baseUrl: 'http://localhost:5173',
  },
  retries: {
    runMode: 3,
    openMode: 1,
  },
});
