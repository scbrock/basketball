# predict outcome of next game give Lebron James's points, rebounds, and assists in the last 3 games
# Standardized data + 2 layers


from keras.models import Sequential
from keras.layers import Dense
from sklearn import preprocessing
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy
import tensorflow

numpy.random.seed(20)

dataset = numpy.loadtxt("lbj_pts_reb_asst_pm_data.csv", delimiter=",")
testset = numpy.loadtxt("lbj_pts_reb_asst_pm_testdata.csv",delimiter=",")

X_test = testset[:,0:15]
Y_test = testset[:,15]
X_test = preprocessing.scale(X_test)


X = dataset[:,0:15]
Y = dataset[:,15]

print(X_test.shape)
print(X.shape)

# need to get a test dataset - 2017/18 season

X_standard = preprocessing.scale(X)

X_normal = preprocessing.normalize(X)

# model_1 uses regular data
model_1 = Sequential()
model_1.add(Dense(15, input_dim=15, activation='relu'))
model_1.add(Dense(5, activation='relu'))
#model.add(Dense(9, activation='relu'))
model_1.add(Dense(1, activation='sigmoid'))



model_1.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])


model_1.fit(X, Y, epochs=100, batch_size=10, verbose=0)
scores_1 = model_1.evaluate(x=X_test,y=Y_test)
print("Model 1, regular performance:")
print("%s,%.3f%%" % (model_1.metrics_names[1], scores_1[1]*100))






