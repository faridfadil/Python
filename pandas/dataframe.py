import pandas as pd 

dictionary = {
	"fname": ["John", "Don", "Tom"],
	"lname": ["Pedro", "John", "Engine"],
	"age": [22, 52, 15]
}

df = pd.DataFrame(dictionary)

filt = df["age"] < 50
indexChange = df.set_index("fname")


input()