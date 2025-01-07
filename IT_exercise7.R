####################################################### IT Exercise 7
### Plotting a basic sin function
x <- seq(0,8*pi,length.out=100)
y <- sin(x)
plot(x,y,type="l")

### Plotting a basic cos function
x <- seq(0,8*pi,length.out=100)
y <- cos(x)
plot(x,y,type="l")

### Plotting a sin function for Task 1b
x <- seq(0.2*pi,length.out=12)
y <- 4/pi*((sin(x)+sin(3*x)/3)+(sin(5*x)/5)+(sin(7*x)/7)+(sin(9*x)/9))
plot(x,y,type="l")

### Natural Log
3^4
exp(4*log(3))

### Log Base 2
log2(3)
log(3)/log(2)













