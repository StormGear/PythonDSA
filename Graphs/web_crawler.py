import re
import requests

class WebCrawler:
    def __init__(self):
        self.visited_sites = []

    # crawl the web using breadth first search
    def crawl(self, start_url):
        queue = [start_url]
        self.visited_sites.append(start_url)

        while queue:
            actual_url = queue.pop(0)
            print(actual_url)

            # get all the links from the actual_url
            links = self.get_links(actual_url)

            for link in links:
                if link not in self.visited_sites:
                    self.visited_sites.append(link)
                    queue.append(link)

    def get_links(self, url):
        html_text = self.read_raw_html(url)
        return re.findall(r"https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+", html_text)
        
    def read_raw_html(self, url):
        try:
            raw_html = requests.get(url)
        except Exception as e:
            pass
        
        return raw_html.text
    
if __name__ == "__main__":
    crawler = WebCrawler()
    crawler.crawl("https://www.google.com")
    print(crawler.visited_sites)