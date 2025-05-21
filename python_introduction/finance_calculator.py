# Prompting the user for financial details
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculating monthly savings
monthly_savings = monthly_income - monthly_expenses

# Projecting annual savings with 5% interest
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

# Output results
print(monthly_savings)
print(projected_savings)
