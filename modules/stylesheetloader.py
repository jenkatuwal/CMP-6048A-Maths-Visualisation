class StyleSheetLoader:
    
    def __init__(self):
        self.filename = ""
    
    def __repr__(self):
        return str(self.file_content)
    
    def load(self, **kwargs):
        self.filename = kwargs["filename"]
        self.filename = f"GUI/stylesheets/{self.filename}"
        with open(self.filename, "r") as f:
            self.file_content = f.read()
            return self.file_content

