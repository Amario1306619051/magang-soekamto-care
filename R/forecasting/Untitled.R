library(tseries)
library(forecast)
library(lmtest)
library(normtest)
library(nortest)

setwd("/Users/amariofausta/Documents/Magang/R/forecasting")
data <- read.csv("DATA1.csv",sep=";")
data

#menampilkan data
penjualan <- data$zt
bulan <- data$t
ts.plot(penjualan)

#menstasionerkan variansi data
BoxCox.lambda(penjualan)

loga <- log(penjualan)
loga

ts.plot(loga)

#plotting acf dan pacf
par(mfrow=c(1,2))
acf(loga,max = 56)
pacf(loga,max=56)

#differencing 1 non musiman
differencing1 <- diff(loga,differences = 1)
differencing1
ts.plot(differencing1)
acf(differencing1,lag.max = 70)
pacf(differencing1,lag.max = 70)
adf.test(differencing1)

#differencing 1 musiman
diffnonmus <- diff(differencing1,lag = 12)
diffnonmus
ts.plot(diffnonmus)
par(mfrow=c(1,2))
acf(diffnonmus,lag.max = 70)
pacf(diffnonmus,lag.max=70)
adf.test(diffnonmus)


#ARIMA(0,1,1)(0,1,1)
fit3 <- arima(loga,order=c(0,1,1),seasonal=list(order=c(0,1,1),period=12,method="ML"))
fit3

#diagnostic checking
#uji kesignifikan parameter
print('Hasil kesignifikan parameter')
coeftest(fit3)

#uji residual white nose
print('Hasil uji residual white noise')
Box.test(fit3$residuals,type="Ljung")

#uji residual apakah berdistribusi normal
print('Hasil uji residual berdistribusi normal')
shapiro.test(fit3$residuals)

#shapiro-Francia mormalitty test
print("Hasil Normaliti tes")
sf.test(fit3$residuals)

fit4 <- arima(loga,order=c(0,1,1),seasonal=list(order=c(1,1,1),period=12,method="ML"))
fit4

#diagnostic checking
#uji kesignifikan parameter
coeftest(fit4)

#uji residual white nose
Box.test(fit4$residuals,type="Ljung")

#uji residual apakah berdistribusi normal
Shapiro.test(fit4$residuals)

#shapiro-Francia mormalitty test
sf.test(fit4$residuals)

fit5 <- arima(loga,order=c(0,1,1),seasonal=list(order=c(1,1,0),period=12,method="ML"))
fit5

#diagnostic checking
#uji kesignifikan parameter
coeftest(fit5)

#uji residual white nose
Box.test(fit5$residuals,type="Ljung")

#uji residual apakah berdistribusi normal
shapiro.test(fit5$residuals)

#shapiro-Francia mormalitty test
sf.test(fit5$residuals)

#peramalan
forecasting <- forecast(loga,model = fit3, h =12)
forecasting
plot(forecasting)