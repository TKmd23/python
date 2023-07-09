import json

json_str = '{"id": 235, "band": "Nike", "qty": 84, "status": {"isForSale": true}}'
json_array = '[1, 2, 3]'

sneakers = json.loads(json_str)
my_list = json.loads(json_array)

new_sneakers = {'id': 235,
                'band': "Nike",
                'qty': 84,
                'status': {'isForSale': True}
                }

json_from_dict = json.dumps(new_sneakers, indent=4)
print(json_from_dict)



