from math import exp,log

def simMovAvg(data,lastAvg,n):
    if len(data)<=n:
        #return(sum(data[-n:])/n)
        return lastAvg+data[-1]
    else:
        return lastAvg+data[-1]-data[-1-n]

def getα(halfLife):
    return exp(log(0.5)/halfLife)

def expMovAvg(lastVal,lastEMA,halfLife):
    a=getα(halfLife)
    return (lastEMA+a*(lastVal-lastEMA))#(a*lastVal)+((1-a)*lastAvg)

def movStandDev(data,lastSMA,curSMA,n):
    if len(data)<n:
        return 0
    elif len(data)==n:
        avg=sum(data)/n
        tot = 0
        for x in range(n):
            tot+data[x]-avg
        return (tot/(n-1))**0.5
    else:
        var = ((data[-1]-data[-n-1])*(data[-1]-curSMA+data[-n-1]-lastSMA))/(n-1)
        return var**0.5

def expVar(lastVal,lastEMA,lastVAR,halfLife):
    a=getα(halfLife)
    return (lastVAR+a*(lastVal-LastEMA)**2)*(1-a)

def expMovStandDev(expVAR):
    return (expVAR)**0.5    

    
