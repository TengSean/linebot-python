# %%
import json

# with open('./tutorial/items.json', 'r') as f:
#     jd = [json.loads(line) for line in f]

# %%
import os

# os.getcwd()
with open('./linebot-python/tutorial/items.json', 'r') as f:
    a = f.read()
print(a[0])

# %%
import json , os

print(os.getcwd())
with open('./tutorial/2020-07-26.json', 'r', ) as f:
    a = json.load(f)
print(json.dumps(a, indent=4, ensure_ascii=False))

# %%
