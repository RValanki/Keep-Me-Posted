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
             'gray-700': '#344054'
             },
        },
        fontFamily: {
           inter: ['Inter']
        }
  },
  plugins: [
    require('flowbite/plugin')
    ]
};