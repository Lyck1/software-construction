# Implement your project 7 here
import sys

class Code:
    def __init__(self, fn):
        self.fn = fn
        if fn[-4]==".":
            self.base_fn = fn[:-4]
        else:
            self.base_fn = fn

        self.labels={}
        self.ofd = open(fn, "w")

    def new_label(self, label):
        if label in self.labels:
            self.labels[label]=self.labels[label]+1
        else:
            self.labels[label]=1
    def replace_labels(self, s):
        for label in self.labels:
            s=s.replace("<"+label+">",label+str(self.labels[label]))
        s=s.replace("<FILENAME",self.base_fn)
        return s

    def emit(self,s):
        s=self.replace_labels(s)
        self.ofd.write(s)
        self.ofd.write("\n")

    def emit_comment(self,comment):
        comment=self.replace_labels(comment)
        self.ofd.write("//")
        self.ofd.write(comment)
        if comment[-1]!="\n":
            self.ofd.write("\n")

    def close(self):
        self.ofd.close()
def op_push(args, ofd):
    memorysegment=args[0]
    value=int(args[1])

    match memorysegment:
        case "constant":
            ofd.write("@"+str(value)+"\n")
            ofd.write("D=A\n")
            ofd.write("@SP\n")
            ofd.write("A=M\n")
            ofd.write("M=D\n")
            ofd.write("@SP\n")
            ofd.write("M=M+1\n")
        case "local":
            ofd.write("@LCL\n")
            ofd.write("A=M\n")
            while value>0:
                value=value-1
                ofd.write("A=A+1\n")
            ofd.write("D=M\n")
            ofd.write("@SP\n")
            ofd.write("A=M\n")
            ofd.write("M=D\n")
            ofd.write("@SP\n")
            ofd.write("M=M+1\n")
        case "argument":
            ofd.write("@ARG\n")
            ofd.write("A=M\n")
            while value > 0:
                value = value - 1
                ofd.write("A=A+1\n")
            ofd.write("D=M\n")
            ofd.write("@SP\n")
            ofd.write("A=M\n")
            ofd.write("M=D\n")
            ofd.write("@SP\n")
            ofd.write("M=M+1\n")
        case "this":
            ofd.write("@THIS\n")
            ofd.write("A=M\n")
            while value > 0:
                value = value - 1
                ofd.write("A=A+1\n")
            ofd.write("D=M\n")
            ofd.write("@SP\n")
            ofd.write("A=M\n")
            ofd.write("M=D\n")
            ofd.write("@SP\n")
            ofd.write("M=M+1\n")
        case "that":
            ofd.write("@THAT\n")
            ofd.write("A=M\n")
            while value > 0:
                value = value - 1
                ofd.write("A=A+1\n")
            ofd.write("D=M\n")
            ofd.write("@SP\n")
            ofd.write("A=M\n")
            ofd.write("M=D\n")
            ofd.write("@SP\n")
            ofd.write("M=M+1\n")
        case "temp":
            ofd.write("@5\n")
            while value > 0:
                value = value - 1
                ofd.write("A=A+1\n")
            ofd.write("D=M\n")
            ofd.write("@SP\n")
            ofd.write("A=M\n")
            ofd.write("M=D\n")
            ofd.write("@SP\n")
            ofd.write("M=M+1\n")
        case "pointer":
            if value==0:
                ofd.write("@THIS\n")
                ofd.write("D=M\n")
                ofd.write("@SP\n")
                ofd.write("A=M\n")
                ofd.write("M=D\n")
                ofd.write("@SP\n")
                ofd.write("M=M+1\n")
            else:
                ofd.write("@THAT\n")
                ofd.write("D=M\n")
                ofd.write("@SP\n")
                ofd.write("A=M\n")
                ofd.write("M=D\n")
                ofd.write("@SP\n")
                ofd.write("M=M+1\n")
        case "static":
            ofd.write("@16\n")
            while value > 0:
                value = value - 1
                ofd.write("A=A+1\n")
            ofd.write("D=M\n")
            ofd.write("@SP\n")
            ofd.write("A=M\n")
            ofd.write("M=D\n")
            ofd.write("@SP\n")
            ofd.write("M=M+1\n")
        case "_":
            raise Exception("Unknown memory segment"+memorysegment)

