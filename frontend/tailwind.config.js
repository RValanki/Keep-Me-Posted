/** @type {import('tailwindcss').Config} */
/** @type {import('flowbite/plugin').flowbitePluginType} */

export default {
  content: [
    './src/**/*.{html,js,svelte,ts}',
    './node_modules/flowbite-svelte/**/*.{html,js,svelte,ts}'
  ],
  theme: {
    extend: {
        colors: {
             'light-blue': '#f5faff',
             'medium-blue': '#84caff',
             'blue-800': '#1849a9',
             'gray-400': '#98a2b3',
             'gray-700': '#344054',
             'success-25': '#F6FEF9',
             'success-100': '#D1FADF',
             'success-300': '#6CE9A6',
             'success-700': '#027A48'
             },
        },
        fontFamily: {
          inter: ['Inter', 'sans-serif'],
        }
  },
  plugins: [
    require('flowbite/plugin')
    ]
};