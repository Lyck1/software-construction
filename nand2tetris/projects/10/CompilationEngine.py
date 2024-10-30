from JackTokenizer import JackTokenizer

class CompilationEngine:
    def __init__(self, input_file, output_file):
        self.statementKeywords = ['let', 'if', 'while', 'do', 'return']
        self.varKeywords = ['field', 'static']
        self.functionKeywords = ['function', 'constructor', 'method']
        self.unary = ['~']
        self.operations = ['+', '-', '=', '|', '&lt;', '&gt;', '&amp;', '-']
        self.tokenizer = JackTokenizer(input_file)
        self.output = open(output_file, "w")


    def compileClass(self):
        if self.tokenizer.has_more_lines():
            self.tokenizer.next_line()
            self.tokenizer.next_line()
            self.output.write("<class>\n")
            self.output.write(self.tokenizer.get_current_line())
            self.tokenizer.next_line()
            self.output.write(self.tokenizer.get_current_line())
            self.tokenizer.next_line()
            self.output.write(self.tokenizer.get_current_line()) # {
            self.tokenizer.next_line()

            while self.tokenizer.get_token() in self.varKeywords:
                self.compileClassVarDec()

            while self.tokenizer.get_token() in self.functionKeywords:
                self.compilesubroutineDec()

            self.output.write(self.tokenizer.get_current_line()) # }

            self.output.write("</class>\n")
            self.output.close()

    def compileClassVarDec(self):
        self.output.write("<classVarDec>\n")
        while self.tokenizer.get_token() != ";":
            self.output.write(self.tokenizer.get_current_line())
            self.tokenizer.next_line()
        self.output.write(self.tokenizer.get_current_line())
        self.tokenizer.next_line()
        self.output.write("</classVarDec>\n")

    def compilesubroutineDec(self):
        self.output.write("<subroutineDec>\n")
        self.output.write(self.tokenizer.get_current_line())
        self.tokenizer.next_line()
        self.output.write(self.tokenizer.get_current_line())
        self.tokenizer.next_line()
        self.output.write(self.tokenizer.get_current_line())
        self.tokenizer.next_line()
        self.output.write(self.tokenizer.get_current_line()) # (
        self.tokenizer.next_line()
        self.compileParameterList()                             # parameters
        self.output.write(self.tokenizer.get_current_line()) # )
        self.tokenizer.next_line()
        self.compileSubroutineBody()                            # subbody writes {}
        self.output.write("</subroutineDec>\n")

    def compileSubroutineBody(self):
        self.output.write("<subroutineBody>\n")
        self.output.write(self.tokenizer.get_current_line()) # {
        self.tokenizer.next_line()

        if self.tokenizer.get_token() == "var":
            self.compileVarDec()
        self.compileStatements()

        self.output.write(self.tokenizer.get_current_line()) # }
        self.tokenizer.next_line()
        self.output.write("</subroutineBody>\n")

    def compileVarDec(self):
        self.output.write("<varDec>\n")
        while self.tokenizer.get_token() == "var":
            while self.tokenizer.get_token() != ";":
                self.output.write(self.tokenizer.get_current_line())
                self.tokenizer.next_line()
            self.output.write(self.tokenizer.get_current_line())
            self.tokenizer.next_line()
            if self.tokenizer.get_token() == "var":
                self.output.write("</varDec>\n")
                self.output.write("<varDec>\n")

        self.output.write("</varDec>\n")


    def compileParameterList(self):
        self.output.write("<parameterList>\n")
        while self.tokenizer.get_token() != ")":
            self.output.write(self.tokenizer.get_current_line())
            self.tokenizer.next_line()
        self.output.write("</parameterList>\n")

    def compileWhile(self):
        self.output.write("<whileStatement>\n")
        self.output.write(self.tokenizer.get_current_line()) # while
        self.tokenizer.next_line()
        self.output.write(self.tokenizer.get_current_line()) # (
        self.tokenizer.next_line()
        self.compileExpression()
        self.output.write(self.tokenizer.get_current_line()) # )
        self.tokenizer.next_line()
        self.output.write(self.tokenizer.get_current_line()) # {
        self.tokenizer.next_line()
        self.compileStatements()
        self.output.write(self.tokenizer.get_current_line()) # }
        self.tokenizer.next_line()
        self.output.write("</whileStatement>\n")

    def compileIf(self):
        self.output.write("<ifStatement>\n")
        self.output.write(self.tokenizer.get_current_line()) # if
        self.tokenizer.next_line()
        self.output.write(self.tokenizer.get_current_line()) # (
        self.tokenizer.next_line()
        self.compileExpression()
        self.output.write(self.tokenizer.get_current_line()) # )
        self.tokenizer.next_line()
        self.output.write(self.tokenizer.get_current_line()) # {
        self.tokenizer.next_line()
        self.compileStatements()
        self.output.write(self.tokenizer.get_current_line()) # }
        self.tokenizer.next_line()
        if self.tokenizer.get_token() == "else":
            self.output.write(self.tokenizer.get_current_line()) # else
            self.tokenizer.next_line()
            self.output.write(self.tokenizer.get_current_line()) # {
            self.tokenizer.next_line()
            self.compileStatements()
            self.output.write(self.tokenizer.get_current_line()) # }
            self.tokenizer.next_line()
        self.output.write("</ifStatement>\n")

    def compileDo(self):
        self.output.write("<doStatement>\n")
        self.output.write(self.tokenizer.get_current_line())
        self.tokenizer.next_line()
        self.output.write(self.tokenizer.get_current_line())
        self.tokenizer.next_line()

        if self.tokenizer.get_token() == ".":
            self.output.write(self.tokenizer.get_current_line())
            self.tokenizer.next_line()
            self.output.write(self.tokenizer.get_current_line())
            self.tokenizer.next_line()

        self.output.write(self.tokenizer.get_current_line()) # (
        self.tokenizer.next_line()
        self.compileExpressionList()
        self.output.write(self.tokenizer.get_current_line()) # )
        self.tokenizer.next_line()
        self.output.write(self.tokenizer.get_current_line()) # ;
        self.tokenizer.next_line()
        self.output.write("</doStatement>\n")

    def compileReturn(self):
        self.output.write("<returnStatement>\n")
        self.output.write(self.tokenizer.get_current_line())
        self.tokenizer.next_line()

        if self.tokenizer.get_token() != ";":
            self.compileExpression()

        self.output.write(self.tokenizer.get_current_line()) # ;
        self.tokenizer.next_line()
        self.output.write("</returnStatement>\n")

    def compileLet(self):
        self.output.write("<letStatement>\n")
        self.output.write(self.tokenizer.get_current_line()) # let
        self.tokenizer.next_line()
        self.output.write(self.tokenizer.get_current_line()) # name
        self.tokenizer.next_line()
        if self.tokenizer.get_token() == "[":
            self.output.write(self.tokenizer.get_current_line()) # [
            self.tokenizer.next_line()
            self.compileExpression()
            self.output.write(self.tokenizer.get_current_line())
            self.tokenizer.next_line()
        self.output.write(self.tokenizer.get_current_line()) # =
        self.tokenizer.next_line()
        self.compileExpression()
        self.output.write(self.tokenizer.get_current_line()) # ;
        self.tokenizer.next_line()
        self.output.write("</letStatement>\n")



    def compileExpressionList(self):
        self.output.write("<expressionList>\n")

        while self.tokenizer.get_token() != ")":
            self.compileExpression()
            if self.tokenizer.get_token() == ",":
                self.output.write(self.tokenizer.get_current_line())
                self.tokenizer.next_line()

        self.output.write("</expressionList>\n")

    def compileExpression(self):
        self.output.write("<expression>\n")
        self.compileTerm()
        if self.tokenizer.get_token() in self.operations:
            self.output.write(self.tokenizer.get_current_line())
            self.tokenizer.next_line()
            self.compileTerm()
        self.output.write("</expression>\n")

    def compileTerm(self):
        self.output.write("<term>\n")
        skipped = True
        self.output.write(self.tokenizer.get_current_line())
        if self.tokenizer.get_token() not in "([.~":
            self.tokenizer.next_line()
            skipped = False
        if self.tokenizer.get_token() == "[":
            if skipped:
                self.tokenizer.next_line()
            self.output.write(self.tokenizer.get_current_line())
            self.tokenizer.next_line()
            self.compileExpression()
            self.output.write(self.tokenizer.get_current_line())
            self.tokenizer.next_line()
        elif self.tokenizer.get_token() in self.unary:
            if skipped:
                self.tokenizer.next_line()
            self.compileTerm()
        elif self.tokenizer.get_token() in "(":
            if skipped:
                self.tokenizer.next_line()
            self.compileExpression()
            self.output.write(self.tokenizer.get_current_line())
            self.tokenizer.next_line()
        elif self.tokenizer.get_token() in ".":
            if skipped:
                self.tokenizer.next_line()
            self.output.write(self.tokenizer.get_current_line())
            self.tokenizer.next_line()
            self.output.write(self.tokenizer.get_current_line())
            self.tokenizer.next_line()
            self.output.write(self.tokenizer.get_current_line())
            self.tokenizer.next_line()
            self.compileExpressionList()
            self.output.write(self.tokenizer.get_current_line())
            self.tokenizer.next_line()
        self.output.write("</term>\n")

    def compileSmallTerm(self):
        self.output.write("<term>\n")
        self.output.write(self.tokenizer.get_current_line())
        self.tokenizer.next_line() # (
        self.output.write("<expression>\n")
        self.output.write("<term>\n")
        self.output.write(self.tokenizer.get_current_line()) # -
        self.tokenizer.next_line()
        self.output.write("<term>\n")
        self.output.write(self.tokenizer.get_current_line()) # j
        self.tokenizer.next_line()
        self.output.write("</term>\n")
        self.output.write("</term>\n")
        self.output.write("</expression>\n")
        self.output.write(self.tokenizer.get_current_line()) # )
        self.tokenizer.next_line()
        self.output.write("</term>\n")


    def compileStatements(self):
        self.output.write("<statements>\n")

        while self.tokenizer.get_token() in self.statementKeywords:
            token = self.tokenizer.get_token()
            match token:
                case 'let':
                    self.compileLet()
                case 'if':
                    self.compileIf()
                case 'while':
                    self.compileWhile()
                case 'do':
                    self.compileDo()
                case 'return':
                    self.compileReturn()
                case _:
                    break
        self.output.write("</statements>\n")
