# (Ugly) function for measuring cross-entropy error
cross.entropy <- function(target, predicted)
{
predicted = pmax(1e-10, pmin(1-1e-10, predicted))
- sum(target * log(predicted) + (1 - target) * log(1 - predicted))
}

# Creation of validation data
dv <- data.frame(x1 = rnorm(10000), x2 = rnorm(10000)
, x3 = rnorm(10000), x4 = rnorm(10000))
dv$y = with(dv, ifelse(runif(10000) < g(x1, x2), 1, 0))

# Create predicted results for each model
dv$y.lr <- predict(fit.lr, dv, type = "response")
dv$y.rf <- predict(fit.rf, dv, type = "prob")[, 2]

# Function to show ensemble cross entropy error at weight W for log. reg.
error.by.weight <- function(w) cross.entropy(dv$y, w*dv$y.lr + (1-w)* dv$y.rf)

# Plot + pretty
plot(Vectorize(error.by.weight), from = 0.0, to = 1,
xlab = "ensemble weight on logistic regression", ylab = "cross-entropy error of ensemble", col = "blue")
text(0.1, error.by.weight(0)-30, "Random\nForest\nOnly")
text(0.9, error.by.weight(1)+30, "Logistic\nRegression\nOnly")

