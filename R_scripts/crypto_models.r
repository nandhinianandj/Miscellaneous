crypto.data <- function ()
{
require(XML)
require(httr)
url <- "https://coinmarketcap.com/all/views/all/"
z <- x <- shared.get.webpage(url)
x <- shared.parse.html(x, keyword = "table")
u <- c(x[22:28])
for(i in 1:length(u))
{
u1 <- grep(u[i], x)
x <- x[-u1]
}
u1 <- grep("[*]", x)
x1 <- x[-u1]
hdr <- c("Rank", "Name", "Symbol", "MktCap", "Price",
"Supply", "Volume", "Ch1h", "Ch24h", "Ch7d",
"URL", "Minable")
x1 <- x1[-(1:10)]
x1 <- matrix(x1, length(x1)/11, 11, byrow = T)
x1 <- x1[, -2]
x1 <- gsub(",", "", x1)
x1 <- gsub("\\$", "", x1)
x1 <- gsub("%", "", x1)
x1 <- cbind(x1, rep("", nrow(x1)), rep("Y", nrow(x1)))
y <- grep("currency-symbol visible-xs", z)
z1 <- z[y]
y <- grep("link-secondary", z1)

z1 <- z1[y]
y <- grep("href", z1)
z1 <- z1[y]
y <- grep("currencies", z1)
z1 <- z1[y]
if(length(z1) != nrow(x1))
stop("ERROR")
x <- x[-(1:10)]
for(i in 1:length(z1))
{
u <- unlist(strsplit(z1[i], "/"))[3]
x1[i, 11] <- u
u1 <- grep("[*]", x[1:11])
if(length(u1) > 0)
{
x1[i, 12] <- "N"
x <- x[-(1:12)]
}
else
x <- x[-(1:11)]
}
x1 <- rbind(hdr, x1)
shared.write.table(x1, "crypto.cap.txt", T)
}
crypto.hist.prc <- function (date)
{
require(XML)
require(httr)
x <- read.delim("crypto.cap.txt", header = T)
x <- as.matrix(x)
univ <- x[, 11]
for(i in 1:length(univ))
{
url <- paste("https://coinmarketcap.com/currencies/",
univ[i],
"/historical-data/?start=20000101&end=", date, sep = "")
x <- shared.get.webpage(url)
x <- shared.parse.html(x, keyword = "table")
n <- length(x)/7
if(n < 1 | trunc(n) != n)
	{
write(univ[i], "crypto.bad.txt", append = T)
next
}
x <- matrix(x, length(x)/7, 7, byrow = T)
x[1, ] <- c("Date", "Open", "High", "Low",
"Close", "Volume", "MktCap")
file <- paste("CryptoHistData/", univ[i], ".txt", sep = "")
shared.write.table(x, file, T)
}
}
crypto.prc.files <- function ()
{
match.univ <- function (univ1, univ2)
{
good <- match(univ1, univ2, nomatch = 0)
univ <- univ2[good]
return(univ)
}
read.file <- function(file, header = T)
{
x <- read.delim(file, header = header)
x <- as.matrix(x)
x <- gsub(",", "", x)
return(x)
}
x <- read.file("crypto.cap.txt")
univ <- x[, 11]
mnbl <- x[, 12]
name <- x[, 2]
bad <- readLines("crypto.bad.txt")
take <- is.na(match(univ, bad))
mnbl <- mnbl[take]
name <- name[take]
mnbl[mnbl == "Y"] <- 1
mnbl[mnbl == "N"] <- 0
univ <- univ[take]
shared.write.table(mnbl, file = "cr.mnbl.txt", T)
shared.write.table(name, file = "cr.name.txt", T)
n <- length(univ)

for(i in 1:n)
{
x <- read.file(paste("CryptoHistData/", univ[i],
".txt", sep = ""))
if(i == 1)
{
dates <- x[, "Date"]
d <- length(dates)
prc <- matrix(NA, n, d)
cap <- matrix(NA, n, d)
high <- matrix(NA, n, d)
low <- matrix(NA, n, d)
vol <- matrix(NA, n, d)
open <- matrix(NA, n, d)
dimnames(prc)[[2]] <- dates
dimnames(cap)[[2]] <- dates
dimnames(high)[[2]] <- dates
dimnames(low)[[2]] <- dates
dimnames(vol)[[2]] <- dates
dimnames(open)[[2]] <- dates
prc[1, ] <- x[1:d, "Close"]
cap[1, ] <- x[1:d, "MktCap"]
high[1, ] <- x[1:d, "High"]
low[1, ] <- x[1:d, "Low"]
vol[1, ] <- x[1:d, "Volume"]
open[1, ] <- x[1:d, "Open"]
}
else
{
dates1 <- x[, "Date"]
dates1 <- match.univ(dates, dates1)
prc[i, dates1] <- x[1:length(dates1), "Close"]
cap[i, dates1] <- x[1:length(dates1), "MktCap"]
high[i, dates1] <- x[1:length(dates1), "High"]
low[i, dates1] <- x[1:length(dates1), "Low"]
vol[i, dates1] <- x[1:length(dates1), "Volume"]
open[i, dates1] <- x[1:length(dates1), "Open"]
}
}
mode(prc) <- "numeric"
mode(cap) <- "numeric"
mode(high) <- "numeric"
mode(low) <- "numeric"

mode(vol) <- "numeric"
mode(open) <- "numeric"
shared.write.table(prc, file = "cr.prc.txt", T)
shared.write.table(cap, file = "cr.cap.txt", T)
shared.write.table(high, file = "cr.high.txt", T)
shared.write.table(low, file = "cr.low.txt", T)
shared.write.table(vol, file = "cr.vol.txt", T)
shared.write.table(open, file = "cr.open.txt", T)
}
crypto.prc <- function (days = 365, back = 0,
lookback = days, d.r = 20, d.v = 20, d.i = 20)
{
calc.ix <- function(z, days)
{
ix <- colSums(z[, 1:days])
ix <- ix[days:1]
ix <- ix / ix[1]
return(ix)
}
read.prc <- function(file, header = F, make.numeric = T)
{
x <- read.delim(file, header = header)
x <- as.matrix(x)
if(make.numeric)
mode(x) <- "numeric"
return(x)
}
calc.mv.avg <- function(x, days, d.r)
{
if(d.r == 1)
return(x[, 1:days])
y <- matrix(0, nrow(x), days)
for(i in 1:days)
y[, i] <- rowMeans(x[, i:(i + d.r - 1)], na.rm = T)
return(y)
}
prc <- read.prc("cr.prc.txt")
cap <- read.prc("cr.cap.txt")

high <- read.prc("cr.high.txt")
low <- read.prc("cr.low.txt")
vol <- read.prc("cr.vol.txt")
open <- read.prc("cr.open.txt")
mnbl <- read.prc("cr.mnbl.txt")
name <- read.prc("cr.name.txt", make.numeric = F)
d <- days + d.r + 1
prc <- prc[, 1:d]
cap <- cap[, 1:d]
high <- high[, 1:d]
low <- low[, 1:d]
vol <- vol[, 1:d]
open <- open[, 1:d]
take <- rowSums(is.na(prc)) == 0 & rowSums(is.na(cap)) == 0 &
rowSums(is.na(high)) == 0 & rowSums(is.na(low)) == 0 &
rowSums(is.na(vol)) == 0 & rowSums(is.na(open)) == 0 &
rowSums(vol == 0) == 0
ret <- log(prc[take, -d] / prc[take, -1])
prc <- prc[take, -1]
cap <- cap[take, -1]
high <- high[take, -1]
low <- low[take, -1]
vol <- vol[take, -1]
open <- open[take, -1]
mnbl <- mnbl[take, 1]
name <- name[take, 1]
if(back > 0)
{
ret <- ret[, (back + 1):ncol(ret)]
prc <- prc[, (back + 1):ncol(prc)]
cap <- cap[, (back + 1):ncol(cap)]
high <- high[, (back + 1):ncol(high)]
low <- low[, (back + 1):ncol(low)]
vol <- vol[, (back + 1):ncol(vol)]
open <- open[, (back + 1):ncol(open)]
}
days <- lookback
av <- log(calc.mv.avg(vol, days, d.v))
hlv <- (high - low)^2 / prc^2
hlv <- 0.5 * log(calc.mv.avg(hlv, days, d.i))
take <- rowSums(!is.finite(hlv)) == 0

av <- av[take, ]
hlv <- hlv[take, ]
mom <- log(prc / open)[take, 1:days]
mom1 <- log(prc / open)[take, 1:days + 1]
mom2 <- log(prc / open)[take, 1:days + 2]
mom3 <- log(prc / open)[take, 1:days + 3]
mom4 <- log(prc / open)[take, 1:days + 4]
size <- log(cap)[take, 1:days]
ret <- ret[take, 1:days]
mnbl <- mnbl[take]
name <- name[take]
for(i in 1:days)
{
flm <- cbind(size[, i], mom[, i], hlv[, i], av[, i])
if(i == 1)
fac <- matrix(NA, ncol(flm) + 1, days)
reg <- lm(ret[, i] flm)
fac[, i] <- coefficients(reg)
}
t.stat <- sqrt(365) * rowMeans(fac) / apply(fac, 1, sd)
t.stat <- round(t.stat, 2)
prc <- prc[take, ]
cap <- cap[take, ]
y <- prc[name == "Xaurum", ]
prc[name == "Xaurum", y > 1] <-
prc[name == "Xaurum", y > 1] / 8000
ix.cap <- calc.ix(cap, days)
ix.prc <- calc.ix(prc, days)
plot(1:length(ix.cap), ix.cap, type = "l",
col = "green", xlab = "days", ylab = "index value",
ylim = c(min(c(ix.cap, ix.prc)) - .5,
max(c(ix.cap, ix.prc)) + .5))
lines(1:length(ix.prc), ix.prc, col = "blue")
return(t.stat)
}
