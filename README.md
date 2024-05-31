# Reference-resolver
Turn chemistry references into links. I use this to quickly insert links to presentations and conference notes. This script is not the clever part; it is powered by the awesome [Chemistry Reference Resolver](https://chemsearch.kovsky.net/) by Oleksandr Zhurakovsky. 

## Use
I like to be able to type "ref" followed by the reference I want to link to in Windows cmd and have the script generate the link. For this, I save a separate batch file `ref.bat` in a location pointed to by my PATH environment variable, which contains this text: 

```
@echo off
python "path\to\script\ref.py" %*
```
replacing the path\to\script with the actual script path. 

Now, I can type this kind of command in any cmd window, to have the link generated and copied to my clipboard: 
```
ref "Organic Letters 25, 2945-2947"
```
```
ref "OL 2015, 17, 5728"
```
```
ref "10.1021/acs.oprd.1c00167" -nopaste
```
Don't forget the double quote marks on the reference (only strictly necessary when there's whitespace in the argument). 

If I don't want it copied to my clipboard, I can type ` -nopaste` after my command &ndash; though I highly recommend using Windows Clipboard History (WIN + v). 
