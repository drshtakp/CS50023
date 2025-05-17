import panda as pd
df = pd.read_csv("palindrome.txt", header=None, names=["palindrome"])
df.to_html("output.html")