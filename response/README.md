When creating a Google Form that prompts users for a short answer (or paragraph), it’s possible to enable response validation and require that the user’s input match a regular expression. For instance, you could require that a user input an email address with a regex like this one:  
^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$  
Or you could more easily use Google’s built-in support for validating an email address.      

This is a program that prompts the user for an email address via input and then prints Valid or Invalid, respectively, if the input is a syntatically valid email address.    
This program is based on regular expressions and uses the validator_collection library . As to run this code make sure to download the library by passing the command - pip install validator_collection.
