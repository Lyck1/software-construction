# Implement your project 8 here
import glob
import os
import sys
from pathlib import Path

class Code:
    def __init__(self, output_file_name):
        self.ofn = output_file_name
        self.labels = {}
        self.ofd = open(output_file_name, "w")
        self.base_fn = "bootstrap"

    def set_input_file(self, fn):
        self.base_fn = Path(fn).stem

    def new_label(self, label):
        if label in self.labels:
            self.labels[label] = self.labels[label] + 1
        else:
            self.labels[label] = 1

    def replace_labels(self, s):
        for label in self.labels:
            # replace <LABEL> to LABEL1 (or LABEL2, LABEL3...)
            s = s.replace("<" + label + ">", label + str(self.labels[label]))
        s = s.replace("<FILENAME>", self.base_fn)
        return s

    def emit(self, s):
        s = self.replace_labels(s)
        self.ofd.write(s)
        self.ofd.write("\n")

    def emit_comment(self, comment):
        comment = self.replace_labels(comment)
        self.ofd.write("// ")
        self.ofd.write(comment)
        if comment[-1] != "\n":
            self.ofd.write("\n")

    def close(self):
        self.ofd.close()

    def __exit__(self, *args):
        self.close()
def op_push(args, code):
    memorysegment=args[0]
    value=int(args[1])

    match memorysegment:
        case "constant":
            code.emit("@"+str(value)+"")
            code.emit("D=A")
            code.emit("@SP")
            code.emit("A=M")
            code.emit("M=D")
            code.emit("@SP")
            code.emit("M=M+1")
        case "local":
            code.emit("@LCL")
            code.emit("A=M")
            while value>0:
                value=value-1
                code.emit("A=A+1")
            code.emit("D=M")
            code.emit("@SP")
            code.emit("A=M")
            code.emit("M=D")
            code.emit("@SP")
            code.emit("M=M+1")
        case "argument":
            code.emit("@ARG")
            code.emit("A=M")
            while value > 0:
                value = value - 1
                code.emit("A=A+1")
            code.emit("D=M")
            code.emit("@SP")
            code.emit("A=M")
            code.emit("M=D")
            code.emit("@SP")
            code.emit("M=M+1")
        case "this":
            code.emit("@THIS")
            code.emit("A=M")
            while value > 0:
                value = value - 1
                code.emit("A=A+1")
            code.emit("D=M")
            code.emit("@SP")
            code.emit("A=M")
            code.emit("M=D")
            code.emit("@SP")
            code.emit("M=M+1")
        case "that":
            code.emit("@THAT")
            code.emit("A=M")
            while value > 0:
                value = value - 1
                code.emit("A=A+1")
            code.emit("D=M")
            code.emit("@SP")
            code.emit("A=M")
            code.emit("M=D")
            code.emit("@SP")
            code.emit("M=M+1")
        case "temp":
            code.emit("@5")
            while value > 0:
                value = value - 1
                code.emit("A=A+1")
            code.emit("D=M")
            code.emit("@SP")
            code.emit("A=M")
            code.emit("M=D")
            code.emit("@SP")
            code.emit("M=M+1")
        case "pointer":
            if value==0:
                code.emit("@THIS")
                code.emit("D=M")
                code.emit("@SP")
                code.emit("A=M")
                code.emit("M=D")
                code.emit("@SP")
                code.emit("M=M+1")
            else:
                code.emit("@THAT")
                code.emit("D=M")
                code.emit("@SP")
                code.emit("A=M")
                code.emit("M=D")
                code.emit("@SP")
                code.emit("M=M+1")
        case "static":
            code.emit("@"+ code.base_fn + "." + str(value))
            code.emit("D=M")
            code.emit("@SP")
            code.emit("A=M")
            code.emit("M=D")
            code.emit("@SP")
            code.emit("M=M+1")
        case "_":
            raise Exception("Unknown memory segment"+memorysegment)

