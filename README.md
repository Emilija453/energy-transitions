# Energy Transitions Project Overview

This project focuses on exploring energy transitions, particularly in Lithuania and the Baltic region, along with a global perspective. Utilizing Plotly.js, interactive visualizations depict energy-related data, offering insights into consumption, production, critical materials, and transition trends over time.

## Structure
The project data undergoes analysis in Jupyter Notebooks, where it's processed, visualized, and transformed into interactive insights before being transferred to HTML for presentation. 

- **Data Analysis**: Raw energy-related datasets are explored, cleaned, and processed within Jupyter Notebooks.
  
- **Visualization**: Interactive visualizations depicting energy trends for Vilnius, Klaipeda, and Panevezys are created using tools like Plotly.js.
  
- **Insight Generation**: Insights into energy consumption, production, and transition trends are derived through statistical analysis and data visualization techniques.
  
- **HTML Output**: The processed data and visualizations are rendered into HTML documents, allowing for easy viewing and interaction by users.
  
## Content
### Vilnius, Klaipeda and Panevezys Energy Analysis
- **Hourly Trends**: Visualizes energy generation and consumption hourly averages.
- **Daily Comparison**: Compares daily energy trends.
- **Net Energy Balance**: Illustrates the net energy balance over time.
- **Weather Influence**: Examines weather variables' impact on energy production and consumption.

#### Data Source: [Ignitis](https://ignitisinnovation.com/what-we-do/open-data/)

---

### Energy Analysis in the Baltic Region
Explores energy trends in the Baltic region, focusing on Lithuania, through visualizations of production by source, renewables, electricity generation, and imports.

- **Energy Production**: Covers trends in various energy sources.
- **Electricity Production**: Analyzes generation sources.
- **Renewable Energy**: Focuses on renewable production.
- **Renewable Share**: Compares renewable electricity across Baltic countries.
- **Electricity Imports**: Examines net imports in select Baltic countries.

#### Data Source: [International Energy Agency](https://www.iea.org/data-and-statistics/data-product/world-energy-statistics-and-balances), [Our World in Data](https://ourworldindata.org/energy)

---

### Global Energy and Mineral Analysis
Visualizes electricity imports and critical mineral trade data, offering insights into regional energy dynamics and mineral demands.

- **Electricity Imports**: Trends of net imports across regions.
- **Top Exporters/Importers of Critical Minerals (2022)**: Highlights top exporters/importers and their values.
- **Predicted Demand for Critical Minerals**: Analyzes predicted demand for critical minerals under different scenarios.

#### Data Source: [Our World in Data](https://ourworldindata.org/energy), [International Energy Agency](https://www.iea.org/reports/critical-minerals-market-review-2023)

---

### Machine Learning Model
Utilizes Random Forest Regression to predict total demand for critical minerals in comparison to the International Energy Agencie's Global Energy and Climate Model.
- **Predicted vs Real Total Demand**: Compares predicted and real demands.
- **Error Analysis**: Plots residuals for error analysis.
- **Test Size Sensitivity Analysis**: Examines model performance sensitivity.
- **Predictions**: Generates predictions for specific scenarios.

**Scenarios**:
- **The Stated Policies Scenario** serves as a benchmark to evaluate current energy and climate policies' achievements and limitations, emphasizing the "implementation gap" between current policies and announced decarbonization targets.
- **The Announced Pledges Scenario** assesses current climate commitments' contribution to limiting global warming to 1.5 °C, highlighting the "ambition gap" between current pledges and the Paris Agreement's level of ambition.
- **The Net Zero Emissions by 2050 Scenario** outlines a pathway for achieving global net zero CO2 emissions by 2050, emphasizing universal access to electricity and clean cooking by 2030.

#### Data Source: [International Energy Agency](https://www.iea.org/data-and-statistics/data-tools/critical-minerals-data-explorer)