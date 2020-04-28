# Simbe
Simplest Blog Engine


### Roadmap
- Syntax highlighting for code fragments
- define template in content with variable
- tags
   read all tags when reading all posts
   create folders for each tag
   produce output for each content to each tag
   - /output/spark-datasets.html         [tag: empty]
   - /output/big-data/spark-datsets.html [tag: big-data]
   - /output/spark/spark-datasets.html   [tag: spark]
- modularize code, write unit tests




(read-contents) -> (extract tags)
                -> (extract post links)
				-> (render all content files with given template to string) -> (save output to root)
				                                                            -> (save output to tags)
																			
																			