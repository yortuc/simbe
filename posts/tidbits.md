@template: post.html

# Tidbits

> *Tidbit*: a small piece of interesting information, or a small dish of pleasant-tasting food. (Cambridge dictionary)

### Array in udf

How to apply an udf on a column which contains an array<string> type: use Seq[String]

Dataframe looks like this:

<pre>
	root
	 |-- id: long (nullable = false)
	 |-- items: array (nullable = true)
	 |    |-- element: string (containsNull = true)
</pre>

udf:
<pre>
	val countItems = udf((history: Seq[String]) => history.size)
	df.withColumn("items_count", countItems($"history"))	
</pre>







