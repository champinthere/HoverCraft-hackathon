

def latexHeader():
    return """
\\documentclass[11pt]{article}
\\usepackage[margin=1.2in]{geometry}
\\usepackage{amsmath}
\\usepackage{mathpazo}
\\linespread{2.0}
\\begin{document}
"""


def makeTitle():
    return """
\\title{Generated Calculator Number Crunchers}
\\author{}
\\maketitle
"""


def latexClose():
    return """
\\end{document}
"""


def beginList():
    return """
\\begin{enumerate}
"""


def endList():
    return """
\\end{enumerate}
"""


def addItem(s):
    return "\\item " + s


def flalign(s):
    return "\\begin{flalign*}\n& " + s + " &\n\\end{flalign*}"


if __name__ == '__main__':
    print(latexHeader(), makeTitle(), beginList(),
            addItem(flalign("\\frac{2}{5}")), endList(), latexClose())
