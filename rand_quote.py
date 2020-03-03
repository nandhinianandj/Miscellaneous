import random
import sys



def main():
    quote_file = sys.argv[1]
    #quote_file = '/home/nandhini/my_writings/wordpress_blog_posts/aangjie/quotes.md'
    quote_fd = open(quote_file)
    quote_lines = quote_fd.read()
    quotes = quote_lines.split("~Aang Jie")
    quote_count = random.choice(range(len(quotes)))
    print quotes[quote_count]

if __name__ == '__main__':
    main()
