#Inyamah Amaefule
#ainyamah@yahoo.com
#Hamaamah Bakare
#Mini Project: Prototype of a Magento order placement software for an e-commerce store.

LV=1
Feragamo=2
versas=3
kappa=4
religion=5
Gio_GioAmani=6
HugoBoss=7
Gucci=8
GucciGabani=9
Yohiyamamoto=10
shoe=int(input("choose a Shoe \n1. LV\n2.Feragamo\n3.versa\n4.kappa\n5.Gio-GioAmani\n7.HogoBoss\n8.Gucci\n9gucci&Gabani\n10.Yohiyamamoto\n"))
if(shoe==1):
               size=input("Please what is your shoe size(LV)\n")
               colour=input("Please choose a color for you shoe(LV):\n")
               Amount=input("please enter the Am,out of your selected shoe(LV):\n")
               Checkout=size+ " "+colour+" " +Amount
               print(Checkout)
elif(shoe==2):
    size=input("Please what is your shoe size(Feragamo)\n")
    colour=input("Please choose a color for you shoe(Feragamo):\n")
    Amount=input("please enter the Am,out of your selected shoe(Feragamo):\n")
    Checkout=size+ " "+colour+" " +Amount
    print(Checkout)
elif(shoe==3):
     size=input("Please what is your shoe size(versas)\n")
     colour=input("Please choose a color for you shoe(versas):\n")
     Amount=input("please enter the Am,out of your selected shoe(versas):\n")
     Checkout=size+ " "+colour+" " +Amount
     print(Checkout)
elif(shoe==4):
     size=input("Please what is your shoe size(kappa)\n")
     colour=input("Please choose a color for you shoe(kappa:\n")
     Amount=input("please enter the Am,out of your selected shoe(kappa):\n")
     Checkout=size+ " "+colour+" " +Amount
     print(Checkout)
elif(shoe==5):
    size=input("Please what is your shoe size(religion)\n")
    colour=input("Please choose a color for you shoe(religion):\n")
    Amount=input("please enter the Am,out of your selected shoe(religion):\n")
    Checkout=size+ " "+colour+" " +Amount
    print(Checkout)
elif(shoe==6):
    size=input("Please what is your shoe size(Gio_GioAmani)\n")
    colour=input("Please choose a color for you shoe(Gio_GioAmani):\n")
    Amount=input("please enter the Am,out of your selected shoe(Gio_GioAmani):\n")
    Checkout=size+ " "+colour+" " +Amount
    print(Checkout)
               



else:
                        print("The shoe is not available")
                        