def op_pop(args, ofd):
    memorysegment=args[0]
    value=int(args[1])

    match memorysegment:
        case "local":
            ofd.write("@SP\n")
            ofd.write("A=M\n")
            ofd.write("A=A-1\n")
            ofd.write("D=M\n")
            ofd.write("@SP\n")
            ofd.write("M=M-1\n")
            ofd.write("@LCL\n")
            ofd.write("A=M\n")
            while value>0:
                value=value-1
                ofd.write("A=A+1\n")
            ofd.write("M=D\n")
        case "argument":
            ofd.write("@SP\n")
            ofd.write("A=M\n")
            ofd.write("A=A-1\n")
            ofd.write("D=M\n")
            ofd.write("@SP\n")
            ofd.write("M=M-1\n")
            ofd.write("@ARG\n")
            ofd.write("A=M\n")
            while value > 0:
                value = value - 1
                ofd.write("A=A+1\n")
            ofd.write("M=D\n")
        case "this":
            ofd.write("@SP\n")
            ofd.write("A=M\n")
            ofd.write("A=A-1\n")
            ofd.write("D=M\n")
            ofd.write("@SP\n")
            ofd.write("M=M-1\n")
            ofd.write("@THIS\n")
            ofd.write("A=M\n")
            while value > 0:
                value = value - 1
                ofd.write("A=A+1\n")
            ofd.write("M=D\n")
        case "that":
            ofd.write("@SP\n")
            ofd.write("A=M\n")
            ofd.write("A=A-1\n")
            ofd.write("D=M\n")
            ofd.write("@SP\n")
            ofd.write("M=M-1\n")
            ofd.write("@THAT\n")
            ofd.write("A=M\n")
            while value > 0:
                value = value - 1
                ofd.write("A=A+1\n")
            ofd.write("M=D\n")
        case "temp":
            ofd.write("@SP\n")
            ofd.write("A=M-1\n")
            ofd.write("D=M\n")
            ofd.write("@5\n")
            while value > 0:
                value = value - 1
                ofd.write("A=A+1\n")
            ofd.write("M=D\n")
            ofd.write("@SP\n")
            ofd.write("M=M-1\n")
        case "pointer":
            if value==0:
                ofd.write("@SP\n")
                ofd.write("A=M-1\n")
                ofd.write("D=M\n")
                ofd.write("@SP\n")
                ofd.write("M=M-1\n")
                ofd.write("@THIS\n")
                ofd.write("M=D\n")
            else:
                ofd.write("@SP\n")
                ofd.write("A=M-1\n")
                ofd.write("D=M\n")
                ofd.write("@SP\n")
                ofd.write("M=M-1\n")
                ofd.write("@THAT\n")
                ofd.write("M=D\n")
        case "static":
            ofd.write("@SP\n")
            ofd.write("A=M-1\n")
            ofd.write("D=M\n")
            ofd.write("@SP\n")
            ofd.write("M=M-1\n")
            ofd.write("@16\n")
            while value > 0:
                value = value - 1
                ofd.write("A=A+1\n")
            ofd.write("M=D\n")
        case "_":
            raise Exception("Unknown memory segment"+memorysegment)
def op_add(ofd):
    ofd.write("@SP\n")
    ofd.write("A=M-1\n")
    ofd.write("D=M\n")
    ofd.write("@SP\n")
    ofd.write("M=M-1\n")
    ofd.write("A=M\n")
    ofd.write("A=A-1\n")
    ofd.write("D=D+M\n")
    ofd.write("M=D\n")
    pass
def op_sub(ofd):
    ofd.write("@SP\n")
    ofd.write("A=M-1\n")
    ofd.write("A=A-1\n")
    ofd.write("D=M\n")
    ofd.write("A=A+1\n")
    ofd.write("D=D-M\n")
    ofd.write("A=A-1\n")
    ofd.write("M=D\n")
    ofd.write("@SP\n")
    ofd.write("M=M-1\n")
    pass

def op_eq(ofd, counter):
    ofd.write("@SP\n")
    ofd.write("A=M-1\n")
    ofd.write("D=M\n")
    ofd.write("A=A-1\n")
    ofd.write("D=D-M\n")

    ofd.write("@EQ_TRUE" + str(counter) + "\n")
    ofd.write("D;JEQ\n")

    ofd.write("@SP\n")
    ofd.write("A=M-1\n")
    ofd.write("A=A-1\n")
    ofd.write("M=0\n")

    ofd.write("@END" + str(counter) + "\n")
    ofd.write("0;JMP\n")

    ofd.write("(EQ_TRUE" + str(counter) + ")\n")
    ofd.write("@SP\n")
    ofd.write("A=M-1\n")
    ofd.write("A=A-1\n")
    ofd.write("M=-1\n")

    ofd.write("(END" + str(counter) + ")\n")
    ofd.write("@SP\n")
    ofd.write("M=M-1\n")

