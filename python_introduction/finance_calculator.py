m_income = int(input("Enter your monthly income: "))
m_expenses = int(input("Enter your total montly expenses: "))
m_savings = m_income - m_expenses

y_savings = m_savings * 12 + (m_savings * 12 * 0.05)

print(f"Your monthly savings are ${m_savings}")
print(f"Projected savings after one year, with interest, is: ${y_savings}")

