class JackTokenizer:

    def __init__(self, input_file):
        with open(input_file, 'r') as f:
            self.lines = f.readlines()
        self.current_line_index = 0
        self.current_line = None
        self.token = None
        self.type = None



    def has_more_lines(self):
        return self.current_line_index < len(self.lines)

    def next_line(self):
        if self.has_more_lines():
            self.current_line = self.lines[self.current_line_index]
            self.current_line_index += 1

