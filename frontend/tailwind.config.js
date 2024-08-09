/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{html,js,svelte,ts}'],
  theme: {
    extend: {
        colors: {
            'light-blue': '#f5faff',
             'medium-blue': '#84caff',
             'blue-800': '#1849a9',
             'gray-900': '#101828',
             'gray-700': '#344054',
             'gray-500': '#667085',
             'gray-400': '#98a2b3',
             'gray-300': '#d0d5dd'
             },
        },
        fontFamily: {
           inter: ['Inter']
        }
  },
  plugins: []
};