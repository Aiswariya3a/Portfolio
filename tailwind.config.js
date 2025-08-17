// tailwind.config.js
const defaultTheme = require('tailwindcss/defaultTheme')

/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
      './templates/**/*.html',
      './mysite/templates/**/*.html',
      './mysite/forms.py',
  ],
  theme: {
    extend: {
      colors: {
        'midnight': '#111827', // A deep, dark blue
        'charcoal': '#1F2937', // A slightly lighter charcoal
        'neon-teal': '#2DD4BF',
        'neon-purple': '#A78BFA',
        'neon-coral': '#F472B6',
        'neon-gold': '#FBBF24',
      },
      fontFamily: {
        // Add Poppins as the default sans-serif font
        sans: ['Poppins', ...defaultTheme.fontFamily.sans],
        // Add a playful display font for headings
        display: ['Audiowide', 'cursive'],
      },
    },
  },
  plugins: [
    require('@tailwindcss/typography'),
  ],
}