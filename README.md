# AdultSalaryDataUS
Beginner ML project on the UCI Adult Dataset [here](https://archive.ics.uci.edu/ml/datasets/Adult)

# A total of 4 classifiers were used, Namely -
1. Random Forest Classifer. 
2. AdaBoost Classifier.
3. KNN Classifier.
4. SVM Classifier.

The details is given in the jupyter notebook of each classifier in the Classifiers Folder.

# The result and peroformance on the training set:
1. Random Forest gave the best accuracy and performed well on the negative label, but couldn't acheive a good recall or f1-score.
2. AdaBoost had an average accuracy but the best ROC AUC score and the best recall and f1-score.
3. KNN performed worse than Random Forst or AdaBoost, but better than SVM.
4. SVM classifier was not able to do a good job, maye because of Randomised Search Cross Validation
