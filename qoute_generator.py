import random
from datetime import datetime

class QuoteGenerator:
    def __init__(self):
        self.quotes = [
            ("Life is what happens while you're busy making other plans.", "John Lennon"),
            ("The way to get started is to quit talking and begin doing.", "Walt Disney"),
            ("The future belongs to those who believe in the beauty of their dreams.", "Eleanor Roosevelt"),
            ("Success is not final, failure is not fatal.", "Winston Churchill"),
            ("Write tests before writing code.", "Every Good Programmer")
        ]

    def get_random_quote(self):
        return random.choice(self.quotes)

    def add_quote(self, quote, author):
        self.quotes.append((quote, author))
        print(f"\nNew quote added successfully!")

    def display_quote(self):
        quote, author = self.get_random_quote()
        print("\n" + "="*50)
        print(f"Quote: {quote}")
        print(f"Author: {author}")
        print("="*50)
        print(f"Generated at: {datetime.now().strftime('%H:%M:%S')}\n")

def main_menu():
    generator = QuoteGenerator()
    
    while True:
        print("\n=== Quote Generator Menu ===")
        print("1. Show random quote")
        print("2. Add new quote")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ")
        
        if choice == "1":
            generator.display_quote()
        elif choice == "2":
            quote = input("Enter the quote: ")
            author = input("Enter the author: ")
            generator.add_quote(quote, author)
        elif choice == "3":
            print("\nThanks for using Quote Generator! Goodbye!")
            break
        else:
            print("\nInvalid choice! Please try again.")

if __name__ == "__main__":
    print("Welcome to Quote Generator!")
    main_menu()

