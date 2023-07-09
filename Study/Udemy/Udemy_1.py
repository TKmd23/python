def image_info(dicter: dict):
    if 'image_title' not in dicter.keys() or 'image_id' not in dicter.keys():
        raise ValueError("Fuck you")
    return f"Image {dicter['image_title']} has id {dicter['image_id']}"


test = {'image_title': "My cat",
        'image_id': "2307"}

try:
    print(image_info(test))
except ValueError as e:
    print(e)
else:
    print("no problems")

print("all done")