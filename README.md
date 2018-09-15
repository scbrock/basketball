# basketball

file: NBA_data_exploration.ipynb

## Purpose:
Predicting NBA teams' stats performance, on a scale of 1 to 5, given the previous season's information. For example, given the previous
season performance of the Cleveland Cavaliers and the performance of the top 8 players on the Cavaliers, how will the Cavaliers' win percentage be in the next season? 

## Data:
All the data used has been taken from nba.com. Data has been divided into two groups, team and player. Team data represents team averages for a given season. Player data represents player averages for a given season. Feature vectors are then generated based on a team's most recent season performance. For training and testing, the labels are the categorized team statistics (e.g. pts, 3pt %, win %, etc.) for the following year. 

## Implementation:
There are 3 models, a linear model, an xgboost model, and a neural network (in Keras). Each model is trained on 70% of the data and is then tested on the remaining 30%. Accuracies can then be compared.

## Results:
The xgboost model outperformed the neural network and linear model. This is probably due to the lack of data (~500 data points).


