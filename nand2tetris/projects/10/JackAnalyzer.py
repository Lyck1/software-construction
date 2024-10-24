import os
import sys



def main(argv: list[str]):
    targets = []
    sourceDir = argv[0]

    # Ensure we only attempt to compile a jack file
    if os.path.isfile(sourceDir):
        if not sourceDir.endswith('.jack'):
            print(f'Target {sourceDir} is not a valid source file')
            return
        targets.append(sourceDir)

    if os.path.isdir(sourceDir):
        files = os.listdir(sourceDir)
        jackFiles = [os.path.join(sourceDir, file) for file in files if file.endswith('.jack')]
        if not jackFiles:
            print(f'Folder {sourceDir} does not contain any jack files')
            return
        targets.extend(jackFiles)

    print(f'Parsing {len(targets)} targets')
    for target in targets:
        print(f'Parsing {target}')
        # Add your code here

        keywords = [
            'class', 'constructor', 'function', 'method',
            'field', 'static', 'var', 'int', 'char', 'boolean',
            'void', 'true', 'false', 'null', 'this', 'let',
            'do', 'if', 'else', 'while', 'return'
        ]

        symbols = [
            '{', '}', '(', ')', '[', ']', '.', ',', ';',
            '+', '-', '*', '/', '&', '|', '<', '>', '=', '~'
        ]


        path = target.split("\\")[1]
        tokenizer = open(path.removesuffix(".jack") + "T.xml", "w")
        with open(target, 'r') as f:
            in_word = False
            in_string = False
            in_comment = False
            word = ""
            string = ""
            tokenizer.write("<tokens>\n")
            for line in f:
                line = line.strip()
                if line.startswith("//"):
                    continue
                elif line.startswith("/**"):
                    in_comment = True
                    if line.endswith("*/"):
                        in_comment = False
                        continue
                    continue
                elif in_comment == True:
                    if line.endswith("*/"):
                        in_comment = False
                        continue
                    else:
                        continue
                elif "//" in line:
                    line = line.split("//")[0]
                for c in line:
                    if in_string:
                        if c == '"':
                            tokenizer.write("<stringConstant>"+string+"</stringConstant>\n")
                            in_string = False
                        else:
                            string = string + c
                    elif in_word:
                        if c.isalnum() or c == "_":
                            word = word + c
                        else:
                            in_word = False
                            if word in keywords:
                                tokenizer.write("<keyword>"+word+"</keyword>\n")
                            elif word.isnumeric():
                                tokenizer.write("<integerConstant>"+word+"</integerConstant>\n")
                            else:
                                tokenizer.write("<identifier>"+word+"</identifier>\n")
                            word = ""
                            if c in symbols:
                                if c == "<":
                                    tokenizer.write("<symbol>&lt;</symbol>\n")
                                elif c == ">":
                                    tokenizer.write("<symbol>&gt;</symbol>\n")
                                elif c == "&":
                                    tokenizer.write("<symbol>&amp;</symbol>\n")
                                else:
                                    tokenizer.write("<symbol>" + c + "</symbol>\n")
                    else:
                        if c == '"':
                            in_string = True
                            string = ""
                        elif c.isalnum():
                            in_word = True
                            word = c
                        elif c in symbols:
                            if c == "<":
                                tokenizer.write("<symbol>&lt;</symbol>\n")
                            elif c == ">":
                                tokenizer.write("<symbol>&gt;</symbol>\n")
                            elif c == "&":
                                tokenizer.write("<symbol>&amp;</symbol>\n")
                            else:
                                tokenizer.write("<symbol>"+c+"</symbol>\n")
            tokenizer.write("</tokens>\n")


        print(f'{target} parsed successfully')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f'Usage: {sys.argv[0]} [source]')
        exit()
    main(sys.argv[1:])
