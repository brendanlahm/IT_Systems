################################# Golden-section search algorithm
### Define golden ratios
golden_ratio1 <- as.numeric(format(round(34/89,3)))
golden_ratio2 <- as.numeric(format(round((sqrt(5)-1)/2,3)))

### Define a unimodal function
f <- function(x){
  
  # Monotonic increasing function
  return((x*2)-1)
  
  # Monotonic decreasing function
  #return((x*(-2))+100)
  
}

### Define golden-section search algorithm
gss <- function(f, a, b){
  
  lambda <<- as.numeric(format(round(a + golden_ratio1*(b-a),3)))
  mu <<- as.numeric(format(round(a + golden_ratio2*(b-a),3)))
  print(lambda)
  print(mu)
  if(f(lambda) > f(mu)){
    while(b-lambda > 0.1){
    
      min <- paste0("New minimum is ", lambda)
      print(min)
      max <- paste0("Maximum remains ", b)
      print(max)
      gss(f, lambda, b)
      
    }

  } else {
    while(mu-a > 0.1){
      
      min <- paste0("Minimum remains ", a)
      print(min)
      max <- paste0("New maximum is ", mu)
      print(max)
      gss(f, a, mu)

    }
  }
  
}