def op_pop(args, code):
    memorysegment=args[0]
    value=int(args[1])

    match memorysegment:
        case "local":
            code.emit("@SP")
            code.emit("A=M")
            code.emit("A=A-1")
            code.emit("D=M")
            code.emit("@SP")
            code.emit("M=M-1")
            code.emit("@LCL")
            code.emit("A=M")
            while value>0:
                value=value-1
                code.emit("A=A+1")
            code.emit("M=D")
        case "argument":
            code.emit("@SP")
            code.emit("A=M")
            code.emit("A=A-1")
            code.emit("D=M")
            code.emit("@SP")
            code.emit("M=M-1")
            code.emit("@ARG")
            code.emit("A=M")
            while value > 0:
                value = value - 1
                code.emit("A=A+1")
            code.emit("M=D")
        case "this":
            code.emit("@SP")
            code.emit("A=M")
            code.emit("A=A-1")
            code.emit("D=M")
            code.emit("@SP")
            code.emit("M=M-1")
            code.emit("@THIS")
            code.emit("A=M")
            while value > 0:
                value = value - 1
                code.emit("A=A+1")
            code.emit("M=D")
        case "that":
            code.emit("@SP")
            code.emit("A=M")
            code.emit("A=A-1")
            code.emit("D=M")
            code.emit("@SP")
            code.emit("M=M-1")
            code.emit("@THAT")
            code.emit("A=M")
            while value > 0:
                value = value - 1
                code.emit("A=A+1")
            code.emit("M=D")
        case "temp":
            code.emit("@SP")
            code.emit("A=M-1")
            code.emit("D=M")
            code.emit("@5")
            while value > 0:
                value = value - 1
                code.emit("A=A+1")
            code.emit("M=D")
            code.emit("@SP")
            code.emit("M=M-1")
        case "pointer":
            if value==0:
                code.emit("@SP")
                code.emit("A=M-1")
                code.emit("D=M")
                code.emit("@SP")
                code.emit("M=M-1")
                code.emit("@THIS")
                code.emit("M=D")
            else:
                code.emit("@SP")
                code.emit("A=M-1")
                code.emit("D=M")
                code.emit("@SP")
                code.emit("M=M-1")
                code.emit("@THAT")
                code.emit("M=D")
        case "static":
            code.emit("@SP")
            code.emit("A=M-1")
            code.emit("D=M")
            code.emit("@SP")
            code.emit("M=M-1")
            code.emit("@"+ code.base_fn + "." + str(value))
            code.emit("M=D")
        case "_":
            raise Exception("Unknown memory segment"+memorysegment)
def op_add(code):
    code.emit("@SP")
    code.emit("A=M-1")
    code.emit("D=M")
    code.emit("@SP")
    code.emit("M=M-1")
    code.emit("A=M")
    code.emit("A=A-1")
    code.emit("D=D+M")
    code.emit("M=D")
    pass
def op_sub(code):
    code.emit("@SP")
    code.emit("A=M-1")
    code.emit("A=A-1")
    code.emit("D=M")
    code.emit("A=A+1")
    code.emit("D=D-M")
    code.emit("A=A-1")
    code.emit("M=D")
    code.emit("@SP")
    code.emit("M=M-1")
    pass

def op_eq(code, counter):
    code.emit("@SP")
    code.emit("A=M-1")
    code.emit("D=M")
    code.emit("A=A-1")
    code.emit("D=D-M")

    code.emit("@EQ_TRUE" + str(counter) + "")
    code.emit("D;JEQ")

    code.emit("@SP")
    code.emit("A=M-1")
    code.emit("A=A-1")
    code.emit("M=0")

    code.emit("@END" + str(counter) + "")
    code.emit("0;JMP")

    code.emit("(EQ_TRUE" + str(counter) + ")")
    code.emit("@SP")
    code.emit("A=M-1")
    code.emit("A=A-1")
    code.emit("M=-1")

    code.emit("(END" + str(counter) + ")")
    code.emit("@SP")
    code.emit("M=M-1")

def op_lt(code, counter):
    code.emit("@SP")
    code.emit("A=M-1")
    code.emit("D=M")
    code.emit("A=A-1")
    code.emit("D=M-D")

    code.emit("@LT_TRUE" + str(counter) + "")
    code.emit("D;JLT")

    code.emit("@SP")
    code.emit("A=M-1")
    code.emit("A=A-1")
    code.emit("M=0")

    code.emit("@END" + str(counter) + "")
    code.emit("0;JMP")

    code.emit("(LT_TRUE" + str(counter) + ")")
    code.emit("@SP")
    code.emit("A=M-1")
    code.emit("A=A-1")
    code.emit("M=-1")

    code.emit("(END" + str(counter) + ")")
    code.emit("@SP")
    code.emit("M=M-1")
    pass

