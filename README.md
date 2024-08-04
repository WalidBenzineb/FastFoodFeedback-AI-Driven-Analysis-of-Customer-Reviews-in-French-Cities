# FastFoodFeedback: AI-Driven Analysis of Customer Reviews in French Cities

## Project Overview

This project conducts an in-depth analysis of customer reviews for fast food restaurants in three major French cities: Lyon, Marseille, and Paris. The primary goal is to identify key factors influencing customer satisfaction and dissatisfaction, and to develop targeted, cost-effective strategies for improving customer experience in each city.

## Table of Contents

- [Data Collection](#data-collection)
- [Methodology](#methodology)
- [Key Findings](#key-findings)
- [City-Specific Analysis](#city-specific-analysis)
- [Improvement Strategies](#improvement-strategies)
- [Cross-City Initiatives](#cross-city-initiatives)
- [Implementation Plan](#implementation-plan)
- [Project Structure](#project-structure)
- [How to Run the Project](#how-to-run-the-project)
- [Conclusion](#conclusion)
- [Future Work](#future-work)

## Data Collection

- **Source**: Google Reviews
- **Scope**: Fast food restaurants in Lyon, Marseille, and Paris
- **Sample Size**: Lyon : 11892 reviews, marseille : 13053 reviews and paris : 26240 reviews. Total : 51185 reviews.
- **Data Points**: review text, date of review
- **Ethics**: All data was collected in compliance with Google's terms of service

## Methodology

1. **Data Collection**: Reviews were gathered from Google Reviews using automated data collection techniques.

2. **Data Preprocessing**:
   - Reviews were cleaned to remove irrelevant information and correct formatting issues.
   - Sentiment categorization: 1-3 stars classified as negative, 4-5 stars as positive.

3. **Categorization**:
   Reviews were categorized into six main areas:
   - Food
   - Service
   - Cleanliness
   - Price
   - Ambiance
   - Delivery

4. **Analysis**:
   - Conducted comparative analysis of positive and negative reviews across the three cities.
   - Focused primarily on negative reviews due to their higher impact on business reputation.
   - Calculated percentage distribution of each category within positive and negative reviews.

5. **Visualization**:
   - Created pie charts to visualize the distribution of categories in both positive and negative reviews for each city.
   - Used consistent color coding across all charts for easy comparison.

6. **Strategy Development**:
   - Identified key issues based on the highest percentages of negative reviews in each category.
   - Developed targeted strategies addressing the most significant problems in each city.
   - Created cross-city initiatives to address common issues.

## Key Findings

- Negative reviews have a more significant impact on business reputation and customer retention than positive ones.
- Service and food quality are the top concerns across all three cities, but their relative importance varies.
- Each city has unique secondary concerns that require targeted strategies.

## City-Specific Analysis

### Lyon
![categories_reviews_negatifs_lyon](https://github.com/user-attachments/assets/fe777b88-7e54-4111-a03f-bcdf9af38761)
![categories_reviews_positifs_lyon](https://github.com/user-attachments/assets/f643b2f4-012b-4818-8c45-c3d568f14777)

- **Positive Reviews**:
  - Service: 44.4%
  - Food: 39.5%
- **Negative Reviews**:
  - Service: 41.7%
  - Food: 37.4%
  - Cleanliness: 9.5%
- **Notable**: Highest percentage of delivery-related complaints (2.7%) among the three cities.

### Marseille
![categories_reviews_negatifs_marseille](https://github.com/user-attachments/assets/c865e947-f3cc-49dc-8329-64e68648fe24)
![categories_reviews_positifs_marseille](https://github.com/user-attachments/assets/050c81c0-f165-4653-bd42-2daca7d34d89)

- **Positive Reviews**:
  - Service: 46.4%
  - Food: 35.0%
- **Negative Reviews**:
  - Service: 42.6%
  - Food: 34.6%
  - Cleanliness: 11.5%
- **Notable**: Highest percentage of cleanliness complaints and showed more price sensitivity (5.6%) than Lyon.

### Paris
![categories_reviews_negatifs_paris](https://github.com/user-attachments/assets/68c41663-f9b6-47ea-9226-a87733270c65)
![categories_reviews_positifs_paris](https://github.com/user-attachments/assets/875fddb2-0a34-4199-8e70-9bfdd22a7261)

- **Positive Reviews**:
  - Service: 41.6%
  - Food: 38.4%
- **Negative Reviews**:
  - Food: 37.6%
  - Service: 38.3%
  - Price: 9.4%
- **Notable**: Highest price sensitivity and more ambiance-related complaints (4.0%) than other cities.

## Improvement Strategies

### Lyon

1. **Service Improvement**:
   - Create a concise, one-page "service basics" guide for all staff.
   - Implement daily 5-minute pre-shift briefings focusing on one specific service aspect.

2. **Food Quality Consistency**:
   - Institute daily taste tests of 1-2 menu items by managers.
   - Review and simplify recipes to maintain consistency across staff and shifts.

3. **Delivery Enhancement**:
   - Create a checklist for proper packaging of all items before handoff to drivers.
   - Include a "How was your delivery?" feedback card with all delivery orders.

### Marseille

1. **Service Excellence**:
   - Develop a list of friendly, locally appropriate phrases for customer interactions.
   - Implement a system where staff rotate responsibilities each shift.

2. **Cleanliness Initiative**:
   - Introduce a "clean as you go" policy for all staff members.
   - Create a comprehensive end-of-shift cleaning checklist.

3. **Value Perception**:
   - Use eye-catching in-store signage to highlight best value-for-money menu items.

### Paris

1. **Parisian Service Standards**:
   - Develop a "Parisian hospitality" training program emphasizing politeness and proper etiquette.
   - Train staff to use more formal language and greetings with customers.

2. **Food Quality Perception**:
   - Focus on consistent portion sizes across all shifts and staff members.
   - Source one or two ingredients locally and highlight this in marketing materials.

3. **Value Enhancement**:
   - Introduce a small loyalty program (e.g., free side item after 5-10 purchases).
   - Create a strategic "happy hour" with reduced prices on select items during slower periods.
   - Offer a small, complimentary "amuse-bouche" with meals to increase perceived value.

## Cross-City Initiatives

1. **Enhanced Customer Feedback System**:
   - Implement a QR code-based quick survey system.
   - Design a short, 3-question survey completable in under a minute.
   - Offer a small discount on the next visit for completing the survey.

2. **Social Media Engagement**:
   - Regularly monitor and respond to reviews on platforms like Google, TripAdvisor, and social media.
   - Utilize free social media management tools to track mentions and respond promptly.

3. **Staff Empowerment**:
   - Allow staff to offer a free drink or small side item to resolve minor complaints on the spot.

4. **Menu Optimization**:
   - Track sales of each menu item over time.
   - Consider removing the lowest-selling items to simplify operations and reduce waste.

## Implementation Plan

1. Prioritize issues based on the percentage of complaints in each city.
2. Implement changes gradually, starting with one or two initiatives at a time.
3. Regularly review customer feedback and sales data to measure the impact of each initiative.
4. Adjust strategies based on results and ongoing customer feedback.
5. Ensure all staff members are well-informed about new initiatives and their role in implementation.
6. Celebrate successes with staff to maintain motivation and reinforce the importance of improvements.

## Project Structure

```bash
fast-food-review-analysis/
│
├── reviews/
│   ├── paris_reviews.csv
│   ├── marseille_reviews.csv
│   └── lyon_reviews.csv
│
├── cleaned_reviews/
│   ├── cleaned_paris_reviews.csv
│   ├── cleaned_marseille_reviews.csv
│   └── cleaned_lyon_reviews.csv
│
├── scored_reviews/
│   ├── scored_paris_reviews.csv
│   ├── scored_marseille_reviews.csv
│   └── scored_lyon_reviews.csv
│
├── results/
│   ├── categories_avis_positifs_lyon.png
│   ├── categories_avis_negatifs_lyon.png
│   ├── categories_avis_positifs_marseille.png
│   ├── categories_avis_negatifs_marseille.png
│   ├── categories_avis_positifs_paris.png
│   └── categories_avis_negatifs_paris.png
│
├── clean_data.py
├── scoring_reviews.py
├── main.py
├── requirements.txt
└── README.md
```

## How to Run the Project

1. Clone the repository

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the data cleaning script:
   ```bash
   python clean_data.py
   ```

4. Run the scoring script:
   ```bash
   python scoring_reviews.py
   ```

5. Run the main analysis script:
   ```bash
   python main.py
   ```

7. View the results in the `results/` directory.


## Conclusion

By focusing on these city-specific concerns and implementing targeted, cost-effective strategies, fast food businesses in Lyon, Marseille, and Paris can work towards reducing negative reviews, enhancing customer satisfaction, and improving their overall reputation and profitability. The key to success lies in consistent application, ongoing monitoring, and a commitment to continuous improvement in response to evolving customer needs and preferences.

## Future Work

- Conduct periodic review analyses to track improvements over time.
- Expand the analysis to include other major French cities or regions.
- Investigate correlations between review sentiment and external factors (e.g., seasons, local events, tourist influx).
- Develop a machine learning model to automate the categorization of reviews for faster analysis.
- Conduct a competitor analysis to benchmark performance against other fast food chains in these cities.

---

# Contact Information

Walid Benzineb - benzinebwal@gmail.com
