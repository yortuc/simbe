# Simbe
Simplest Blog Engine


### Roadmap
- define template in content with variable [done]
- modularize code, write unit tests [done]
- add disquss and GA
- Syntax highlighting for code fragments
- tags
   read all tags when reading all posts
   create folders for each tag
   produce output for each content to each tag
   - /output/spark-datasets.html         [tag: empty]
   - /output/big-data/spark-datsets.html [tag: big-data]
   - /output/spark/spark-datasets.html   [tag: spark]



### Work Flow

```
(read-contents) -> (extract tags)
                -> (extract post links)
				-> (render all content files with given template to string) -> (save output to root)
				                                                            -> (save output to tags)
```																		
																			