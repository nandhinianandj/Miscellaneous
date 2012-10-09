require(fields) # for heatmap plot with legend
require(randomForest) # requires installation, for random forest models

random.seed(20120926)

# heatmap wrapper, plotting func(x, y) over range a by a
hmap.func <- function(a, f, xlab, ylab) 
{
image.plot(a, a, outer(a, a, f), zlim = c(0, 1), xlab = xlab, ylab = ylab)
}
         
# define class signal
g <- function(x, y) 1 / (1 + 2^(x^3+ y+x*y))
# create training data
d <- data.frame(x1 = rnorm(10000), x2 = rnorm(10000) ,x3 = rnorm(10000), x4 = rnorm(10000))
d$y = with(d, ifelse(runif(10000) < g(x1, x2), 1, 0))
         
# plot signal (left hand plot below)
a = seq(-2, 2, len = 100)
hmap.func(a, g, "x1", "x2")
         
# plot training data representation (right hand plot below)
z = tapply(d$y,  list(cut(d$x1, breaks = seq(-2, 2, len=25)), cut(d$x2, breaks = seq(-2, 2, len=25))), mean)

image.plot(seq(-2, 2, len=25), seq(-2, 2, len=25), z, zlim = c(0, 1), xlab = "x1", ylab = "x2")

# Fit log regression and random forest
fit.lr = glm(y~x1+x2+x3+x4, family = binomial, data = d)
fit.rf = randomForest(as.factor(y)~x1+x2+x3+x4, data = d, ntree = 100, proximity = FALSE)
         
# Create funtions in x1, x2 to give model predictions
# while setting x3, x4 at origin
g.lr.sig = function(x, y) predict(fit.lr, data.frame(x1 = x, x2 = y, x3 = 0, x4 = 0), type = "response") 
g.rf.sig = function(x, y) predict(fit.rf, data.frame(x1 = x, x2 = y, x3 = 0, x4 = 0), type = "prob")[, 2] 
g.en.sig = function(x, y) 0.5*g.lr.sig(x, y) + 0.5*g.rf.sig(x, y)
         
# Map model predictions in x1 and x2
hmap.func(a, g.lr.sig, "x1", "x2")
hmap.func(a, g.rf.sig, "x1", "x2")
hmap.func(a, g.en.sig, "x1", "x2")
