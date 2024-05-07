# Exchange rates (as of May 2024)
exchange_rates = {
    "COP": 0.00027,  # Colombian pesos to USD
    "PEN": 0.28,     # Peruvian soles to USD
    "BRL": 0.19      # Brazilian reais to USD
}

# Get user input for remaining amounts
CP = int(input("What do you have left in pesos? "))
PS = int(input("What do you have left in soles? "))
BR = int(input("What do you have left in reais? "))

# Calculating the total amount in USD
total_usd = CP * exchange_rates["COP"] + PS * exchange_rates["PEN"] + BR * exchange_rates["BRL"]

# Output the result
print("Cha-ching! Now you have ${:.2f} in USD. 💰".format(total_usd))

#In Python, "${:.2f}" is a string formatting expression used to format a floating-point number with two decimal places and include a dollar sign ($) before the number.
