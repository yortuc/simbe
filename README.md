# Simbe
> Simplest Blog Engine

Static site generators are rocket science today. So many complicated features that I do not need. So, I came up with the simplest static blog generator so far, with limited features of course. 

## Start using
```
git clone https://github.com/yortuc/simbe.git
cd simbe
python compile.py 
```

## Add content
A post is a `.md` file in posts folder. Additinally, you can specify variables starting with `@` and use it in template. Some variables are mandatory like title, date and template. 

Example:
```
@template: post.html
@title: DataLake Paths Structure
@date: 22-04-2020

# DataLake Paths Best Practices

Solving a problem within *24 hours of it appearing* here will reward you with LeetCoins. Completing all 30 on the ...
```

## Add new template
Tempates are just html files. You can import other html files or variables from content file. 

Example:
```
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en-us" lang="en-us">
<%html_head%>
<body>
	<%page_header%>

	<div class="post">
		<%content%>
	</div>
</body>
</html>
```

In this example, `page_header` is another template. And `content` is a variable generated with the content of the post file. 


### Roadmap
- define template in content with variable [done]
- modularize code, write unit tests [done]
- support for nested templates
- add disquss and GA
- Syntax highlighting for code fragments
														