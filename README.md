# India_Census_2011_EDA

## Overview 
Exploratory Data Analysis (EDA) is a crucial step in understanding large and complex datasets. The India Census 2011 dataset provides comprehensive demographic, social, and economic information about the population of India, covering aspects such as population size, literacy rates, gender distribution, age groups, and household conditions.
In this analysis, we explore patterns, distributions, and relationships within the dataset to gain meaningful insights about India’s population structure and development indicators in 2011.

## Dataset Description
| **Column Name**        | **Description**                         |
| ---------------------- | --------------------------------------- |
| `District_code`        | Unique code for each district           |
| `State_name`           | Name of the state                       |
| `District_name`        | Name of the district                    |
| `Population`           | Total population of the district        |
| `Male`                 | Total male population                   |
| `Female`               | Total female population                 |
| `Literate`             | Number of literate people               |
| `Workers`              | Total number of working individuals     |
| `Male_Workers`         | Total number of working males           |
| `Female_Workers`       | Total number of working females         |
| `Cultivator_Workers`   | Workers engaged in cultivation          |
| `Agricultural_Workers` | Workers engaged in agriculture          |
| `Household_Workers`    | Workers engaged in household industries |
| `Hindus`               | Hindu population                        |
| `Muslims`              | Muslim population                       |
| `Christians`           | Christian population                    |
| `Sikhs`                | Sikh population                         |
| `Buddhists`            | Buddhist population                     |
| `Jains`                | Jain population                         |
| `Secondary_Education`  | People with secondary-level education   |
| `Higher_Education`     | People with higher secondary education  |
| `Graduate_Education`   | People who are graduates                |
| `Age_Group_0_29`       | Population aged 0–29 years              |
| `Age_Group_30_49`      | Population aged 30–49 years             |
| `Age_Group_50`         | Population aged 50 years and above      |

## Data cleaning
I already have a cleaned data so i further moved to the next phase of analysis.

## Exploratory Data Analysis

# 1. Population comparison of Different States
## Uttar Pradesh has the highest population, followed by Maharashtra, Bihar, and West Bengal.
States and Union Territories with the lowest populations include Tripura, Meghalaya, Nagaland, Arunachal Pradesh, Goa, Puducherry, Mizoram, Chandigarh, and Sikkim, as well as island territories such as Andaman and Nicobar Islands, Daman and Diu, and Lakshadweep.
<img width="980" height="565" alt="image" src="https://github.com/user-attachments/assets/c77e3a3d-360b-4e2a-a7c8-7ad94b21c81e" />

# 2. Distribution of Male and Female Population Across state in India
## The male and female populations are highest in Uttar Pradesh, followed by Maharashtra, Bihar, and West Bengal.
The lowest male and female populations are observed in Tripura, Meghalaya, Nagaland, Arunachal Pradesh, Goa, Puducherry, Mizoram, Chandigarh, and Sikkim, as well as in the island territories of the Andaman and Nicobar Islands, Daman and Diu, and Lakshadweep.
<img width="1493" height="738" alt="image" src="https://github.com/user-attachments/assets/9a90f357-82e2-4129-9a33-bc05e8e0272f" />

# 3. State wise Sex-Ratio
## The sex ratio is highest in Kerala followed by Puducherry, Tamil Nadu, Andhra Pradesh, and Chhattisgarh, while it is lowest in Daman and Diu, Chandigarh, Andaman and Nicobar Islands, and Haryana.
<img width="1122" height="739" alt="image" src="https://github.com/user-attachments/assets/b990f959-9792-4ea5-a2cd-f331f9fab29f" />

# 4. Literacy Rate of Different States
## Kerala has the highest literacy rate, followed by Lakshadweep, Goa, Daman and Diu, and Puducherry,the states with the lowest literacy rates are Rajasthan, Jharkhand, Arunachal Pradesh, and Bihar.
<img width="1371" height="716" alt="image" src="https://github.com/user-attachments/assets/b8c2a75d-7a6c-4712-9a97-540fe18f22d8" />

