import random
with open("heading.txt") as f1:

    title_h1 = f1.readline()
    s = (title_h1.split(","))
    title_h1_tag = random.choice(s)

A= "<h1>"+'Top 10 best'+" "+ "Keyword1"+" "+title_h1_tag +" "+"Review in 2022"+"<h1/>"
print(A.replace("Keyword1", "baitcasting reel"))

with open("h1title.txt") as f2:

    first_h2 = f2.readline()
    ss = (first_h2.split(","))
    first_h2_tag = random.choice(ss)

B= "<h2>"+'best'+" "+ "Keyword1"+ " "+first_h2_tag+"<h2/>"

print(B.replace("Keyword1", "baitcasting reel"))

