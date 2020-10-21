library(e1071)
library(randomForest)
library(caret)
library(C50)
#Read Data
data <- read.csv("Movie data.csv")
data$Title <- NULL
str(data)
#Split Data
smp_size <- floor (0.66*nrow(data))
set.seed(123)
train_d <-sample(seq_len(nrow(data)),size=smp_size)
train<- data[train_d,]
test<-data[-train_d,]
test$HIT.FLOP
#Naive Bayes
NB<-naiveBayes(HIT.FLOP~.,data=train)
Pred<-predict(NB, test, type = "class")
Pred
A <- table(Pred, test$HIT.FLOP, dnn=c("Predicted", "Actual"))
confusionMatrix(A)
#SVM
SVM<-svm(HIT.FLOP~.,data=train)
Pred<-predict(SVM, test, type = "class")
Pred
B <- table(Pred, test$HIT.FLOP, dnn=c("Predicted", "Actual"))
confusionMatrix(B)
#Random Forest
RF<- randomForest(HIT.FLOP~,data=train)
Pred<-predict(RF, test, type = "class")
Pred
C <- table(Pred, test$HIT.FLOP, dnn=c("Predicted", "Actual"))
confusionMatrix(C)
#Decision Tree
C50 <- C5.0(HIT.FLOP~,data=train)
Pred<-predict(C50, test, type = "class")
D<- table(Pred, test$HIT.FLOP, dnn=c("Predicted", "Actual"))
confusionMatrix(D)

