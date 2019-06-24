setwd('D:\\EPAM\\Data Scientist Academy\\Eveosev\\week-06\\day-04')

#Import data
original_train = read.csv(file.choose())
test = read.csv('test.csv', header = TRUE)

#check missing value
library(mice)
md.pattern(train)


#Missing data
#Omit the missing rows
train_noNA = na.omit(original_train)
logistic_omit = glm(formula = Survived ~ Pclass + Sex + Age + SibSp + Parch + Fare + Embarked,
                    family = binomial(link = "logit"), 
                    data = train_noNA)
summary(logistic_omit)

#drop insignificant variable one-by-one
logistic_omit = glm(formula = Survived ~ Pclass + Sex + Age + SibSp + Parch + Fare,
                    family = binomial(link = "logit"), 
                    data = train_noNA)

logistic_omit = glm(formula = Survived ~ Pclass + Sex + Age + SibSp,
                    family = binomial(link = "logit"), 
                    data = train_noNA)

train_prob = predict(logistic_omit, train_noNA[c('Pclass', 'Sex', 'Age', 'SibSp')], type = 'response')

train_prob_sorted = train_prob[order(train_prob)]
n = length(train_prob_sorted)


#ROC
library(pROC)
ROC = roc(train_noNA$Survived, train_prob)
auc(ROC)
plot(ROC, print.auc=TRUE, auc.polygon=TRUE, grid=c(0.1, 0.2),
    grid.col=c("olivedrab", "grey"), max.auc.polygon=TRUE,
    auc.polygon.col="olivedrab3", print.thres=TRUE,
    main="ROC",xlab="Treshhold",ylab="Sensitivity") 

#Conclusion
treshhold = 0.515
Survived_pre = data.frame('Survived_pred' = as.numeric(train_prob > treshhold))
table(train_noNA$Survived, Survived_pre$Survived_pred)
accuracy = sum(Survived_pre == train_noNA$Survived) / length(train_noNA$Survived)

#Prediction
test_noNA = na.omit(test)
test_prob = predict(logistic_omit, test_noNA[c('Pclass', 'Sex', 'Age', 'SibSp')], type = 'response')
Survived_pre_test = data.frame('Survived_pred' = as.numeric(test_prob > treshhold))



#Imputation with mean value
library(Hmisc)
train_mean = data.frame('Age_mean_imputation' = impute(original_train$Age, mean))
train = cbind(original_train, train_mean)
logistic_mean = glm(formula = Survived ~ Pclass + Sex + SibSp + Age_mean_imputation,
                    family = binomial(link = "logit"), 
                    data = train)
summary(logistic_mean)

prob_mean_imputatio = predict(logistic_mean, 
                              train[c('Pclass', 'Sex', 'SibSp',  'Age_mean_imputation')],
                              type = 'response')

ROC_mean = roc(train$Survived, prob_mean_imputatio)
auc(ROC_mean)
plot(ROC_mean, print.auc=TRUE, auc.polygon=TRUE, grid=c(0.1, 0.2),
     grid.col=c("olivedrab", "grey"), max.auc.polygon=TRUE,
     auc.polygon.col="olivedrab3", print.thres=TRUE,
     main="ROC",xlab="Treshhold",ylab="Sensitivity") 

treshhold = 0.389
Survived_pre_mean = data.frame('Survived_pred_mean' = as.numeric(prob_mean_imputatio > treshhold))
table(train$Survived, Survived_pre_mean$Survived_pred_mean)
accuracy = sum(Survived_pre_mean == train$Survived) / length(train$Survived)

#Test output
#Prediction
test_mean = data.frame('Age_mean_imputation' = impute(test$Age, median))
test = cbind(test, test_mean)
test_prob = predict(logistic_mean, test[c('Pclass', 'Sex', 'Age_mean_imputation', 'SibSp')], type = 'response')
Survived_pre_mean_imputation = data.frame('PassengerId' = test$PassengerId, 'Survived' = as.numeric(test_prob > treshhold))

write.csv(Survived_pre_mean_imputation, 'Prediction_by_Logistic_with_mean_imputation',row.names = FALSE)


#KNN imputation
?knnImputation
Age_knnImuptation = knnImputation(original_train[, !names(original_train) %in% 'Survived'])
Age_knnImputation = data.frame('Age_imputation' = Age_knnImuptation$Age)
train = cbind(train, Age_knnImputation)
logistic_KNN = glm(formula = Survived ~ Pclass + Sex + SibSp + Age_imputation,
                    family = binomial(link = "logit"), 
                    data = train)

prob_knn = predict(logistic_KNN,
                    train[c('Pclass', 'Sex', 'SibSp',  'Age_imputation')],
                    type = 'response')

ROC_knn = roc(train$Survived, prob_knn)
auc(ROC_knn)
plot(ROC_knn, print.auc=TRUE, auc.polygon=TRUE, grid=c(0.1, 0.2),
     grid.col=c("olivedrab", "grey"), max.auc.polygon=TRUE,
     auc.polygon.col="olivedrab3", print.thres=TRUE,
     main="ROC",xlab="Treshhold",ylab="Sensitivity") 

treshhold = 0.424
test_Age_knnImuptation = knnImputation(test)
test_Age_knnImputation = data.frame('Age_imputation' = test_Age_knnImuptation$Age)
test = cbind(test, test_Age_knnImputation)
test_prob = predict(logistic_KNN, test[c('Pclass', 'Sex', 'Age_imputation', 'SibSp')], type = 'response')
Survived_pre_knn = data.frame('PassengerId' = test$PassengerId, 'Survived' = as.numeric(test_prob > treshhold))
write.csv(Survived_pre_knn, 'Prediction_by_Logistic_with_knn_imputation',row.names = FALSE)
