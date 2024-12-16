# goodreads.csv Dataset

Analysis for the goodreads.csv dataset.
# Analysis Report on Goodreads Book Dataset

## Dataset Overview

The dataset comprises information related to **10,000 books**, predominantly sourced from Goodreads, presenting various attributes such as book IDs, authors, average ratings, number of ratings, and publication years. Below is a summary of the key features along with insights drawn from the analysis.

---

## 1. Attributes and Data Quality

### Missing Values

While the dataset is relatively comprehensive, several attributes exhibit missing values that may influence data integrity:

- **ISBN**: 700 missing values
- **ISBN13**: 585 missing values
- **Original Publication Year**: 21 missing values
- **Original Title**: 585 missing values
- **Language Code**: 1,084 missing values

These gaps indicate areas for potential improvement and caution when conducting analyses that depend on these fields.

### Data Types

Most columns are appropriately formatted. Numeric fields are largely represented as integers, while text fields use object types. However, a few numeric attributes are stored as `float64` when integers would suffice, indicating possible optimization opportunities.

---

## 2. Author Representation

The dataset encompasses **4,664 unique authors**. Notably, **Stephen King** is the most frequently appearing author with **60 mentions**. This highlights a concentration in popular authors, suggesting that they may significantly influence readership and ratings. This aspect warrants further exploration into the dynamics of popularity and reader preference.

---

## 3. Publication Year Analysis

The **mean original publication year** is approximately **1982**, with a publication range extending from as early as 1750 to 2017. This dataset's temporal depth provides a rich field for analysis of trends in publishing and shifts in reader demographics over time, particularly in relation to generational reading habits.

---

## 4. Ratings and Reviews Landscape

### Average Ratings

The average rating across the dataset stands at **4.00**, indicating a generally positive reception of the books. The standard deviation of **0.25** illustrates a moderate consistency in ratings, with the majority of books clustering around this score.

### Ratings Count

On average, books receive **54,001 ratings**, although there's significant variability, with the highest book accruing **4,780,653 ratings**. A study focused on these standout books could reveal factors contributing to their popularity.

### Text Reviews

Books in the dataset average approximately **2,919 text reviews** each, signaling a robust level of community engagement. Analyzing how text reviews relate to average ratings could yield insights into reviewer behavior and opinion dynamics in relation to scoring.

---

## 5. Rating Distribution

The breakdown of ratings illustrates a pronounced preference for high scores:

- **1 star**: 1,345 ratings
- **2 stars**: 3,110 ratings
- **3 stars**: 11,475 ratings
- **4 stars**: 19,966 ratings
- **5 stars**: 23,790 ratings

The high averages suggest quality control in the dataset, raising questions about what aspects (e.g., author, genre, publication year) encourage higher ratings. 

---

## 6. Language Distribution

English is the dominant language in the dataset, with **6,341 instances** (approximately 71% of the dataset), followed by a variety of other language entries (25 unique codes). This prevalence underscores a potential bias toward English literature, potentially skewing analyses that aim to encompass broader linguistic trends.

---

## Conclusion and Future Analysis Directions

This dataset serves as a foundational resource for investigating contemporary reading trends, author prominence, publication histories, and bibliometric metrics. The following future analysis directions are proposed:

1. **Correlation Studies**: Investigating the relationship between `original_publication_year` and `average_rating` to discern if newer books consistently excel in ratings.
2. **Author Clustering**: Understanding the concentration of particular authors or genres to reveal insights into literary dominance.
3. **Sentiment Analysis**: Comparing textual feedback from reviews to numeric ratings to see if textual sentiment aligns with numerical scores.
4. **Language Impact**: Exploring how language diversity affects ratings and reviews, examining whether non-English titles garner similar engagement.
5. **Dealing with Missing Data**: Assessing the implications of missing values, particularly in critical fields such as `isbn`, `original_title`, and `language_code`, on overall data quality.

While the dataset is rich in content, its missing pieces require contextual scrutiny, paving the way for valuable literary insights and community engagement strategies aligned with reader preferences and publication trends.

---

![Output Visualization](output.png)