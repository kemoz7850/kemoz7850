import sys

link = "https://fmovies24.to/tv/house-qk23/7-8"
temp = list(link)
temp[len(temp)-1] = char(int(link[len(link)-1])+1)
print(link)
# with open("output.txt", "w") as file:
#     file.write(str(link))