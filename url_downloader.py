import wget

filename = input("File with urls, will download all urls from txt file EX: urls.txt  : ")

url_list = open(filename, "r")

for URL in url_list:
    URL = URL.replace("\n", "")
    name = URL.split("/")
    name = name[len(name) - 1]
    print(name)
    response = wget.download(URL, name)
