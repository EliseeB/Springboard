
it('should calculate the monthly rate correctly', function () {
  const values = {
    amount: 10000,
    years: 3,
    rate: 2.3,
  }

  expect(calculateMonthlyPayment(values)).toEqual('287.74')

});


it("should return a result with 2 decimal places", function() {
  
  const values = {
    amount: 110000,
    years: 3,
    rate: 2.3,
  }

  expect(calculateMonthlyPayment(values)).toEqual('3165.11')
  

}); 

/// etc
