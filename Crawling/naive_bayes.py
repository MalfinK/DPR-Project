# import standard libraries for classification
import pandas as pd  # untuk mempermudah akses kolom per baris
import string
import numpy as np  # untuk mempermudah proses dalam pembuatan array atau matrix
import nltk

# import for machine learning naive bayes
# from sklearn.naive_bayes import MultinomialNB
# from sklearn import model_selection
# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.feature_extraction.text import TfidfTransformer
# from sklearn.model_selection import train_test_split
# from sklearn.utils.multiclass import unique_labels
# from sklearn.preprocessing import LabelBinarizer, OrdinalEncoder, OneHotEncoder

# # import for visualization
# import sklearn.metrics as classification_report
# import accuracy_score
# import confusion_matrix
# import matplotlib.pyplot as plt
# import seaborn as sns

# call the dataset used
dataset = pd.read_csv('hasil_crawler2.csv', header=0, delimiter=';', encoding='utf-8')
df = pd.DataFrame(dataset)
# print(df)

# input parameters for prediction class
xTarget = df.drop(['id', 'y'], axis=1)
print(xTarget)

# output parameters for prediction class
yTarget = df['y']
print(yTarget)

# switch encode yTarget to binary
yTarget = LabelBinarizer().fit_transform(yTarget)
# print(yTarget)

# switch encode atribut value to index value
tfid_transformer = OneHotEncoder()
xTarget = tfid_transformer.fit_transform(xTarget)
# print(xTarget)
# print(xTarget.shape)

# make data training and data testing from dataset with 30% from sum of instances
xTrain, xTest, yTrain, yTest = train_test_split(xTarget, yTarget, test_size=0.3, random_state=0)
# print(xTrain.shape)
# print(xTest.shape)
# print(yTrain.shape)
# print(yTest.shape)

# doing make naive bayes model
naiveBayes = MultinomialNB().fit(xTrain, np.ravel(yTrain, order='C'))
# print(naiveBayes)

# prediction to model training which has been made
prediction = naiveBayes.predict(xTest)
accurasies = accuracy_score(yTest, prediction)
# print(prediction)
# print(accurasies)

# make confusion matrix
confusionMatrix = confusion_matrix(yTest, prediction)
# print(confusionMatrix)

# procedur for map the confusion matrix


def plot_confusion_matrix(y_true, y_pred, classes, normalize=False, title=None, cmap=plt.cm.Blues):
    if not title:
        if normalize:
            title = 'Normalized confusion matrix'
        else:
            title = 'Confusion matrix, without normalization'

    # Compute confusion matrix
    cm = confusion_matrix(y_true, y_pred)
    # Only use the labels that appear in the data
    classes = classes[unique_labels(y_true, y_pred)]
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)

    fig, ax = plt.subplots()
    im = ax.imshow(cm, interpolation='nearest', cmap=cmap)
    ax.figure.colorbar(im, ax=ax)
    # We want to show all ticks...
    ax.set(xticks=np.arange(cm.shape[1]),
            yticks=np.arange(cm.shape[0]),
            # ... and label them with the respective list entries
            xticklabels=classes, yticklabels=classes,
            title=title,
            ylabel='True label',
            xlabel='Predicted label')

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
                rotation_mode="anchor")

    # Loop over data dimensions and create text annotations.
    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            ax.text(j, i, format(cm[i, j], fmt),
                    ha="center", va="center",
                    color="white" if cm[i, j] > thresh else "black")
    fig.tight_layout()
    return ax


# visualization result of confusion matrix
classNames = yTarget
np.set_printoptions(precision=2)

# Plot non-normalized confusion matrix
plot_confusion_matrix(yTest, prediction, classes=classNames, title='Confusion matrix, without normalization')

# Plot normalized confusion matrix
plot_confusion_matrix(yTest, prediction, classes=classNames, normalize=True, title='Normalized confusion matrix')

# plt.show()
