import json
x = '{"name":"Ahmed", "age":21, "gender":"male"}'
y = json.loads(x)
print(y["age"])