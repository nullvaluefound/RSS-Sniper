from sys import exit, argv
import traceback
import argparse
from scope import Scope

def argumentParser():
    parser = argparse.ArgumentParser(description='RSS Sniper')
    parser.add_argument('-v', '--vendors', action='store_true', help='Snipe Vendors')
    parser.add_argument('-n', '--news', action='store_true', help='Snipe News')
    parser.add_argument('-p', '--products', action='store_true', help='Snipe Products')
    parser.add_argument('-c', '--cves', action='store_true', help='Snipe CVEs')

    if len(argv) == 1:
        parser.print_help()
        exit(1)
    else:
        return parser.parse_args()

def main():
    args = argumentParser()
    scope = Scope()

    if args.news:
        
        news = scope.snipeNews()
        with open("news.txt", "w") as f:
            f.writelines(news)
            
    # elif args.products:
    #     print(scope.snipeProducts())
    # elif args.vendors:
    #     print(scope.snipeVendors())
    # elif args.cves:
    #     print(scope.snipeCVEs())
    else:
        print("Generic Failure")
        print(traceback.format_exc())
    exit(0)

if __name__ == "__main__":
    main()