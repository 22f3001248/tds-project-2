# happiness.csv Dataset

Analysis for the happiness.csv dataset.
# Comprehensive Report on Life Quality Indicators Dataset

## Summary of the Dataset

This dataset provides an extensive overview of various life quality indicators across different countries over the years. The following variables are included:

- **Country name**: The name of the country.
- **Year**: The specific year of the observation.
- **Life Ladder**: A measure of subjective well-being and happiness.
- **Log GDP per capita**: The logarithm of the Gross Domestic Product per capita, which reflects the economic standing of a nation.
- **Social support**: Reflects the perceived support received from friends, family, and community.
- **Healthy life expectancy at birth**: The average number of years a newborn is expected to live in good health.
- **Freedom to make life choices**: Index measuring the level of autonomy individuals feel in making their own life choices.
- **Generosity**: A measure reflecting a country's altruism.
- **Perceptions of corruption**: Represents the level of perceived corruption in government and public institutions.
- **Positive affect**: The extent of positive emotions experienced by individuals.
- **Negative affect**: The extent of negative emotions experienced by individuals.

### Data Types

The dataset contains mixed types of data:

| Column Name                          | Data Type      |
|--------------------------------------|-----------------|
| Country name                         | Object (String) |
| Year                                 | Integer         |
| Life Ladder                          | Float           |
| Log GDP per capita                   | Float           |
| Social support                       | Float           |
| Healthy life expectancy at birth      | Float           |
| Freedom to make life choices         | Float           |
| Generosity                            | Float           |
| Perceptions of corruption             | Float           |
| Positive affect                       | Float           |
| Negative affect                       | Float           |

### Missing Values

Notably, several columns contain missing values as outlined below:

| Column Name                          | Missing Values |
|--------------------------------------|-----------------|
| Log GDP per capita                   | 28              |
| Social support                        | 13              |
| Healthy life expectancy at birth      | 63              |
| Freedom to make life choices         | 36              |
| Generosity                            | 81              |
| Perceptions of corruption             | 125             |
| Positive affect                       | 24              |
| Negative affect                       | 16              |

### Summary Statistics

The summary statistics of the dataset provide valuable insights into each variable:

- **Countries**: A total of 2363 observations across 165 unique countries, with Argentina appearing most frequently (18 occurrences).
- **Years**: The dataset spans from 2005 to 2023, with an average year of 2014.76.
- **Life Ladder**:
  - Mean: 5.48 
  - Standard Deviation: 1.13 
  - Range: 1.28 – 8.02

- **Log GDP per capita**:
  - Mean: 9.40
  - Standard Deviation: 1.15
  - Range: 5.53 – 11.68

- **Social Support**:
  - Mean: 0.81
  - Standard Deviation: 0.12
  - Range: 0.23 – 0.99

- **Healthy Life Expectancy at Birth**:
  - Mean: 63.40
  - Standard Deviation: 6.84
  - Range: 6.72 – 74.60

- **Freedom to Make Life Choices**:
  - Mean: 0.75
  - Standard Deviation: 0.14
  - Range: 0.23 – 0.99

- **Generosity**:
  - Mean: ~0.0001
  - Standard Deviation: 0.16
  - Range: -0.34 – 0.70

- **Perceptions of Corruption**:
  - Mean: 0.74
  - Standard Deviation: 0.18
  - Range: 0.04 – 0.98

- **Positive Affect**:
  - Mean: 0.65
  - Standard Deviation: 0.11
  - Range: 0.18 – 0.88

- **Negative Affect**:
  - Mean: 0.27
  - Standard Deviation: 0.09
  - Range: 0.08 – 0.71

## Insights

Currently, no specific insights have been derived from the dataset.

## Visualizations

![Output Visualization](output.png)

---

This report outlines the comprehensive summary of the Life Quality Indicators dataset, including summary statistics, data types, and the treatment of missing values. Further analysis and visual exploration might uncover insights into the relationships between economic, social, and emotional well-being across different nations.