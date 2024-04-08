import streamlit as st
import matplotlib.pyplot as plt

# Function to calculate cash flow at exit (replace with your model)
def calculate_exit_value(investment_amount, exit_multiple, dilution):
    # This example uses a simple exit multiple on initial investment
    return investment_amount * (1 - dilution) * exit_multiple

# Streamlit app
st.title("VC Investment Analysis")

# Pretext
st.markdown("""
### Welcome to the VC Investment Analysis App

This app is designed to assist venture capital investors in analyzing potential investment opportunities. 
Enter your investment parameters, define different scenarios, and visualize the cumulative investment across financing rounds for each scenario. 
Additionally, key performance metrics such as cash flow at exit, gross investment multiple, and return on investment (ROI) are calculated and displayed for each scenario.

Please input your investment amount and defined risk discount factor and define scenarios in the sidebar on the left.
""")

# Investment parameters
investment_amount = st.sidebar.number_input("Investment amount (in millions)", min_value=0.0) * 1e6  # Convert to millions
discount_rate = st.sidebar.number_input("Discount risk rate (in %)", min_value=0.0)

# Scenario definitions (replace with your estimates)
scenarios = {
    "Worst Case": {"exit_multiple": 2.0, "dilution": 0.20},
    "Expected Case": {"exit_multiple": 5.0, "dilution": 0.10},
    "Best Case": {"exit_multiple": 10.0, "dilution": 0.05},
}

# Financing round definitions (replace with your estimates)
rounds = [
    {"name": "Seed", "investment_percentage": 0.10},
    {"name": "Series A", "investment_percentage": 0.20},
    {"name": "Series B", "investment_percentage": 0.30},
    {"name": "Series C", "investment_percentage": 0.40},
]

# Calculate total VC investment across rounds
total_vc_investment = 0
for round in rounds:
    investment_in_round = investment_amount * round["investment_percentage"]
    total_vc_investment += investment_in_round

# Calculate cash flow at exit for each scenario
scenario_data = {}
for scenario_name, scenario_values in scenarios.items():
    exit_multiple = scenario_values["exit_multiple"]
    dilution = scenario_values["dilution"]
    cash_flow_at_exit = calculate_exit_value(total_vc_investment, exit_multiple, dilution)
    scenario_data[scenario_name] = cash_flow_at_exit

# Cumulative investment for each round across scenarios (avoid redundancy)
round_investments = {scenario_name: [] for scenario_name in scenarios.keys()}
for round in rounds:
    investment_in_round = investment_amount * round["investment_percentage"]
    for scenario_name in scenario_data.keys():
        round_investments[scenario_name].append(investment_in_round)

# Create separate bar plots for each scenario with distinct colors
scenario_colors = ["green", "blue", "orange"]  # Customize colors as needed
for i, (scenario_name, round_values) in enumerate(round_investments.items()):
    plt.figure(figsize=(10, 6))
    plt.bar([round["name"] for round in rounds], round_values, color=scenario_colors[i], label=scenario_name)
    plt.xlabel("Financing Round")
    plt.ylabel("Cumulative Investment (Millions)")
    plt.title(f"Cumulative Investment Across Rounds ({scenario_name})")
    plt.grid(axis='y')
    plt.legend()
    st.pyplot(plt)

# Display additional information for VC investors (assuming successful exit)
for scenario_name, cash_flow in scenario_data.items():
    gross_investment_multiple = cash_flow / investment_amount
    roi = gross_investment_multiple - 1

    st.write(f"{scenario_name} Performance:")
    st.write(f"- Cash Flow at Exit: {cash_flow:.2f} millions")
    st.write(f"- Gross Investment Multiple: {gross_investment_multiple:.2f}x")
    st.write(f"- ROI: {roi:.2%}")

st.info("**Disclaimer:** This is a simplified example. Actual VC investment analysis involves complex calculations, risk assessments, and market considerations. Please consult with financial professionals for real-world investment decisions.")