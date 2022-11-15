# fiskabur 🐡
fiskabúr - pronouced (fish-ka-bush) is a basic template for running javascript app in a desktop wrapper
the code is tiny and easy to read and *seems* less resource intensive then electron


## Development

```bash
pip install -r requirements.txt 
python3 main.py
```

# Why make this?
- eletron is too heavy
- the api is as big or little as you want it because its custom
- common operation people need (open file, save file, save settings, camera) [coming soon]

# Building

Window/Mac
```bash
pyinstaller main.py 
```

Mac
```bash
python3 build-mac.py py2app
```

## TODO
- include chumbucket somehow
- common operation modules

# Docs
https://pywebview.flowrl.com/

# Icons

https://pngtoicon.com/
https://pypi.org/project/generate-iconset/

Size generator + Mac icns
```
$ generate-iconset assets/icon.png
```





