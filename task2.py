while True:
    file_name=input("ENTER the filename with extension: ")
    name_split=file_name.split(".")
    ext=name_split[-1]
    if ext=="py":
        print("It's a PYTHON FILE")
    elif ext=="pdf":
        print("It's a PDF FILE")
    elif ext=="txt":
        print("It's a PLAIN TEXT FILE")
    elif (ext=="doc")or(ext=="docx"):
        print("It's a MICROSOFT WORD FILE")
    elif (ext=="html")or(ext=="htm"):
        print("It's a HTML FILE")
    elif (ext=="ppt")or(ext=="pptx"):
        print("It's a MICROSOFT POWERPOINT FILE")
    elif ("close") or ("exit") in file_name:
        break
