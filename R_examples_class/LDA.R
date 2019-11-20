library(topicmodels)
library(tidytext)

data("AssociatedPress")

ap_lda <- LDA(AssociatedPress, k = 2, control = list(seed = 1234))

topics <- tidy (ap_lda, matrix="beta")
docs <- tidy (ap_lda, matrix="gamma")

topics
docs