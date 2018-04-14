import os, fnmatch
import difflib

def find(pattern):
    result = []
    path=r'C:\Users\Mahender Goel\Documents\MUSIC\songs'
    for root, dirs, files in os.walk(path):
        for name in files:
            d = difflib.SequenceMatcher(None,name, pattern).ratio()
            if d>=0.3:
                result.append(os.path.splitext(name)[0])
    return result[:10]

#print(find('dil'))
