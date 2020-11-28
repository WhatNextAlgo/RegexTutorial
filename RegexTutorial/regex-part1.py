# Databricks notebook source
import re

# COMMAND ----------

# MAGIC %md ###character Sets and Quantifier

# COMMAND ----------

# MAGIC %md **\w contain character `[a-zA-Z0-9_]` and \W contain opposite of \w **

# COMMAND ----------

re.search("\w+","abcd abcd")

# COMMAND ----------

re.search("\w+\W\w+","abcd abcd")

# COMMAND ----------

re.search("\w+\W{0,}?\w+","abcd abcd").group()

# COMMAND ----------

#\d match digits [0-9]
#\D match This matches and non digits character; ~\d

# COMMAND ----------

string = "23abcd++"
re.search("\d+",string)

# COMMAND ----------

# '\s' matches any whitespace character  new lines,tabs,spaces etc
# '\S' matches any non-whitespace character ~s

# COMMAND ----------

re.search("\S+",string).group()

# COMMAND ----------

text ="""Now you know how to set up a scalable, fault-tolerant stream using the Event Hubs
Connector for Apache Spark. Learn more about using Event Hubs with Structured Streaming and Spark Streaming by following these links:"""

# COMMAND ----------

"^".join(re.findall("\S+",text))

# COMMAND ----------

# "." dot  matches any character except newline

# COMMAND ----------

re.search(".+",text).group()

# COMMAND ----------

re.search(".+",text,flags=re.DOTALL).group()

# COMMAND ----------

# MAGIC %md ##Creating your own Character sets

# COMMAND ----------

# [A-Z] '-' is metacharater when use in [] (custom character set) 
# we read  [A-Z] as A to Z

# COMMAND ----------

text1 = "Hello,There,How,Are,You..."

# COMMAND ----------

re.findall("[A-Z]",text1)

# COMMAND ----------

re.findall("[A-Z,]",text1)

# COMMAND ----------

re.findall("[A-Z,.]",text1)

# COMMAND ----------

string =  "Hello , There , How , Are , You ..."
re.findall("[A-Z,\s.]",string)

# COMMAND ----------

# MAGIC %md ###Quantifier with custom set
# MAGIC **+** one or more <br>
# MAGIC **?** 0 or 1 <br>
# MAGIC **{}** start point and end point<br>
# MAGIC ** * ** 0 or more

# COMMAND ----------

text2 = """HELLO, There, How, Are, You... """

# COMMAND ----------

re.search("[A-Z]+",text2)

# COMMAND ----------

re.findall("[A-Z]+",text2)

# COMMAND ----------

re.findall("[A-Z]{2,}",text2)

# COMMAND ----------

re.findall("[A-Za-z\s,]+",text2)

# COMMAND ----------

re.findall("[A-Z]?[a-z\s,]+",text2)

# COMMAND ----------

re.search("[^A-Za-z\s,]+",text2)

# COMMAND ----------

re.findall("[^A-Z]+",text2)

# COMMAND ----------

# MAGIC %md ###GROUPS

# COMMAND ----------

text3 = "John have 3 dogs but I Think my friend sumit has 3 cats and Mike has 5 dogs "

# COMMAND ----------

re.findall("[A-Za-z]+ \w+ \d+ \w+",text3)

# COMMAND ----------

#() = metacharacter for groups

# COMMAND ----------

re.findall("([A-Za-z]+) \w+ \d+ \w+",text3)

# COMMAND ----------

re.findall("[A-Za-z]+ \w+ \d+ (\w+)",text3)

# COMMAND ----------

re.findall("([A-Za-z]+) \w+ (\d+) (\w+)",text3)

# COMMAND ----------

info = re.findall("([A-Za-z]+) \w+ (\d+) (\w+)",text3)

# COMMAND ----------

info

# COMMAND ----------

list(zip(*info))

# COMMAND ----------

match = re.search("([A-Za-z]+) \w+ (\d+) (\w+)",text3)

