
def process(self):
    self.edit("SMALL")
    self.edit("IDEOGRAPHIC", "ideographic")
    self.processAs("Basic Latin")
    self.processAs("General Punctuation")

if __name__ == "__main__":
    from glyphNameFormatter.test import printRange
    printRange("Small Form Variants")
