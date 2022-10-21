import random
with open("title.txt") as f1:

    title_h1 = f1.readline()
    s = (title_h1.split(","))
    base_keyword = random.choice(s)

print("<h1>"+'Top 10 best'+" "+ base_keyword+ "<h1/>")

