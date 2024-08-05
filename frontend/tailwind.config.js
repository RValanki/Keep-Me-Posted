/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{html,js,svelte,ts}'],
  theme: {
    extend: {
        colors: {
            'light-blue': '#f5faff',
             'medium-blue': '#84caff',
             'blue-800': '#1849a9',
             'gray-400': '#98a2b3'
             },
        },
        fontFamily: {
          inter: ['Inter', 'sans-serif'],
        }
  },
  plugins: []
};