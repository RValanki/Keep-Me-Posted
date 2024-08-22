import { defineConfig } from "cypress";

export default defineConfig({
  projectId: '2ciyzj',
  e2e: {
    setupNodeEvents(on, config) {
      // implement node event listeners here
    },
  },
  retries: {
    runMode: 3,
    openMode: 1,
  },
});