def op_gt(code, counter):
    code.emit("@SP")
    code.emit("A=M-1")
    code.emit("D=M")
    code.emit("A=A-1")
    code.emit("D=M-D")

    code.emit("@GT_TRUE" + str(counter) + "")
    code.emit("D;JGT")

    code.emit("@SP")
    code.emit("A=M-1")
    code.emit("A=A-1")
    code.emit("M=0")

    code.emit("@END" + str(counter) + "")
    code.emit("0;JMP")

    code.emit("(GT_TRUE" + str(counter) + ")")
    code.emit("@SP")
    code.emit("A=M-1")
    code.emit("A=A-1")
    code.emit("M=-1")

    code.emit("(END" + str(counter) + ")")
    code.emit("@SP")
    code.emit("M=M-1")
    pass

def op_neg(code):
    code.emit("@SP")
    code.emit("A=M")
    code.emit("M=0")
    code.emit("A=A-1")
    code.emit("D=M")
    code.emit("A=A+1")
    code.emit("D=M-D")
    code.emit("A=A-1")
    code.emit("M=D")

def op_and(code):
    code.emit("@SP")
    code.emit("A=M-1")
    code.emit("D=M")
    code.emit("A=A-1")
    code.emit("M=D&M")
    code.emit("@SP")
    code.emit("M=M-1")

def op_or(code):
    code.emit("@SP")
    code.emit("A=M-1")
    code.emit("D=M")
    code.emit("A=A-1")
    code.emit("M=D|M")
    code.emit("@SP")
    code.emit("M=M-1")

def op_not(code):
    code.emit("@SP")
    code.emit("A=M-1")
    code.emit("M=!M")

def op_label(args, code):
    memorysegment=args[0]
    code.emit("(" + memorysegment + ")")

def op_goto(args, code):
    memorysegment=args[0]
    code.emit("@" + memorysegment + "")
    code.emit("0;JMP")

def op_if_goto(args, code):
    memorysegment=args[0]
    code.emit("@SP")
    code.emit("M=M-1")
    code.emit("A=M")
    code.emit("D=M")
    code.emit("@" + memorysegment + "")
    code.emit("D;JNE")

def op_call(args, code, counter):
    memorysegment=args[0]
    nargs=args[1]

    code.emit("@retAddrLabel" + str(counter) + "")
    code.emit("D=A")
    code.emit("@SP")
    code.emit("A=M")
    code.emit("M=D")
    code.emit("@SP")
    code.emit("M=M+1")

    code.emit("@LCL")
    code.emit("D=M")
    code.emit("@SP")
    code.emit("A=M")
    code.emit("M=D")
    code.emit("@SP")
    code.emit("M=M+1")

    code.emit("@ARG")
    code.emit("D=M")
    code.emit("@SP")
    code.emit("A=M")
    code.emit("M=D")
    code.emit("@SP")
    code.emit("M=M+1")

    code.emit("@THIS")
    code.emit("D=M")
    code.emit("@SP")
    code.emit("A=M")
    code.emit("M=D")
    code.emit("@SP")
    code.emit("M=M+1")

    code.emit("@THAT")
    code.emit("D=M")
    code.emit("@SP")
    code.emit("A=M")
    code.emit("M=D")
    code.emit("@SP")
    code.emit("M=M+1")

    code.emit("@SP")
    code.emit("D=M")
    code.emit("@5")
    code.emit("D=D-A")
    code.emit("@" + str(nargs) + "")
    code.emit("D=D-A")
    code.emit("@ARG")
    code.emit("M=D")

    code.emit("@SP")
    code.emit("D=M")
    code.emit("@LCL")
    code.emit("M=D")

    code.emit("@" + memorysegment + "")
    code.emit("0;JMP")

    code.emit("(retAddrLabel" + str(counter) + ")")

def op_function(args, code):
    memorysegment = args[0]
    nargs=int(args[1])
    code.emit("(" + memorysegment + ")")
    while nargs>0:
        code.emit("@SP")
        code.emit("A=M")
        code.emit("M=0")
        code.emit("@SP")
        code.emit("M=M+1")
        nargs=nargs-1

