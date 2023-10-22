startup
    went to Pleiades, downloaded a site as a JSON file
    opened the JSON here and in jypter
        {} - curly brackets usually means dictionary
            this is a JSON file, however. python treats JSON "objects" as dictionaries


>> import json 
in python
change from
>> with open('589918.json', encoding = 'utf-8') as f:
    data = f.read()
to
>> with open('589918.json', encoding = 'utf-8') as f:
    data = json.load(f)

the former reads it as a txt file, the latter as a JSON file, which python understands as a dictionary

dictionaries
    keys, values

the JSON file is a dictionary inside a list inside a dictionary
    read a dict with dictname['name of key']
    read a list with listname[#] (place number in the bracket)

now let's read from pleiades directly, rather than downloading the file
>>    def getjson(uri) :
>>        uri = f'https://pleiades.stoa.org/places/{uri}/json'
>>        with urllib.request.urlopen(uri) as f:
>>            data = json.loads(f.read().decode())
>>        return data

>> def coordinates(uri) : 
>>     return getjson(uri)['features'][0]['geometry']['coordinates']

Notes
        Helpful websites

            Recogito
                https://recogito.pelagios.org/
            Loco:lligo
                https://docuracy.github.io/Locolligo/
            Peripleo
                https://github.com/britishlibrary/peripleo

        Shortcuts for VSCode

            Shift + Alt + F (Windows)
            Shift + Option + F (Mac)

        Tag for Peripleo

        <iframe src=" " style="width:100%; height:50vw;"></iframe>


Loco:lligo 
    transmutes csv to JSON
peri pleo
    this is a repo from github
    we imported it, so we all have a copy of it on our own githubs
    we then uploaded our JSON to our github repo
    
