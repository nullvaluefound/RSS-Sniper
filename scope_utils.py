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


class ScopeUtils:
    def __init__(self):
        self.rss_feeds_data = rss_feeds_data
        self.keywords_data = keywords_data
        self.vendors_data = vendors_data

    # Completed
    def aimDownRSSNews(self):
        articles = {}
        for rss_name, rss_url in self.rss_feeds_data["Journalists"].items():
            feed = feedparser.parse(rss_url)
            for entry in feed.entries:
                for category,keywords in self.keywords_data.items():
                    entry["rss_name"] = rss_name
                    for keyword in keywords:
                        if keyword.lower() in entry.title.lower():
                            if category not in articles.keys():
                                entry["rss_name"] = rss_name
                                articles[category] = [entry]
                            else:
                                entry["rss_name"] = rss_name
                                articles.get(category).append(entry)
        return articles

    # Under Construction - Not Working
    def aimDownRSSVendors(self):
        articles = {}
        for rss_name, rss_url in self.rss_feeds_data["Vendors"].items():
            feed = feedparser.parse(rss_url)
            for entry in feed.entries:
                for category,keyword in self.keywords_data.items():
                    entry["rss_name"] = rss_name
                    if entry.title.lower() in keyword.lower():
                        if category not in articles:
                            entry["rss_name"] = rss_name
                            articles[category] = [entry]
                        else:
                            entry["rss_name"] = rss_name
                            articles.get(category).append(entry)
        return articles

    # Under Construction - Not Working
    def aimDownRSSCVEs(self):
        articles = {}
        # for rss_name, rss_url in self.rss_feeds_data["cve_rss_feeds"].items():
        #     feed = feedparser.parse(rss_url)
        #     for entry in feed.entries:
        #         for category,keyword in self.keywords_data.items():
        #             entry["rss_name"] = rss_name
        #             if entry.title.lower() in keyword.lower():
        #                 if category not in articles:
        #                     entry["rss_name"] = rss_name
        #                     articles[category] = [entry]
        #                 else:
        #                     entry["rss_name"] = rss_name
        #                     articles.get(category).append(entry)
        return articles