def op_lt(ofd, counter):
    ofd.write("@SP\n")
    ofd.write("A=M-1\n")
    ofd.write("D=M\n")
    ofd.write("A=A-1\n")
    ofd.write("D=M-D\n")

    ofd.write("@LT_TRUE" + str(counter) + "\n")
    ofd.write("D;JLT\n")

    ofd.write("@SP\n")
    ofd.write("A=M-1\n")
    ofd.write("A=A-1\n")
    ofd.write("M=0\n")

    ofd.write("@END" + str(counter) + "\n")
    ofd.write("0;JMP\n")

    ofd.write("(LT_TRUE" + str(counter) + ")\n")
    ofd.write("@SP\n")
    ofd.write("A=M-1\n")
    ofd.write("A=A-1\n")
    ofd.write("M=-1\n")

    ofd.write("(END" + str(counter) + ")\n")
    ofd.write("@SP\n")
    ofd.write("M=M-1\n")
    pass

def op_gt(ofd, counter):
    ofd.write("@SP\n")
    ofd.write("A=M-1\n")
    ofd.write("D=M\n")
    ofd.write("A=A-1\n")
    ofd.write("D=M-D\n")

    ofd.write("@GT_TRUE" + str(counter) + "\n")
    ofd.write("D;JGT\n")

    ofd.write("@SP\n")
    ofd.write("A=M-1\n")
    ofd.write("A=A-1\n")
    ofd.write("M=0\n")

    ofd.write("@END" + str(counter) + "\n")
    ofd.write("0;JMP\n")

    ofd.write("(GT_TRUE" + str(counter) + ")\n")
    ofd.write("@SP\n")
    ofd.write("A=M-1\n")
    ofd.write("A=A-1\n")
    ofd.write("M=-1\n")

    ofd.write("(END" + str(counter) + ")\n")
    ofd.write("@SP\n")
    ofd.write("M=M-1\n")
    pass

def op_neg(ofd):
    ofd.write("@SP\n")
    ofd.write("A=M\n")
    ofd.write("M=0\n")
    ofd.write("A=A-1\n")
    ofd.write("D=M\n")
    ofd.write("A=A+1\n")
    ofd.write("D=M-D\n")
    ofd.write("A=A-1\n")
    ofd.write("M=D\n")

def op_and(ofd):
    ofd.write("@SP\n")
    ofd.write("A=M-1\n")
    ofd.write("D=M\n")
    ofd.write("A=A-1\n")
    ofd.write("M=D&M\n")
    ofd.write("@SP\n")
    ofd.write("M=M-1\n")

def op_or(ofd):
    ofd.write("@SP\n")
    ofd.write("A=M-1\n")
    ofd.write("D=M\n")
    ofd.write("A=A-1\n")
    ofd.write("M=D|M\n")
    ofd.write("@SP\n")
    ofd.write("M=M-1\n")

def op_not(ofd):
    ofd.write("@SP\n")
    ofd.write("A=M-1\n")
    ofd.write("M=!M\n")

def main(ifn: str):

    ofn = ifn[:-3] + ".asm"
    print("Translating", ifn, "into", ofn)

    ifd = open(ifn, "r")
    ofd = open(ofn, "w")
    counter = 0

    for line in ifd.readlines():  # iterate each line of the input file
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
                op_push(args, ofd)
            case 'add':
                op_add(ofd)
            case 'pop':
                op_pop(args, ofd)
            case 'sub':
                op_sub(ofd)
            case 'eq':
                op_eq(ofd, counter)
                counter += 1
            case 'lt':
                op_lt(ofd, counter)
                counter += 1
            case 'gt':
                op_gt(ofd, counter)
                counter += 1
            case 'neg':
                op_neg(ofd)
            case 'and':
                op_and(ofd)
            case 'or':
                op_or(ofd)
            case 'not':
                op_not(ofd)
            # TODO : Add more operations
            case _:
                raise Exception("Unexpected operation " + op)

    ifd.close()
    ofd.close()

if __name__ == "__main__":
        print("Command line arguments:", sys.argv)
        main(sys.argv[1])
