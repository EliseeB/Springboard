def convert_temp(unit_in, unit_out, temp):
    """Convert farenheit <-> celsius and return results.

    - unit_in: either "f" or "c" 
    - unit_out: either "f" or "c"
    - temp: temperature (in f or c, depending on unit_in)

    Return results of conversion, if any.

    If unit_in or unit_out are invalid, return "Invalid unit [UNIT_IN]".

    For example:

      convert_temp("c", "f", 0)  =>  32.0
      convert_temp("f", "c", 212) => 100.0
    """
   
     # Fahrenheit to Celsius
    
    def fahrenheit_to_celsius():
        Celsius = (temp - 32) * 5/9
        return Celsius
    
    # Celsius to Fahrenheit
    
    def celsius_to_fahrenheit():
        Fahrenheit = (temp * 9/5) + 32 
        return Fahrenheit
    
    # Handles logic. Checks if input_in and input_out are either equal to "c" or "f".
    
    valid_input = unit_in.lower()
    valid_output = unit_out.lower()
    
    
    if valid_input == "c" and valid_output == 'f':
      return celsius_to_fahrenheit()
    
    elif valid_input == 'f' and valid_output == 'c':
      return fahrenheit_to_celsius()
    
    elif valid_input not in ('c', 'f'):
      return f"Invalid input {valid_input}"
    
    elif valid_output not in ('c', 'f'):
      return f"Invalid input {valid_output}"
    
    else:
      return temp
    

print("c", "f", 0, convert_temp("c", "f", 0), "should be 32.0")
print("f", "c", 212, convert_temp("f", "c", 212), "should be 100.0")
print("z", "f", 32, convert_temp("z", "f", 32), "should be Invalid unit z")
print("c", "z", 32, convert_temp("c", "z", 32), "should be Invalid unit z")
print("f", "f", 75.5, convert_temp("f", "f", 75.5), "should be 75.5")

