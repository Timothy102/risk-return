# VC Investment Analysis App

This Streamlit app is designed to assist venture capital investors in analyzing potential investment opportunities. It allows users to input investment parameters, define different scenarios, and visualize the cumulative investment across financing rounds for each scenario. Additionally, it calculates key performance metrics such as cash flow at exit, gross investment multiple, and return on investment (ROI) for each scenario.

## How to Use

1. **Input Investment Parameters**: Enter the investment amount and the discount risk rate as a percentage.

2. **Define Scenarios**: Define different scenarios representing the worst case, expected case, and best case outcomes for the investment. For each scenario, specify the exit multiple and dilution rate.

3. **View Cumulative Investment**: The app generates bar plots showing the cumulative investment across financing rounds for each scenario. Each scenario is represented by a distinct color.

4. **Analyze Performance Metrics**: The app calculates and displays key performance metrics for each scenario, including cash flow at exit, gross investment multiple, and ROI.

5. **Disclaimer**: Please note that this app provides a simplified analysis and should not be used as the sole basis for investment decisions. Actual investment analysis involves complex calculations, risk assessments, and market considerations. Always consult with financial professionals before making investment decisions.

## How to Run

To run the app locally, make sure you have Python installed. Then, install the required dependencies by running:

```bash
pip install streamlit matplotlib