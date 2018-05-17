# ADESHINA JAMIU OLUWADAMILARE
#oluwadamilare.adeshina@gmail.com
#08127271230
#EXCHANGE RATE CALC FOR NIGERIAN NAIRA
#CURRENCY VALUE PER CURRENCY
usdol=305.8
pounds=415.3987
euro=366.5013
swissfrance=306.305
yen=2.7924
cfa=0.5553
yuan=48.2449
riyal=81.5401
southafrican=24.9167
danishkrona=49.1774
sdr=437.5386
#COUNTRY CODE ELEMENT IN LIST
US=0
ENG=1
EUROPE=2
SWISS=3
CH=4
CFA=5
YUAN=6
RIYAL=7
SOUTH=8
DANISH=9
SDR=10
currency=[usdol,pounds,euro,swissfrance,yen,cfa,yuan,riyal,southafrican,danishkrona,sdr]
exchangecount=[US,ENG,EUROPE,SWISS,CH,CFA,YUAN,RIYAL,SOUTH,DANISH,SDR]
run=True
while run:
    print("Enter your conversion code: US=0 ENG=1 EUROPE=2 SWISS=3 CH=4 CFA=5 YUAN=6 RIYAL=7 SOUTH=8 DANISH=9 SDR=10")
    conv=int(input("Conversion code : "))
    for i in exchangecount:
        if conv==i:
            print("Enter your conversion rate")
            money=int(input("conversion rate : "))
            print(money*currency[i])
    print("press 1 to run again or 0 to exit")
    x=int(input("Your Option : "))
    if x == 1:
        run = True
    else:
        run = False