# 5. Male vs Female Literacy rate by state
## Every state shows a relatively balanced male and female literacy rate.In states with an already high overall literacy rate, the literacy levels of both males and females are nearly equal and higher compared to other states.
<img width="1494" height="736" alt="image" src="https://github.com/user-attachments/assets/6956a292-4adc-443a-8a01-f8f3546ea9a6" />

# 6. Proportion of Children/Youth of Top 10 States
<img width="494" height="384" alt="image" src="https://github.com/user-attachments/assets/db764523-9115-4b76-a963-4e81ff486aaa" />

# 7. Correlation b/w Literacy and Educational Levels
## The literacy rate shows a very strong positive correlation with all levels of education. It is most strongly correlated with secondary education (0.93), followed closely by higher education (0.92) and graduation-level education (0.87). This indicates that regions with higher literacy rates tend to have more people completing secondary and higher education, suggesting that improving access to education, particularly at the secondary level, is likely to have the greatest impact on overall literacy.
<img width="618" height="530" alt="image" src="https://github.com/user-attachments/assets/915c67a6-1627-4be7-a90a-e7802690a083" />

# 8. Percentage of Workers in Differnt State
# The highest number of workers are found in Himachal Pradesh, Sikkim, Daman and Diu, Nagaland, Chhattisgarh, Andhra Pradesh, Manipur, and Karnataka.The lowest number of workers is observed in Haryana, Kerala, Jammu & Kashmir, Bihar, and Uttar Pradesh.
<img width="1434" height="662" alt="image" src="https://github.com/user-attachments/assets/13e39677-56b1-4989-bea9-4cb0e7ed8f8e" />

# 9. Comparison of Male Vs Female Participation in Workforce By State
## In each state, male participation in the workforce is higher compared to female participation.
<img width="1098" height="764" alt="image" src="https://github.com/user-attachments/assets/1b6e748c-93bd-45df-b317-dc94ea4ad403" />

# 10. Proportion of Female workers in Different State
# Himachal Pradesh has the highest number of female workers, followed by Nagaland, Manipur, Chhattisgarh, Sikkim, and Andhra Pradesh.The lowest number of female workers is observed in Uttar Pradesh, Chandigarh, Punjab, Daman and Diu,Delhi and Lakshadweep.
<img width="1202" height="703" alt="image" src="https://github.com/user-attachments/assets/ef20106e-f7c3-4611-aeae-4f5c4ab36086" />

# 11. WorkForce Distribution Among Cultivators,Agricultural Laborers and Household workers
## Lakshadweep mostly has household workers, while other states have a mix of cultivators, agricultural laborers, and household industry workers.Himachal Pradesh has the highest number of cultivators among all states, whereas Puducherry has the highest number of agricultural laborers.
<img width="865" height="621" alt="image" src="https://github.com/user-attachments/assets/c47c4d30-4d90-4deb-9ce1-9e3e2b40129b" />

# 12. Relationship between Education level and Workforce Participation
<img width="559" height="574" alt="image" src="https://github.com/user-attachments/assets/0235115a-b338-4ac5-9790-9344ea5bead8" />
<img width="446" height="449" alt="image" src="https://github.com/user-attachments/assets/73ca98d8-d904-4c90-8803-f341544c7208" />

# 13. Religious Composition of Each State
<img width="1054" height="752" alt="image" src="https://github.com/user-attachments/assets/80e313e5-e686-49c1-b6a8-59a94d55cad4" />

# 14. Correlations Between Religion and Education/literacy or gender ratio
<img width="844" height="601" alt="image" src="https://github.com/user-attachments/assets/bbe63da9-cfcd-40d3-88f6-d55dc08b7445" />

# 15.  Age group distribution across states (0–29, 30–49, 50+)
<img width="1047" height="748" alt="image" src="https://github.com/user-attachments/assets/08828a1b-9a51-4d8f-8baa-cd292c804c29" />

# 16. Correlation b/w Age Groups and Literacy/Employment
<img width="714" height="603" alt="image" src="https://github.com/user-attachments/assets/e6bfd4b0-c83a-4dee-b9cb-9c04c739b8f1" />

