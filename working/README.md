Most countries use a 24-hour clock, whereas some use a 12-hour clock. Accordingly, instead of “09:00 to 17:00”, many would say they work “9:00 AM to 5:00 PM” (or “9 AM to 5 PM”).  

This program expects a str in any of the 12-hour formats below and returns the corresponding str in 24-hour format (i.e., 9:00 to 17:00). Expecting that AM and PM will be capitalized (with no periods therein) and that there will be a space before each.  
9:00 AM to 5:00 PM  
9 AM to 5 PM  
9:00 AM to 5 PM  
9 AM to 5:00 PM  
A ValueError is raised instead if the input to convert is not in either of those formats or if either time is invalid (e.g., 12:60 AM, 13:00 PM, etc.).  
This program is based on regular expressions.
