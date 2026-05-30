Most YouTube videos can be embedded in other websites. On any video if you click Share, and then click Embed, you’ll see HTML , which can then be copied into your any website’s source code, wherein iframe is an HTML “element,” and src is one of several HTML “attributes” therein, the value of which, between quotes, is the video url.  
<iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>  

We’d like to extract the URLs of YouTube videos that are embedded in pages , converting them back to shorter, shareable youtu.be URLs where they can be watched on YouTube itself.
This program expects a str of HTML as input, extracts any YouTube URL that’s the value of a src attribute of an iframe element therein, and returns its shorter, shareable youtu.be equivalent as a str. Expecting that any such URL will be in one of the formats below. Assuming that the value of src will be surrounded by double quotes. And that the input will contain no more than one such URL. If the input does not contain any such URL at all, None is returned.  
http://youtube.com/embed/xvFZjo5PgG0
https://youtube.com/embed/xvFZjo5PgG0
https://www.youtube.com/embed/xvFZjo5PgG0  
This program is based on Regular expressions and uses the RegEx or re module
