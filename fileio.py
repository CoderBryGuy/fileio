# jabber = open("C:\\Users\\Bryan\\Downloads\\sample.txt", 'r')
#
# for line in jabber:
#     if "jabberwock" in line.lower():
#         print(line, end='')
#
# jabber.close()
#
# print("*" * 40)
#
# with open("C:\\Users\\Bryan\\Downloads\\sample.txt", 'r') as jabber:
#     for line in jabber:
#         if "JAB" in line.upper():
#             print(line, end='')

# with open("C:\\Users\\Bryan\\Downloads\\sample.txt", "r") as jabber:
#     line = jabber.readline()
#     while line:
#         print(line, end='')
#         line = jabber.readline()
#

# with open("C:\\Users\\Bryan\\Downloads\\sample.txt", "r") as jabber:
#     lines = jabber.readlines()
# print(lines)
#
# for line in lines:
#     print(line, end='')


# with open("C:\\Users\\Bryan\\Downloads\\sample.txt", "r") as jabber:
#     lines = jabber.readlines()
# print(lines)
#
# for line in lines[::-1]:
#     print(line, end='')


# with open("C:\\Users\\Bryan\\Downloads\\sample.txt", "r") as jabber:
#     lines = jabber.read()
# print(lines)
#
# for line in lines[::-1]:
#     print(line, end='')

with open("C:\\Users\\Bryan\\Downloads\\sample.txt", "r") as jabber:
    lines = jabber.readlines()


with open("sample.txt", "w") as sample:
    for line in lines:
        print(line, file=sample)
