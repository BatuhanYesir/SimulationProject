# Gerekli paketler
library(tidyverse)

# Dosya okuma (ondal??k nokta ve virg??l sorununa g??re d??zenle)
data <- read.csv("queue_data.csv", sep = ",", dec = ".", stringsAsFactors = FALSE)

# Say??sal s??tunlar?? kontrol et
str(data)

# Negatif wait_time de??erlerini temizle
data <- data %>% filter(wait_time >= 0)

hist(data$wait_time, main = "Wait Time Histogram", col = "lightblue")
qqnorm(data$wait_time); qqline(data$wait_time, col = "red")

shapiro.test(data$wait_time)
shapiro.test(data$queue_length)
install.packages("fitdistrplus")
library(fitdistrplus)

# wait_time i??in test
descdist(data$wait_time, boot = 100)

fit.norm <- fitdist(data$wait_time, "norm")
fit.lnorm <- fitdist(data$wait_time, "lnorm")
fit.gamma <- fitdist(data$wait_time, "gamma")
fit.exp <- fitdist(data$wait_time, "exp")

# Kar????la??t??rma
gofstat(list(fit.norm, fit.lnorm, fit.gamma, fit.exp))


descdist(data$queue_length, boot = 100)
fit.norm_q <- fitdist(data$queue_length, "norm")
fit.lnorm_q <- fitdist(data$queue_length, "lnorm")
fit.gamma_q <- fitdist(data$queue_length, "gamma")
fit.exp_q <- fitdist(data$queue_length, "exp")

gofstat(list(fit.norm_q, fit.lnorm_q, fit.gamma_q, fit.exp_q))




