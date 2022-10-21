import random
with open("file_1.txt") as f1, open("file_2.txt") as f2, open("file_3.txt") as f3:

    line_file1 = f1.readline()

    s=(line_file1.split(","))
    first_line = random.choice(s)

    line_file2 = f2.readline()

    ss = (line_file2.split(","))
    second_line = random.choice(ss)


    line_file3 = f3.readline()

    sss = (line_file3.split(","))
    third_line = random.choice(sss)
    final=(first_line + second_line + third_line)

    print(final.replace("good", "best"))