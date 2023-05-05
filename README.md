# Scrapetron
Scrapetron is a Python package for web scraping that provides a simple and intuitive API for extracting data from websites. With Scrapetron, you can easily scrape web pages and extract information such as text, images, links, and more.

## Installation
You can install Scrapetron using pip:

```
pip install scrapetron
```

## Usage
Here's a simple example of how to use Scrapetron to scrape a web page:

```
from scrapetron import Scrapetron
url = 'https://www.example.com'
scraper = Scrapetron(url)
data = scraper.get_text()
print(data)
```
In this example, we create a new Scrapetron object with the URL of the web page we want to scrape. We then call the get_text method to extract the text content of the page.

## Features
Scrapetron provides a number of features for web scraping, including:

- Retrieving text, HTML, and JSON data from web pages
- Parsing HTML using Beautiful Soup
- Extracting data using CSS selectors or XPath expressions
- Following links and scraping multiple pages
- Handling errors and retries

For more information on how to use Scrapetron, please see the documentation.

## Contributing
If you'd like to contribute to Scrapetron, please fork the repository and submit a pull request. We welcome contributions of all kinds, including bug fixes, new features, and documentation improvements.

## License
Scrapetron is licensed under the MIT license. See the LICENSE file for more information.