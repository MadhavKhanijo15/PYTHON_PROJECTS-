'''Program that prompts the user for the name of a file and then outputs that file’s media type if the file’s name ends, case-insensitively, in any of these suffixes:
.gif
.jpg
.jpeg
.png
.pdf
.txt
.zip
If the file’s name ends with some other suffix or has no suffix at all, output application/octet-stream instead, which is a common default'''

Prompt=input("Name of the file:").lower().strip()
if Prompt.endswith(".gif"):
    print("image/gif")
elif Prompt.endswith(".jpg") or Prompt.endswith(".jpeg"):
    print("image/jpeg")
elif Prompt.endswith(".png"):
    print("image/png")
elif Prompt.endswith(".pdf"):
    print("application/pdf")
elif Prompt.endswith(".txt"):
    print("text/plain")
elif Prompt.endswith(".zip"):
    print("application/zip")
else: print("application/octet-stream")