# COMMAND ----------

match.group(0) # entire mactch

# COMMAND ----------

match.groups() # pull out the group

# COMMAND ----------

match.group(1)

# COMMAND ----------

match.group(1,3)

# COMMAND ----------

match.group(3,2,1,1)

# COMMAND ----------

print(match.span())
print(match.start())
print(match.end())

# COMMAND ----------

#entire match and group 
entirematch = re.findall("(([A-Za-z]+) \w+ (\d+) (\w+))",text3)
entirematch

# COMMAND ----------

for i in entirematch:
  print(i[0])

# COMMAND ----------

it = re.finditer("([A-Za-z]+) \w+ (\d+) (\w+)",text3) #iter get exhausted

# COMMAND ----------

for ele in it:
  print(ele.group(1,3,2))

# COMMAND ----------

for ele in it:
  print(ele.group())

# COMMAND ----------

for ele in it:
  print(ele.groups())

# COMMAND ----------

# MAGIC %md ###Naming Groups

# COMMAND ----------

text4 = 'New York, New York 11396'

# COMMAND ----------

Match = re.search("([A-Za-z\s]+),([A-Za-z\s]+)(\d+)",text4)

# COMMAND ----------

Match.group(1),Match.group(2),Match.group(3),Match.group(0)

# COMMAND ----------

#?P<Name> is use for group a name

# COMMAND ----------

pattern = re.compile("(?P<City>[A-Za-z\s]+),(?P<State>[A-Za-z\s]+)(?P<ZipCode>\d+)")

# COMMAND ----------

Match1 = re.search(pattern,text4)

# COMMAND ----------

Match1.group('City'),Match1.group('State'),Match1.group('ZipCode')

# COMMAND ----------

Match1.groups()

# COMMAND ----------

Match1.groupdict()

# COMMAND ----------

# MAGIC %md ###Quantifier on Groups

# COMMAND ----------

strings = "abababababa"
re.search("(ab)+",strings)

# COMMAND ----------

strings = "abababababa"
re.search("[ab]+",strings)

# COMMAND ----------

strings = "ababababbbb"
re.search("[ab]+",strings)

# COMMAND ----------

strings = "ababababbbb"
re.search("(ab)+",strings)

# COMMAND ----------

strings = "abababcbscb"
re.search("(ab)+\w+",strings)

# COMMAND ----------

strings = "123456789"
re.findall("(\d)+",strings)

# COMMAND ----------

strings = "12345 6789"
re.findall("(\d)+",strings)

# COMMAND ----------

strings = "12345 6789"
re.findall("((\d)+)",strings)

# COMMAND ----------

strings = "abbbbb ababababab"
re.findall("(ab)+",strings)

# COMMAND ----------

strings = "abbbbb ababababab"
re.findall("((ab)+)",strings)

# COMMAND ----------

strings="Happy Birthday"
re.search("Happy (Valentines|Birthday|Anniversary)",strings)

# COMMAND ----------

# MAGIC %md 
# MAGIC ###Non-Capture groups

# COMMAND ----------

strings = "1234 56789"
re.findall("(\d)+",strings)

# COMMAND ----------

re.search("(\d)+",strings).groups()

# COMMAND ----------

# MAGIC %md
# MAGIC **?:** is non-capture groups and look slightly similar to the syntax for naming groups.<br>
# MAGIC **?P** is naming groups

# COMMAND ----------

re.findall("(?:\d)+",strings)

# COMMAND ----------

re.findall("\d+",strings)

# COMMAND ----------

text = "123123123 = Alex, 123123123 = Danny, 12345655 = Mike, 324343 = Rick, 24332 = John"
re.findall("(?:123)+ = (\w+)",text)

# COMMAND ----------

string = "1*1*1*2222 1*1*3*3*233 2*2*2*3*4* 1*2*3*3*3"
re.findall(r"(?:1\*){2,}\d+",string)

# COMMAND ----------

# MAGIC %md 
# MAGIC ###BackReferences -Using captured groups inside other operations

