# print("Adelaide".strip('A'))
#
# imelda = "More Mayhem", "Imelda May", "2011", (
#     (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))
#
# with open("imelda3.txt", 'w') as imelda_file:
#     print(imelda, file=imelda_file)

# with open("imelda3.txt", 'r') as imelda_file:
#     contents = imelda_file.readline()
# imelda = eval(contents)
#
# print(imelda)
# title, artist, year, tracks = imelda
# print(artist)
# print(year)

# timesTable = []
# for i in range(0, 12):
#     timesTable.append(" {} times 2 is {}".format(i+1, (i+1)*2))
#     # print(i)
#
# for line in timesTable:
#     print(line)

# with open("sample.txt", 'w') as sample_file:
#     for line in timesTable:
#         print(line, file=sample_file)

with open("sample2.txt", 'w') as tables:
    for i in range(2, 13):
        for j in range(1, 13):
            print("{1:>2} times {0} is {2}".format(i, j, i*j), file=tables)
        print("="* 20, file=tables)
