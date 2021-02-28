from utils import mapping
from os.path import splitext, basename
import string
import glob

raw_iast_files = glob.glob("raw_iast/*.txt")

def getDoc(f):
    doc = None
    with open(f, 'r') as fp:
        doc = fp.read()
    return doc

def iastToLatex(iast):
    table = iast.maketrans(mapping.transliteration)
    return iast.translate(table)

def makeDoc(name, latex):
    print(f'Saving latex version of {name}')
    with open(f'iast_latex/{name}.tex', 'w') as fp:
        fp.writelines(latex)

def main():
    try:
        docs = ( getDoc(f) for f in raw_iast_files )
        texs = ( iastToLatex(doc) for doc in docs )
        for i, tex in enumerate(texs):
            makeDoc(splitext(basename(raw_iast_files[i]))[0], tex)
    except Exception as e:
        print(f'There is an error: {e}')

if __name__ == "__main__":
    main()




