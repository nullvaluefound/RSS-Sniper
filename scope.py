import json
import os
import feedparser
import traceback
try:
    if os.name == 'nt':
        separator = '\\'
    elif os.name == 'posix':
        separator = '/'
    else:
        raise ValueError("Unsupported operating system")

    with open(f".{separator}config{separator}vendors.json", 'r') as vendors_file:
        global vendors_data
        vendors_data = json.load(vendors_file)
        vendors_file.close()

    with open(f".{separator}config{separator}keywords.json", 'r') as keywords_file:
        global keywords_data
        keywords_data = json.load(keywords_file)
        keywords_file.close()
    
    with open(f".{separator}config{separator}rss_feeds.json", 'r') as rss_feeds_file:
        global rss_feeds_data
        rss_feeds_data = json.load(rss_feeds_file)
        rss_feeds_file.close()

except Exception as e:
    print(f"Error loading scope file: {e}")
    print(traceback.format_exc())
    exit(1)    

from scope_utils import ScopeUtils

class Scope:
    def __init__(self):
        self.utils = ScopeUtils()
    
    def snipeNews(self):
        articles = self.utils.aimDownRSSNews()
        output = f""""""
        counter = 0
        for category, articles in articles.items():
            num_articles = len(articles)
            
            output += f"\nCategory: {category} - ({num_articles} articles)\n"
            for article in articles:
                if counter != num_articles:
                    counter += 1 
                output += f"------------------ Article #{counter} ----------------------\n"
                output += f"RSS Name:\t {article.rss_name}\n"
                output += f"Published:\t {article.published}\n"
                output += f"Title:\t\t {article.title}\n"
                output += f"Link:\t\t {article.link}\n"
                output += f"Summary:\n\n {article.summary}\n"
                output += "-----------------------------------------------------\n\n"
                
        return output