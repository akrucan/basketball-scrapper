## Spiders

This project contains a spiders and you can list it using the `list`
command:

    $ scrapy list
    toscrape


## Running the spiders

You can run a spider using the `scrapy crawl` command, such as:

    $ scrapy crawl toscrape

If you want to save the scraped data to a file, you can pass the `-o` option:
    
    $ scrapy crawl toscrape -o tables.json
