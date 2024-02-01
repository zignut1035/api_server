import requests

url = "http://127.0.0.1:8000"
fac = requests.post(url + "/api/factorial", data = {
    "number": 4,
    "action":"factorial"
})
print(fac.json())
med = requests.post(url + "/api/median", data = {
    "numbers": [1,2,3,4],
    "action":"median"
})
print(med.json())
var = requests.post(url + "/api/variance", data = {
    "numbers": [1,2,3,4],
    "action":"variance"
})
print(var.json())
std = requests.post(url + "/api/pstdev" , data = {
    "numbers":[1,2,3,4],
    "action":"standard"
})
print(std.json())