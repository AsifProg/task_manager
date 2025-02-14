module.exports = {
    darkMode: 'class',
    content: [
        '../templates/**/*.html',
        './node_modules/flowbite/**/*.js',
        '../../templates/**/*.html',
        '../../**/templates/**/*.html',
    ],
    theme: {
        extend: {
            colors: {
                primary: {
                    "50":"#d2a1ed",
                    "100":"#c587e8",
                    "200":"#b86ce3",
                    "300":"#ab51de",
                    "400":"#9f37d8",
                    "500":"#8f27c8",
                    "600":"#7c21ae",
                    "700":"#691c93",
                    "800":"#561778",
                    "900":"#43125e",
                    "950":"#300d43"
                }
            }
        },
    },
    plugins: [
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/line-clamp'),
        require('@tailwindcss/aspect-ratio'),
        require('flowbite/plugin')
    ],
    fontFamily: {
        'body': [
            'Inter', 
            'ui-sans-serif', 
            'system-ui', 
            '-apple-system', 
            'system-ui', 
            'Segoe UI', 
            'Roboto', 
            'Helvetica Neue', 
            'Arial', 
            'Noto Sans', 
            'sans-serif', 
            'Apple Color Emoji', 
            'Segoe UI Emoji', 
            'Segoe UI Symbol', 
            'Noto Color Emoji'
    ],
        'sans': [
            'Inter', 
            'ui-sans-serif', 
            'system-ui', 
            '-apple-system', 
            'system-ui', 
            'Segoe UI', 
            'Roboto', 
            'Helvetica Neue', 
            'Arial', 
            'Noto Sans', 
            'sans-serif', 
            'Apple Color Emoji', 
            'Segoe UI Emoji', 
            'Segoe UI Symbol', 
            'Noto Color Emoji'
    ]
    },
}
