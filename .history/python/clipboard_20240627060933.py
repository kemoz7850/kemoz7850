import sys
link = "https://fmovies24.to/tv/house-qk23/7-19"
lst = []
num = ""
for count, i in enumerate(link):
    if i == '-':
        lst.append(count)
max = max(lst)+1
for i in link[max:]:
    num += i
print(int(num)
temp = list(link)
temp[len(temp)-1] = str(int(temp[len(temp)-1])+1)
link = "".join(temp)
print(link)
# with open("output.txt", "w") as file:
#     file.write(str(link))