class JackTokenizer:

    def __init__(self, input_file):
        with open(input_file, 'r') as f:
            self.lines = f.readlines()
        self.current_line_index = 0
        self.current_line = None
        self.tokenType = None
        self.token = None
        self.peek_next = None
        self.peek_tokenType = None
        self.peek_token = None




    def has_more_lines(self):
        return self.current_line_index < len(self.lines)

    def next_line(self):
        if self.has_more_lines():
            self.current_line = self.lines[self.current_line_index]
            self.tokenType = self.current_line.split("<")[1].split(">")[0]
            self.token = self.current_line.split(">")[1].split("<")[0].strip()
            self.current_line_index += 1

    def get_token(self):
        return self.token

    def get_token_type(self):
        return self.tokenType
    def get_current_line(self):
        return self.current_line

    def peek_next_line(self):
        if self.has_more_lines():
            self.peek_next = self.lines[self.current_line_index+1]
            self.tokenType = self.peek_next.split("<")[1].split(">")[0]
            self.token = self.peek_next.split(">")[1].split("<")[0].strip()

    def get_peek_token(self):
        return self.peek_token

    def get_peek_token_type(self):
        return self.peek_tokenType

    def get_peek_next(self):
        return self.peek_next
