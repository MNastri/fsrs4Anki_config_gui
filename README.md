## UI.py
This is a small UI that lets you change your deck config as table
and then convert it to text so that you can paste it in the 
custom scheduler field in Anki  

### Example
![img_2.png](img_2.png)
to use:  
`$ pip install -r requirements.txt`  
`$ python -m UI`

## main.py
This reads a toml file and outputs the code to be pasted in the custom
scheduler field in Anki.

toml is a minimal configuration file format that is very readable
due to obvious semantics (https://toml.io/en/)

I noticed some quirks with toml, like all the elements should be 
float in the `w` parameter or it won't parse the config file.

### The input config file
![img.png](img.png)
### the output string
![img_1.png](img_1.png)

to use:  
`$ pip install -r requirements.txt`  
`$ python -m main`