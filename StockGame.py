from pandas_datareader import data
import matplotlib.pyplot as plt
import pandas as pd
import os
import datetime

def main():
    finish=0;
    print("Disclaimer: You cannot put in a date for a Buy or Sell that is a weekend or if it is not before close on the day of.")
    while finish==0:
        operation=raw_input("What Operation would you like to do? Buy? Sell? Check Portfolio? Update Portfolio? Reset Game? Close App?")
        if operation == 'Buy':
            cost=Closecost(operation)
            Buy=StoreBuy(cost[0],cost[1],cost[2])
        elif operation == 'Sell':
            sell=SellStock()
            net=Net()
        elif operation == 'Check Portfolio':
            portfolio=ReadPortfolio()
        elif operation == 'Update Portfolio':
            portfolio=UpdatePortfolio()
            
        elif  operation == 'Reset Game':
            if os.path.isfile("./Stock.txt"):
                os.remove("./Stock.txt")
            if os.path.isfile("./GainsLosses.txt"):
                os.remove("./GainsLosses.txt")
            if os.path.isfile("./SellStock.txt"):
                os.remove("./SellStock.txt")
        elif  operation == 'Research':
            alpha=Research()
        elif  operation == 'Close':
            finish=1
def StoreBuy(Name,buycost,number):
    if os.path.isfile("./Stock.txt"):
        buycost=str(buycost)
        # Need to check if stock is already bought
        f=open("Stock.txt","a")
        f.write(Name + " \r\n")
        f.write(buycost + " \r\n")
        f.write(number + " \r\n")
        totalcost=(float(buycost)*float(number))
        Change= str((float(totalcost)-float(totalcost))/(float(totalcost)))
        totalcost=str(totalcost)
        f.write(totalcost + " \r\n")
        f.write(totalcost + " \r\n")
        f.write(Change + " \r\n")
    else:
        buycost=str(buycost)
        f=open("Stock.txt","w")
        f.write(Name + " \r\n")
        f.write(buycost + " \r\n")
        f.write(number + " \r\n")
        totalcost=(float(buycost)*float(number))
        Change= str((float(totalcost)-float(totalcost))/(float(totalcost)))
        totalcost=str(totalcost)
        f.write(totalcost + " \r\n")
        f.write(totalcost + " \r\n")
        f.write(Change + " \r\n")
    
def Closecost(Type):
    if Type == 'Buy':
        date=raw_input("Enter Date to Buy Stock in the Format 2019-04-30")
        ticker=raw_input("Enter Stock Ticker")
        number=raw_input("Enter Number of stocks to buy")
        panel_data = data.DataReader(ticker, 'iex', date, date)
        print("You are buying " + ticker + ' at a price of')
        print(panel_data.iloc[0]['close'])
        return[ticker,(panel_data.iloc[0]['close']),number]
    elif Type == 'Sell':
        date=raw_input("Enter Date to Sell Stock in the Format 2019-04-30")
        ticker=raw_input("Enter Stock Ticker")
        number=raw_input("Enter Number of stocks to sell")
        panel_data = data.DataReader(ticker, 'iex', date, date)
        print("You are selling " + ticker + ' at a price of')
        print(panel_data.iloc[0]['close'])
        return[ticker,(panel_data.iloc[0]['close']),number]
def StorePlayers(players):
    f=open("playernames.txt","w")
    for y in players:
        f.write(y + " \r\n")
    f.close()

def ReadPlayers():
    g= open("playernames.txt","r")
    f1= g.readlines()
    for x in f1:
        print(x)
    g.close()
def ReadPortfolio():
    if os.path.isfile("./Stock.txt"):
        g= open("Stock.txt","r")
        f1= g.readlines()
        i=0;
        for x in f1:
            i+=1
            if i>6:
                i=1;
                
            if i==3:
                print("Number of Stocks = " +x)
            elif i == 2:
                print("Bought at = " +x)
            elif i == 1:
                print("Stock Name = " +x)
            elif i == 4:
                print("Bought Value = " +x)
            elif i == 5:
                print("Current Value = " +x)
            elif i == 6:
                print("% Change = " +x)
            else:
                print(x)
        g.close()
    else:
        print("You do not have a portfolio currently")
    if os.path.isfile("./GainsLosses.txt"):
        z= open("GainsLosses.txt","r")
        z1=z.readlines()
        for x in z1:
            print("Net Gain/Loss so Far:" + x + " \r\n")
    else:
        print("You Have not Sold any Stocks yet, so there is no Net Gain Loss Information Yet"+ " \r\n")
