import requests

bit_list = []
resp = requests.get("https://coinmarketcap.com/")
resp_txt = resp.text
parse = resp_txt.split("<span>")
for i in parse:
    if i.startswith("$"):
        for y in i.split("</span>"):
            if y.startswith("$") and y[1].isdigit():
                bit_list.append(y)

bitcoin = bit_list[0]
print(bitcoin)