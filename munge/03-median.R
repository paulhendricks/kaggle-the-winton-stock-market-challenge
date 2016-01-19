train <- read.csv("./data/original/train.csv", stringsAsFactors = FALSE)
test <- read.csv("./data/original/test_2.csv", stringsAsFactors = FALSE)
sample_submission <- read.csv("./data/submission/sample_submission_2.csv", stringsAsFactors = FALSE)
x <- as.numeric(apply(train[,148:209],FUN=median,MARGIN=2))
sample_submission$Predicted <- x
write.csv(sample_submission, "./data/submission/median_submission.csv", row.names = FALSE)
