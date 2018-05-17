#Oladeinde Kuti
#oladeinde.kuti@gmail.com
#07065931683
#Input your question
Questions=[]
X=0
Q1="What is the capital of Togo?"
Q2="What is the capital of Egypt?"
Q3="What is the capital of Kenya?"

Q1answers=['a.Lome','b.Cairo','c.Nairobi']
Q2answers=['a.Lome','b.Cairo','c.Nairobi']
Q3answers=['a.Lome','b.Cairo','c.Nairobi']

a=input(str("Press enter to begin"))
print(Q1)
for i in Q1answers:
        print(i)
b=input(str("Enter your answer: "))
if b=="a":
    X=X+1
else:
    X=X+0
print(Q2)
for i in Q2answers:
        print(i)
b=input(str("Enter your answer: "))
if b=="b":
    X=X+1
else:
    X=X+0
print(Q3)
for i in Q3answers:
        print(i)
b=input(str("Enter your answer: "))
if b=="c":
    X=X+1
else:
    X=X+0
print("Your final score is ",X," out of 3")

    

    

