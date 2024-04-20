# AUTHOR: CALITHOS4136

# getting user input
text = input("File Name: ").strip().lower()

if not text.find(".") == -1:
    exten = text.split(".")[-1]

    if exten.find("gif") != -1 or exten.find("png") != -1 or exten.find("jpg") != -1 or exten.find("jpeg") != -1:

        if exten.find("jpg") != -1:
            exten = "jpeg"

        print(f"image/{exten}")

    elif exten.find("pdf") != -1 or exten.find("zip") != -1:

        print(f"application/{exten}")

    elif exten.find("txt") != -1:

        print(f"text/plain")

    else:
        print(f"application/octet-stream")


else:
    print(f"application/octet-stream")

# EOF

