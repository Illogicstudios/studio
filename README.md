# Studio Tool

> Studio is a tool to toggle a studio in the scene

## How to install

You will need some files that several Illogic tools need. You can get them via this link :
https://github.com/Illogicstudios/common

You must specify the correct path of the installation folder in the ```template_main.py``` file :
```python
if __name__ == '__main__':
    # TODO specify the right path
    install_dir = 'PATH/TO/studio'
    # [...]
```

---

## Feature

The tool will add a reference of a studio in the scene if it doesn't already exist. If it 
exists, the reference is removed from the scene