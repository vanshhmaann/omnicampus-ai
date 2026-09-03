import sys, base64, os
path = sys.argv[1]
b64_data = sys.argv[2]
os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
with open(path, "wb") as f:
    f.write(base64.b64decode(b64_data))
print("Wrote successfully:", path)
