//
const input = document.querySelector('#fruit');

//
const suggestions = document.querySelector('.suggestions ul');

const fruits = ['Apple', 'Apricot', 'Avocado 🥑', 'Banana', 'Bilberry', 'Blackberry', 'Blackcurrant', 'Blueberry', 'Boysenberry', 'Currant', 'Cherry', 'Coconut', 'Cranberry', 'Cucumber', 'Custard apple', 'Damson', 'Date', 'Dragonfruit', 'Durian', 'Elderberry', 'Feijoa', 'Fig', 'Gooseberry', 'Grape', 'Raisin', 'Grapefruit', 'Guava', 'Honeyberry', 'Huckleberry', 'Jabuticaba', 'Jackfruit', 'Jambul', 'Juniper berry', 'Kiwifruit', 'Kumquat', 'Lemon', 'Lime', 'Loquat', 'Longan', 'Lychee', 'Mango', 'Mangosteen', 'Marionberry', 'Melon', 'Cantaloupe', 'Honeydew', 'Watermelon', 'Miracle fruit', 'Mulberry', 'Nectarine', 'Nance', 'Olive', 'Orange', 'Clementine', 'Mandarine', 'Tangerine', 'Papaya', 'Passionfruit', 'Peach', 'Pear', 'Persimmon', 'Plantain', 'Plum', 'Pineapple', 'Pomegranate', 'Pomelo', 'Quince', 'Raspberry', 'Salmonberry', 'Rambutan', 'Redcurrant', 'Salak', 'Satsuma', 'Soursop', 'Star fruit', 'Strawberry', 'Tamarillo', 'Tamarind', 'Yuzu'];

// Function to filter the fruit names based on user input
const search = (str) => {
	
	// Use the filter method to create a new array of matching fruit names
	const results = fruits.filter(fruit => (
	  fruit.toLowerCase().includes(str.toLowerCase()) 
	));
  
	return results;
  }
  
  // Event handler for user input
  const searchHandler = event => {
	// Get the value of the input
	const inputValue = input.value;
  
	// Call the search function to get matching results
	const searchResults = search(inputValue);
  
	// Clear previous suggestions
	suggestions.innerHTML = '';
  
	// Loop through the search results and create suggestion list items
	for (const item of searchResults) {
	  const listItem = document.createElement('li');
	  listItem.innerText = item;
	  suggestions.appendChild(listItem);
  
	  // Clear suggestions if there's no input value
	  if (!inputValue) {
		suggestions.innerHTML = '';
	  }
	}
  }
  
  // Event handler for suggestion selection
  const useSuggestion = event => {
	// Clear suggestions
	suggestions.innerHTML = '';
  
	// Get the selected suggestion's content and set it as the input value
	input.value = event.target.innerText;
  }
  
  // Listen for input events and trigger the searchHandler
  input.addEventListener('input', searchHandler);
  
  // Listen for click events on suggestions and trigger the useSuggestion
  suggestions.addEventListener('click', useSuggestion);