window.addEventListener('DOMContentLoaded', function() {
  const form = document.getElementById("calc-form");
  if (form) {
    setupIntialValues(0, 0, 0);
    form.addEventListener("submit", function(e) {
      e.preventDefault();
     console.log(update());
    });
  }
});

function getCurrentUIValues() {
  return {
    amount: +(document.getElementById("loan-amount").value),
    years: +(document.getElementById("loan-years").value),
    rate: +(document.getElementById("loan-rate").value),
  }
}

// Get the inputs from the DOM.
// Put some default values in the inputs
// Call a function to calculate the current monthly payment

const loanAmount = document.querySelector('#loan-amount')
const termInYears = document.querySelector('#loan-years')
const yearlyRate = document.querySelector('#loan-rate')

function setupIntialValues() {
  const initialValues  = { amount: 10000, years: 3, rate: 2.3 };

  const lonAmountUI = document.getElementById("loan-amount");
  lonAmountUI.value = initialValues.amount;

  const termInYearsUI = document.getElementById("loan-years");
  termInYearsUI.value = initialValues.years;

  const YearlyRateUI = document.getElementById("loan-rate");
  YearlyRateUI.value = initialValues.rate;

  update();

}

// Get the current values from the UI
// Update the monthly payment
function update() {

  const currentValuesUi =  getCurrentUIValues()

  updateMonthly(calculateMonthlyPayment(currentValuesUi))

}

// Given an object of values (a value has amount, years and rate ),
// calculate the monthly payment.  The output should be a string
// that always has 2 decimal places.
function calculateMonthlyPayment(values) {

  const montlyRate = (values.rate / 100) /12
  const n = Math.floor(values.years * 12)
  return (
    (montlyRate * values.amount) / (1 - Math.pow((1 + montlyRate), -n))
  ).toFixed(2)

}

// Given a string representing the monthly payment value,
// update the UI to show the value.
function updateMonthly(monthly) {
  const monthlyUI = document.querySelector('#monthly-payment')
  monthlyUI.innerText = `$ ${monthly}`
}
