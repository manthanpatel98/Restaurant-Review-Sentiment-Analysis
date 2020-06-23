# **Restaurant-Review-Sentiment-Analysis**
## **Predicting Restaurant Review Sentiment**
---
### Web APP on Heroku

![Predicting Restaurant Review Heroku Project](https://github.com/manthanpatel98/Restaurant-Review-Sentiment-Analysis/blob/master/README-Resources/Restaurant-Review1.gif)

### **[The Project on Heroku](https://restaurantreviewsentiment.herokuapp.com/predict)**
---
## **Understanding The Project**

### **Starting with Dataset**
***
![Dataset](https://github.com/manthanpatel98/Restaurant-Review-Sentiment-Analysis/blob/master/README-Resources/Screenshot%20(96).png)

* From this Dataset, To Perform NLP Project, I decided to take **"Review"** and **"Rating columns"**.
* Later After cleaning the columns, I converted **"Rating"** Column, which is actually a numerical column, into the column that has two labels **"Positive"** and **"Negative"**.
* I considered Rating **Above 3** as **"Positive"** and **Below 3** as **"Negative"**.
* To understand detailed Project approach, check my [**Restaurant-Review.ipynb**](https://github.com/manthanpatel98/Restaurant-Review-Sentiment-Analysis/blob/master/Restaurant-Review.ipynb)
***

### **Applied Algorithms & Their Accuracy**
***
| Algorithm | Accuracy |
| ---    | ---    |
| Random Forest | 89.28% |
| MultinomialNB | 90.84% |
| SVM | 76.68% |

* After Checking Accuracy for these Three Algorithms, I decided to use **MultinomialNB** in **Web App**.