def op_return(args, code):

    code.emit("@LCL")
    code.emit("D=M")
    code.emit("@ENDFRAME")
    code.emit("M=D")
    code.emit("@5")
    code.emit("D=D-A")
    code.emit("A=D")
    code.emit("D=M")
    code.emit("@RETADDR")
    code.emit("M=D")

    code.emit("@SP")
    code.emit("A=M-1")
    code.emit("D=M")
    code.emit("@SP")
    code.emit("M=M-1")
    code.emit("@ARG")
    code.emit("A=M")
    code.emit("M=D")
    code.emit("A=A+1")
    code.emit("D=A")
    code.emit("@SP")
    code.emit("M=D")

    code.emit("@ENDFRAME")
    code.emit("D=M")
    code.emit("D=D-1")
    code.emit("A=D")
    code.emit("D=M")
    code.emit("@THAT")
    code.emit("M=D")

    code.emit("@ENDFRAME")
    code.emit("D=M")
    code.emit("D=D-1")
    code.emit("D=D-1")
    code.emit("A=D")
    code.emit("D=M")
    code.emit("@THIS")
    code.emit("M=D")

    code.emit("@ENDFRAME")
    code.emit("D=M")
    code.emit("D=D-1")
    code.emit("D=D-1")
    code.emit("D=D-1")
    code.emit("A=D")
    code.emit("D=M")
    code.emit("@ARG")
    code.emit("M=D")

    code.emit("@ENDFRAME")
    code.emit("D=M")
    code.emit("D=D-1")
    code.emit("D=D-1")
    code.emit("D=D-1")
    code.emit("D=D-1")
    code.emit("A=D")
    code.emit("D=M")
    code.emit("@LCL")
    code.emit("M=D")

    code.emit("@RETADDR")
    code.emit("A=M")
    code.emit("0;JMP")


def assembler(ifn: str, code):
    print(ifn)
    print("Translating", ifn, "into", code.ofn)

    ifd = open(ifn, "r")
    counter = 1

    for line in ifd.readlines():  # iterate each line of the input file
        line = line.strip()
        if line[:2] == "//":      # skip comment lines
            continue
        words = line.split()      # split line into words

        if len(words) == 0:       # skip empty lines
            continue

        # process an actual vm instruction
        op = words[0]             # first word is operation
        args = words[1:]

        match op:
            case 'push':
                op_push(args, code)
            case 'add':
                op_add(code)
            case 'pop':
                op_pop(args, code)
            case 'sub':
                op_sub(code)
            case 'eq':
                op_eq(code, counter)
                counter += 1
            case 'lt':
                op_lt(code, counter)
                counter += 1
            case 'gt':
                op_gt(code, counter)
                counter += 1
            case 'neg':
                op_neg(code)
            case 'and':
                op_and(code)
            case 'or':
                op_or(code)
            case 'not':
                op_not(code)
            case 'label':
                op_label(args, code)
            case 'goto':
                op_goto(args, code)
            case 'if-goto':
                op_if_goto(args, code)
            case 'call':
                op_call(args, code, counter)
                counter += 1
            case 'function':
                op_function(args, code)
            case 'return':
                op_return(args, code)
            # TODO : Add more operations
            case _:
                raise Exception("Unexpected operation " + op)

    ifd.close()

def bootstrapcode(code):
    # TODO make bootstrap code
    code.emit("@256")
    code.emit("D=A")
    code.emit("@SP")
    code.emit("M=D")
    op_call(["Sys.init", "0"], code, 0)
    pass


def process_directory(input_directory):
    # output file name
    output_filname = input_directory + os.sep + input_directory.split(os.sep)[-1] + ".asm"
    print("Input directory:", input_directory)
    print("Output assembler file:", output_filname)

    # new code generator object
    code = Code(output_filname)
    # bootstrap code
    for filename in glob.glob(input_directory + os.sep + "*.vm"):
        basename = filename.split(os.sep)[-1]
        if basename.lower() == "sys.vm":
            # we generate the bootstrap code if
            # there is a file named sys.vm in the directory
            bootstrapcode(code)
            break

    # process all .vm files in directory
    for input_filename in glob.glob(input_directory + os.sep + "*.vm"):
        print("Generating asm code from " + input_filename, "to", output_filname)
        code.set_input_file(input_filename)
        assembler(input_filename, code)


if __name__ == "__main__":
    # input directory is passed as the first argument in the command line
    input_directory = sys.argv[1]
    process_directory(input_directory)
