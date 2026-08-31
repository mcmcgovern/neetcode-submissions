class TextProcessor:
    # Implement method overloading for format_text method
    def format_text(self, text1, text2='') -> str:
        return text1.upper() if not text2 else text1+text2



# Don't modify the code below
processor = TextProcessor()
print(processor.format_text("hello"))
print(processor.format_text("hello", "world"))
