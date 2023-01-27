# Bitly URL shortener

Console utility for shorten links using the bit.ly service. Also, the utility allows you to get the statistics of clicks by short link.

### How to install

To use the Bitly service, you need:
1. To register on the site and generate a token of "Generic Access Token" type
2. You will receive an API Bitly token in the form of a line like this: "17c09e20ad155405123ac1977542fecf00231da7"
4. To conceal data and your token, create a .env file and prescribe all the sensitive data in it, like this:
   "TOKEN=afnroeroinorf13jr94bg3fn"
5. Add the .env file in .gitignore so as not to accidentally notice it. 
   Do not forget to indicate the "python-dotenv" library on a new line in "requirements.txt".

Python3 should already be installed. 
Use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

### Project Goals

This code was written for educational purposes as part of an online course for web developers at [dvmn.org](https://dvmn.org/).
