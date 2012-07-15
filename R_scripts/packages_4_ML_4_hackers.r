packages <- c('arm','ggplot2','glmnet','igraph','lme4','lubridate','RCurl','reshape','RJSONIO','tm','XML')

for (i in 1:length(packages)) {
install.packages(packages[i])
}
