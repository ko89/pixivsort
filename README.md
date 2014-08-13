# pixivsort

This script is most usefull in combination with the Firefox Addon "Ank Pixiv Tool".
With the Addon one can download images of the SNS pixiv with specific filenames.
But since all images are saved into one directory it's kind of messy.
Given the directory with downloaded images 
and a second directory containing subdirectories for each artist,
the script will sort all images into these subdirectories.

## How does it work?
The script searches through the two given directories (SOURCE and DESTINATION).
    
The naming conventions for SOURCE and DESTINATION are currently hardcoded in
main.py. They are regular expressions matching the following names:
SOURCE:
```
    (<artist id>) <artist> - <title>.<extension>
    or for directories:
    (<artist id>) <artist> - <title>
```
DESTINATION:
```
    <artist> (<artist id>)
```        
If you wish to use different naming conventions please change those two
regular expressions.
    
## How to use it?
To run the script, start main.py with source and destination paths:
```
    python pixivsort.py /path/to/source /path/to/destination
```
