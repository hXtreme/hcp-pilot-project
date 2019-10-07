
var search_bar = document.getElementById('home-search-bar');

var search_string = function(s) {
	console.log('search_string(\'' + s + '\')');
};

search_bar.addEventListener('keyup', function(event) {
	if (event.keyCode === 13) {
		event.preventDefault();
		query = document.getElementById('text-field-hero-input').value;
		search_string(query);
	}
});