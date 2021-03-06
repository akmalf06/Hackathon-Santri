module.exports = {
	purge: ['./src/**/*.{js,jsx,ts,tsx}', './public/index.html'],
	darkMode: false, // or 'media' or 'class'
	theme: {
		extend: {
			colors: {
				main: '#17AA9E',
				'main-dark': '##138f85',
				warn: '#AA1717',
			},
		},
	},
	variants: {
		extend: {},
	},
	plugins: [],
};
