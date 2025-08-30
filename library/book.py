class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def get_description(self):
        return f"'{self.title}' by {self.author}, {self.pages} pages."

    def read(self, pages_read):
        if pages_read > self.pages:
            return "You can't read more pages than the book has!"
        return f"You read {pages_read} pages of '{self.title}'."

# EBook inherits from Book
class EBook(Book):
    def __init__(self, title, author, pages, file_size_mb, format_):
        super().__init__(title, author, pages)
        self.file_size_mb = file_size_mb
        self.format_ = format_

    def get_description(self):
        base_desc = super().get_description()
        return f"{base_desc} Format: {self.format_}, File size: {self.file_size_mb}MB."

    def download(self):
        return f"Downloading '{self.title}' ({self.file_size_mb}MB)..."

# PrintedBook inherits from Book
class PrintedBook(Book):
    def __init__(self, title, author, pages, weight_grams, cover_type):
        super().__init__(title, author, pages)
        self.weight_grams = weight_grams
        self.cover_type = cover_type

    def get_description(self):
        base_desc = super().get_description()
        return f"{base_desc} Cover: {self.cover_type}, Weight: {self.weight_grams}g."

    def carry(self):
        return f"You carry '{self.title}', it weighs {self.weight_grams} grams."

# Example usage:
ebook = EBook("computer essentials", "brian mwangi", 356, 10, "PDF")
print(ebook.get_description())
print(ebook.download())
print(ebook.read(50))

printed_book = PrintedBook("2000", "erick mwangi", 328, 400, "Hardcover")
print(printed_book.get_description())
print(printed_book.carry())
print(printed_book.read(100))
