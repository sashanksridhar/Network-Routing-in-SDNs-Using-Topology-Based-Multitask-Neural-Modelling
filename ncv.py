import csv
from sklearn.model_selection import train_test_split
import numpy
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from keras.models import Model
from keras.layers import Input
from keras.layers import Dense

from keras.wrappers.scikit_learn import KerasClassifier

# load the dataset
Xi = []
Y = []
# open the file
with open("D:\\fyp\\fyp_codes\\w1_norm_combined.csv", 'r') as r:
    c = 0
    reader = csv.reader(r)
    for row in reader:
        if c==0:
            c+=1
            continue
        r1 = []
        for j in range(0,len(row)):
            r1.append(float(row[j]))
        Xi.append(r1)
        c+=1

train, test = train_test_split(Xi,test_size=0.25)
X = []
Xt = []
Yt = []
Yd = []
for i in train:
    X.append(numpy.array(i[:len(i)-7]))
    Y.append(numpy.array(i[len(i)-7:]))
    Yd.append(i[len(i)-7:])
for i in test:
    Xt.append(i[:len(i)-7])
    Yt.append(i[len(i)-7:])


Y1=[]
Y2=[]
Y3=[]
Y4=[]
Y5=[]
Y6=[]
Y7=[]
for i in range(0,len(Yd)):
    Y1.append(Yd[i][0])
    Y2.append(Yd[i][1])
    Y3.append(Yd[i][2])
    Y4.append(Yd[i][3])
    Y5.append(Yd[i][4])
    Y6.append(Yd[i][5])
    Y7.append(Yd[i][6])
# split into input (X) and output (y) variables
# Build the neural network

seed = 7
numpy.random.seed(seed)
kfold = StratifiedKFold(n_splits=10, shuffle=True, random_state=seed)
Xout = numpy.array(X)
Yout = numpy.array(Yd)
print(Xout.shape)
print(Yout.shape)

# fit the keras model on the dataset

cvscores = []
for train, test in kfold.split(Xout, numpy.zeros(shape=(Xout.shape[0], 1))):
    #  print(train,test)
    visible = Input(shape=(23,))
    c1 = Dense(23, activation='relu')(visible)
    c2 = Dense(16, activation='relu')(c1)
    s1 = Dense(1, activation='sigmoid')(c2)
    s2 = Dense(1, activation='sigmoid')(c2)
    s3 = Dense(1, activation='sigmoid')(c2)
    s4 = Dense(1, activation='sigmoid')(c2)
    s5 = Dense(1, activation='sigmoid')(c2)
    s6 = Dense(1, activation='sigmoid')(c2)
    s7 = Dense(1, activation='sigmoid')(c2)

    model = Model(inputs=visible, outputs=[s1, s2, s3, s4, s5, s6, s7])
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    # Fit the model
    Xtrain = []
    Ytrain1 = []
    Ytrain2 = []
    Ytrain3 = []
    Ytrain4 = []
    Ytrain5 = []
    Ytrain6 = []
    Ytrain7 = []
    for i in train:
        Xtrain.append(X[i])
        Ytrain1.append(Y1[i])
        Ytrain2.append(Y2[i])
        Ytrain3.append(Y3[i])
        Ytrain4.append(Y4[i])
        Ytrain5.append(Y5[i])
        Ytrain6.append(Y6[i])
        Ytrain7.append(Y7[i])
    model.fit(numpy.array(Xtrain), [Ytrain1,Ytrain2,Ytrain3,Ytrain4,Ytrain5,Ytrain6,Ytrain7], epochs=3, batch_size=10)
    Xtest = []
    Ytest1 = []
    Ytest2 = []
    Ytest3 = []
    Ytest4 = []
    Ytest5 = []
    Ytest6 = []
    Ytest7 = []
    Yt = []
    for i in test:
        Xtest.append(X[i])
        Ytest1.append(Y1[i])
        Ytest2.append(Y2[i])
        Ytest3.append(Y3[i])
        Ytest4.append(Y4[i])
        Ytest5.append(Y5[i])
        Ytest6.append(Y6[i])
        Ytest7.append(Y7[i])
        Yt.append(Yd[i])
    # evaluate the model
    scores = model.evaluate(numpy.array(Xtest), [Ytest1,Ytest2,Ytest3,Ytest4,Ytest5,Ytest6,Ytest7])
    for i in range(0, len(scores)):
        print("%s: %.2f%%" % (model.metrics_names[i], scores[i] * 100))

    predicted = model.predict(numpy.array(Xtest))
    p_classes = numpy.argmax(predicted, axis=1)

    p = []

    for x in numpy.nditer(predicted):
        xi = []
        for i in range(0, 7):

            if x[i] < float(0.5):
                xi.append(0.0)
            else:
                xi.append(1.0)
        p.append(xi)

    count = 0
    for i in range(0, len(Yt)):
        v = 1
        for j in range(0, len(Yt[i])):
            if Yt[i][j] != p[i][j]:
                v = 0
                break
        if v == 1:
            count += 1

    print(count)
    print((count / len(Yt)) * 100)
