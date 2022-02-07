import os

def listposts():
    files = os.listdir("../public_gemini/")
    files.sort()
    return("\n".join(["=> "+_file for _file in files]))


with open("template.gmi") as f:
    s = f.read()
    final = s.replace("{{ listposts }}", listposts())
    with open("../public_gemini/index.gmi", "w") as out:
        out.write(final)
