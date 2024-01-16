// Base URL for the API
const BASE_URL = "http://localhost:5000/api";

/**
 * Given data about a cupcake, generate HTML for display.
 * @param {Object} cupcake - The cupcake data object.
 * @returns {string} - The HTML string for the cupcake.
 */
function generateCupcakeHTML(cupcake) {
    return `
    <div data-cupcake-id=${cupcake.id}>
      <li>
        ${cupcake.flavor} / ${cupcake.size} / ${cupcake.rating}
        <button class="delete-button">X</button>
      </li>
      <img class="Cupcake-img"
            src="${cupcake.image}"
            alt="(no image provided)">
    </div>
  `;
}

/**
 * Fetch and display the initial list of cupcakes on the page.
 */
async function showInitialCupcakes() {
    const response = await axios.get(`${BASE_URL}/cupcakes`);

    for (let cupcakeData of response.data.cupcakes) {
        let newCupcake = $(generateCupcakeHTML(cupcakeData));
        $("#cupcakes-list").append(newCupcake);
    }
}

// Event listener for the form submission to add a new cupcake
$("#new-cupcake-form").on("submit", async function (evt) {
    evt.preventDefault();

    // Get the values from the form inputs
    let flavor = $("#form-flavor").val();
    let rating = $("#form-rating").val();
    let size = $("#form-size").val();
    let image = $("#form-image").val();

    // Post the new cupcake data to the server
    const newCupcakeResponse = await axios.post(`${BASE_URL}/cupcakes`, {
        flavor,
        rating,
        size,
        image
    });

    // Add the new cupcake to the list
    let newCupcake = $(generateCupcakeHTML(newCupcakeResponse.data.cupcake));
    $("#cupcakes-list").append(newCupcake);
    // Reset the form after submission
    $("#new-cupcake-form").trigger("reset");
});

// Event listener for delete button clicks to remove cupcakes
$("#cupcakes-list").on("click", ".delete-button", async function (evt) {
    evt.preventDefault();
    let $cupcake = $(evt.target).closest("div");
    let cupcakeId = $cupcake.attr("data-cupcake-id");

    // Send a delete request to the server
    await axios.delete(`${BASE_URL}/cupcakes/${cupcakeId}`);
    // Remove the cupcake element from the page
    $cupcake.remove();
});

// Call the function to show initial cupcakes when the DOM is ready
$(showInitialCupcakes);