# Databricks notebook source
import re

# COMMAND ----------

# MAGIC %md ###Word Boundries

# COMMAND ----------

# MAGIC %md \b is called 'boundary' and allows you to isolate words.
# MAGIC 
# MAGIC - is similar to ^ and $ (location and no consumption)

# COMMAND ----------

string = "cat catherine catholic wildcat copycat uncatchable"

# COMMAND ----------

pattern = re.compile(r"\bcat\b")

# COMMAND ----------

re.findall(pattern,string)

# COMMAND ----------

string1 = "@montra.org"
string2 = "@montraorg"
string3 = "montra@org"
string4 = "@montra_org"
string5 = "@montra_org @montra_org @montra_org"

# COMMAND ----------

pattern = re.compile(r"\B@[\w]+\b(?!\.)")
re.findall(pattern,string5)

# COMMAND ----------

pattern = re.compile(r"\B@[\w]+$")

# COMMAND ----------

re.search(pattern,string4) # 2 and 4 will give the output

# COMMAND ----------

# MAGIC %md ###Look Around
# MAGIC  

# COMMAND ----------

# 4 Types of look arounds  
positive look ahead ?=
Negative look ahead ?!
positive look behind ?<=
Negative look behind ?<!

# similar syntax
?: # non-capturing groups
?P # naming groups  

# COMMAND ----------

string ='''ABC1   1.1.1.1   201511199   active
           ABC2   2.2.2.2   201511199   inactive
           ABC3   x.x.x.x   201511199   active'''

# COMMAND ----------

pattern = re.compile('ABC\w\s+(\S+)\s+\S+\s+(?=active)') # positive look ahead
re.findall(pattern,string)

# COMMAND ----------

re.search(pattern,string)

# COMMAND ----------

pattern = re.compile('ABC\w\s+(\S+)\s+\S+\s+(?:active)') # non-capturing group but consume
re.findall(pattern,string)


# COMMAND ----------

re.search(pattern,string)

# COMMAND ----------

# MAGIC %md ###Difference between non-capture groups and look arounds

# COMMAND ----------

string = "abababacb"
pattern = re.compile("(?:b)(a)(?:b)")

# COMMAND ----------

re.findall(pattern,string)

# COMMAND ----------

pattern = re.compile("(?<=b)(a)(?=b)")

# COMMAND ----------

re.findall(pattern,string)

# COMMAND ----------

pattern = re.compile("(?=(bab))")

# COMMAND ----------

re.findall(pattern,string)

# COMMAND ----------

string ="I love cherries, apples, and strawberries."
pattern  = re.compile("(\w+)(?=\.|,)")
re.findall(pattern,string)

# COMMAND ----------

pattern2  = re.compile("(\w+)(?:\.|,)")

# COMMAND ----------

re.findall(pattern2,string)

# COMMAND ----------

# MAGIC %md ###consecutives look around fallacy

# COMMAND ----------

string='''cheery 100 red
          apples 200 green
          grapes 500'''

# COMMAND ----------

pattern =re.compile(r"[a-z]+\s*(?=\d+)(?=\s*)(?=[a-z]+)")

# COMMAND ----------

re.findall(pattern,string)

# COMMAND ----------

pattern1 =re.compile("[a-z]+\s*(?=\d+\s*[a-z]+)")
re.findall(pattern1,string)

# COMMAND ----------

#Password validation example #order doesn't matter

# COMMAND ----------

pattern = re.compile("(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!?.])\S+")

# COMMAND ----------

string1="ABZ#!3232asvdve..."
string2="ABZ#3232asvdve"

# COMMAND ----------

re.search(pattern,string1)

# COMMAND ----------

re.search(pattern,string2)

# COMMAND ----------

# MAGIC %md
# MAGIC Negative look ahead ?! <br>
# MAGIC Negative look behind ?<!

# COMMAND ----------

string = """
Remamining party applicants:

Occuption: Party Planner
Occuption: Baking
Occuption: Cook
Occuption: Publicist
Occuption: Entertainer
Occuption: Baker
Occuption: baker
Occuption: pierrot"""

# COMMAND ----------

pattern  = re.compile("Occuption: (?!Baker|Cook|Baking).+",flags=re.I)

# COMMAND ----------

re.findall(pattern,string)

# COMMAND ----------

string = """
Full Invitation List:

Guest: Sumit Maurya
Guest: Arun Tagde
Guest: Vishal singh
Guest: Manohar singh
Entertainer: jarna kantaria
Baker: Bharat singh
Party: Vidit singh
Publist: Darryl Dsouza
Baker: Salim Rampurawala"""

# COMMAND ----------

pattern  = re.compile(r"(?<!Baker: )\b\w+\s+\w+$",flags=re.I|re.M)

# COMMAND ----------

re.findall(pattern,string)

# COMMAND ----------

string = """
Full Invitation List:

Guest: Sumit Sahadev Maurya
Guest: Arun Tagde
Guest: Vishal singh
Guest: Manohar singh
Entertainer: jarna kantaria
Baker: Bharat singh
Party: Vidit singh
Publist: Darryl Dsouza
Baker: Salim Rampurawala"""

# COMMAND ----------

pattern  = re.compile(r"(?<!Baker: )(\b\w+\s+\w+$|\b\w+\s+\w+\s+\w+$)",flags=re.I|re.M)

# COMMAND ----------

re.findall(pattern,string)

# COMMAND ----------

pattern  = re.compile(r"^(?!Baker: ).+\w+$",flags=re.I|re.M)

# COMMAND ----------

re.findall(pattern,string)

# COMMAND ----------

string ='''1111  ABCC   777777777   active
           2222  ABC    888888888   inactive
           3333  XYZ    xxxxxxxxx   active
           4444  1234   203511199   inactive
           5555  1445   201511199   inactive
           '''

# COMMAND ----------

import regex

# COMMAND ----------

pattern = regex.compile('(?<=[A-Z]+)[A-Z]+\s+(\S+)')

# COMMAND ----------

regex.findall(pattern,string)

# COMMAND ----------

s = "C:\Tools\System32\calc.exe"
s2 = "C:\Windows\Tools\System32\calc.exe"
s3 = "C:\Windows\Tools\System32\De-de\calc.exe"
s4 = "C:\Tools\calc.exe"

# COMMAND ----------

pattern = re.compile(r"(?<!System32.*)calc.exe") #error look-behind requires fixed-width pattern

# COMMAND ----------

pattern = regex.compile(r"(?<!System32.*)calc.exe")

# COMMAND ----------

regex.findall(pattern,s4)
