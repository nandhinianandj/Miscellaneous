import random
import sys
import os

def main():
    quote_file = os.path.join(os.getenv("HOME") , 'my_writings/wordpress_blog_posts/aangjie/quotes.md')
    quote_file = sys.argv[1]  if len(sys.argv) > 1 else quote_file
    quote_fd = open(quote_file)
    quote_lines = quote_fd.read()
    quotes = quote_lines.split("~Aang Jie")
    quote_count = random.choice(range(len(quotes)))
    print(quotes[quote_count])

if __name__ == '__main__':
    main()
