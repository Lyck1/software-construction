from JackTokenizer import JackTokenizer

class CompilationEngine:
    def __init__(self, input_file, output_file):

        self.tokenizer = JackTokenizer(input_file)
        self.output = open(output_file, "w")


    def compileClass(self):
        if self.tokenizer.has_more_lines():
            self.tokenizer.next_line()
            self.output.write("<class>\n")

    def compileWhile(self):
        self.output.write("<whileStatements>\n")
        self.output.write(self.tokenizer.current_line + "\n") # while
        self.tokenizer.next_line()
        self.output.write(self.tokenizer.current_line + "\n") # (
        self.tokenizer.next_line()
        self.compileExpression()
        self.output.write(self.tokenizer.current_line + "\n") # )
        self.tokenizer.next_line()
        self.output.write(self.tokenizer.current_line + "\n") # {
        self.tokenizer.next_line()
        self.compileStatements()
        self.output.write(self.tokenizer.current_line + "\n") # }
        self.tokenizer.next_line()
        self.output.write("</whileStatements>\n")
        self.tokenizer.next_line()

    def compileExpression(self):
        self.output.write("<expression>\n")
        self.tokenizer.next_line()
        self.compileTerm()
        if self.tokenizer.next_line() in "+-=<>":
            self.output.write(self.tokenizer.current_line +"\n") #TODO: might not work
            self.compileTerm()
        self.output.write("</expression>\n")

    statementKeywords = ['let', 'if', 'while', 'do', 'return']

    #TODO needs polishing
    def compileStatements(self):
        self.output.write("<statements>\n")
        self.tokenizer.next_line()