def UpdatePortfolio():
    date=raw_input("Enter the most recent date(not Weekend or before close) in the Format 2019-04-30")
    if os.path.isfile("./Stock.txt"):
        g= open("Stock.txt","r")
        f1= g.readlines()
        i=0;
        f=open("Stock2.txt","w")
        for x in f1:
            i+=1
            if i>6:
                i=1;
                
            if i==3:
                print("Number of Stocks = " +x)
                no=x[:-3];
                f.write(x)
            elif i == 2:
                print("Bought at = " +x)
                f.write(x)
            elif i == 1:
                print("Stock Name = " +x)
                tick=x[:-3];
                f.write(x)
            elif i == 4:
                BV=float(x[:-3])
                print("Bought Value = " +x)
                f.write(x)
            elif i == 5:
                now = datetime.datetime.now() #need to add it in
                panel_data = data.DataReader(tick, 'iex', date, date)
                z=str(panel_data.iloc[0]['close'])
                CurrVal=str(float(z)*float(no))
                print("Current Value = " +CurrVal +" \r\n")
                f.write(CurrVal + " \r\n")
            elif i == 6:
                Change=str(((float(CurrVal)-BV)/BV)*100)
                print("% Change = " +Change)
                f.write(Change + " \r\n")
            else:
                print(x)
        g.close()
        f.close()
        os.remove("./Stock.txt")
        os.rename("Stock2.txt","Stock.txt")

def SellStock():
    date=raw_input("Enter the date to sell(not Weekend or before close) in the Format 2019-04-30")
    if os.path.isfile("./Stock.txt"):
        ticker=raw_input("Enter Stock Ticker to Sell")
        g= open("Stock.txt","r")
        f1= g.readlines()
        i=0;
        f=open("Stock2.txt","w")
        h= open("SellStock.txt","w")
        for x in f1:
            i+=1
            if i>6:
                i=1;
                
            if i==3:
                no=x[:-3];
                if sell==0:
                    f.write(x)
            elif i == 2:
                if sell==0:
                    f.write(x)                
            elif i == 1:
                tick=x[:-3];
                if tick == ticker:
                    sell=1
                else:
                    sell=0
                    f.write(x)
            elif i == 4:
                BV=float(x[:-3])
                if sell==0:
                    f.write(x)
            elif i == 5:
                now = datetime.datetime.now() #need to add it in
                panel_data = data.DataReader(tick, 'iex', '2019-05-01', '2019-05-01')
                z=str(panel_data.iloc[0]['close'])
                CurrVal=str(float(z)*float(no))
                if sell==0:
                    f.write(CurrVal + " \r\n")
                elif sell==1:
                    netValue=float(CurrVal)-float(BV)
                    print("Sold for a net gain/loss of" +str(netValue))
                    h.write(str(netValue))
            elif i == 6:
                Change=str(((float(CurrVal)-BV)/BV)*100)
                if sell==0:
                    f.write(Change + " \r\n")
            else:
                print(x)
        g.close()
        f.close()
        os.remove("./Stock.txt")
        os.rename("Stock2.txt","Stock.txt")
        
    else:
        print("You do not have a portfolio currently")

def Net():
    h= open("SellStock.txt","r")
    h1=h.readlines()
    for x in h1:
        NetSoldStock=x
    if os.path.isfile("./GainsLosses.txt"):
        z= open("GainsLosses.txt","r")
        z1=z.readlines()
        for x in z1:
            TotalGainLoss=float(x)
        Total=str(float(NetSoldStock)+TotalGainLoss)
        z.close()
        z= open("GainsLosses.txt","w")
        z.write(Total)
        z.close()
    else:
        z= open("GainsLosses.txt","w")
        z.write(NetSoldStock)
        z.close()
    h.close()
def Research():
    ticker=raw_input("Enter Stock Ticker")
    start_date=raw_input("Enter Start Date no more than 5 years ago in format like 2018-05-01")
    end_date=raw_input("Enter End Date no more than 5 years ago in format like 2019-05-01")
    panel_data = data.DataReader(ticker, 'iex',start_date,end_date)
    all_weekdays = pd.date_range(start=start_date, end=end_date, freq='B')

    close=panel_data['close']
    i=0;
    p=[]
    s=[]
    while i< len(close):
        p.append(close[i])
        s.append(all_weekdays[i])
        i=i+1

    plt.plot(s,p,label=ticker)
    plt.show()



if __name__== '__main__':
    main()
