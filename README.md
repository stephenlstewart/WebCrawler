# WebCrawler
This package turns Nuix into a Web Crawler.  It leverages a 3rd party Web Crawler - [Ache](https://ache.readthedocs.io/en/latest/) - that can dump the crawled pages out to a Kafka topic.  Nuix the subscribes to teh Kafka topic using the Nuix RealTime capability.  The WSS.Web.Scraper.py WSS pull the HTML page out of a metadata field and converts it into a child item.

It is pretty cool and highlights the ease to which you can build new use cases with  Nuix and Kafka.

## Docker Image - Web Crawler
https://github.com/VIDA-NYU/ache
```
docker run -p 8080:8080 vidanyu/ache:latest
```


##Kakfa Setting for Nuix
```
Zookeeper - 127.0.0.1:2181
Bootstrap.servers - 127.0.0.1:9092
```
