import random
import sys

def line_sep(sep):
    a = ''
    for i in range(80):
        a = a + ''.join(sep)
    return a

def main():
#    quote_file = sys.argv[1]
    quote_file = '/home/anand/workspace/my_projects/Miscellaneous/Quotes.txt'
    signature_file = '/home/anand/.signature'
    signature_fd = open(signature_file,'w')
    
    quote_fd = open(quote_file)
    quote_lines = quote_fd.read()
    quote_fd.close()
    quotes = quote_lines.split("~Aang Jie")
    quote_count = random.choice(range(len(quotes)))

    signature = "Thanks and Regards\n" + "Anand Jeyahar\n"

    sep = '='
    signature = signature + line_sep(sep)   
    signature = signature + quotes[quote_count] + "\n\t\t\t\t" + "~Aang Jie\n"
    signature_fd.write(signature)
    signature_fd.close()
    print signature
if __name__ == '__main__':
    main()
