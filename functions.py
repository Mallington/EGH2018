from math import exp,log

def simMovAvg(data,lastAvg,n):
    if len(data)<=n:
        #return(sum(data[-n:])/n)
        return lastaverage+data[-1]
    else:
        return lastaverage+data[-1]-data[-1-n]

def expMovAvg(lastVal,lastAvg,halfLife):
    #a = exp(log(0.5)/halfLife)
    a=halfLife
    return (lastAvg+a*(lastVal-lastAvg))#(a*lastVal)+((1-a)*lastAvg)

 