# COMMAND ----------

re.search(r"(\w+) \1","Merry Merry Christmas")

# COMMAND ----------

re.search(r"(\w+) \1","Merry Merry Christmas").groups()

# COMMAND ----------

re.findall(r"(\w+) \1","happy happy holiday. Merry Merry Christmas")

# COMMAND ----------

re.findall(r"(\w+) \1","happy happy holiday. Merry Merry Christmas Christmas Merry Merry")

# COMMAND ----------

# MAGIC %md
# MAGIC ^ match character at the beginning of the strings <br>
# MAGIC $ match character at the end of the string

# COMMAND ----------

string12 = """U.S had great crisis in year 2012
Lots of people die in 2012, due to flood in California.
North Korea got crisis in 2013, due to the earthquake.
Similarly china and north korea North Korea."""

# COMMAND ----------

re.search(r"^North Korea\.?",string12)

# COMMAND ----------

re.match(r"North Korea\.?",string12)

# COMMAND ----------

re.search(r"North Korea\.?$",string12)

# COMMAND ----------

# MAGIC %md ###re.MULTILINE/re.M

# COMMAND ----------

re.search(r"^North Korea\.?",string12,flags=re.MULTILINE)

# COMMAND ----------

re.match(r"North Korea\.?",string12,flags=re.MULTILINE) #re.MULTILINE work with only re.search()

# COMMAND ----------

# MAGIC %md ###re.IGNORECASE/re.I

# COMMAND ----------

re.findall("North Korea",string12,flags=re.IGNORECASE)

# COMMAND ----------

# MAGIC %md ###re.DOTALL/re.S

# COMMAND ----------

re.match(".*",string12,flags=re.DOTALL).group()

# COMMAND ----------

# MAGIC %md #re.Methods<br>
# MAGIC ###re.SPLIT

# COMMAND ----------

re.split('\.','Today is sunny.I want to go park.I want to eat ice-cream.')

# COMMAND ----------

re.split('(\.)','Today is sunny.I want to go park.I want to eat ice-cream.')

# COMMAND ----------

split ='.'
[i + split for i in re.split('\.','Today is sunny.I want to go park.I want to eat ice-cream.')]

# COMMAND ----------

string = '<p>My Mother has <span style="color:blue">blue</span>eyes.</p>'

# COMMAND ----------

re.split('<\w+>',string)

# COMMAND ----------

re.split('<.+>',string)

# COMMAND ----------

re.split('<[^<>]+>',string)

# COMMAND ----------

[i for i in re.split('<[^<>]+>',string) if i !="" ]

# COMMAND ----------

re.findall('>([^<]+)<',string)

# COMMAND ----------

# MAGIC %md ###re.SUB

# COMMAND ----------

string = """U.S. stock-indexed futures pointed
to a solidly higher open on Monday,
indicating that major
benchmarks were poised to USA rebounform last week's sharp decline
\nwhich represented their biggedt weekly dropd in months."""

# COMMAND ----------

re.sub("U.S|US|USA","United States",string)

# COMMAND ----------

# MAGIC %md ###Using Functions and Sub

# COMMAND ----------

string = "dans has 3 snails.Mike has 4 dogs.Alisa have 9 monkeys."

# COMMAND ----------

re.sub("(\d+)","1",string)

# COMMAND ----------

re.sub("(\d+)",lambda x : str((int(x.group(0))**2)),string)

# COMMAND ----------

input = "eat laugh sleep study"

result = re.sub("\w+",lambda x:x.group(0)+"ing",input)
print(result)

# COMMAND ----------

string = "Merry Merry Christmas"
re.sub(r"(\w+) (\1)",r"Happy \1",string)

# COMMAND ----------

re.sub(r"(\w+) (\1)",r"\1 Happy",string)

# COMMAND ----------

re.sub(r"(\w+) (\1)",r"Happy \2",string)

# COMMAND ----------

# COMMAND ----------
