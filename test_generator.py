import json
from os import listdir
from jinja2 import Environment, FileSystemLoader

def generator(module, method, value):
    env = Environment(loader=FileSystemLoader('.'), trim_blocks=True, lstrip_blocks=True)
    template = env.get_template('template')
    mod = __import__(module)
    fun = getattr(mod, method)
    #answer = [ fun(*v) for v in value ]
    answer = []
    for v in value:
        try:
            answer.append( fun(*v) )
        except Exception, err:
            answer.append( ('error', str(err.message)) )

    output = template.render(module=module, method=method, value=value, answer=answer)

    with open('./test_cases/test_' + method + '.py', 'w') as output_file:
        output_file.write(output)


for filename in listdir('./schemas'):
    with open('./schemas/' + filename) as data_file:    
        data = json.load(data_file)
        module = filename[:-5]
        for method in data:
            value = data[method]['input']
            #print method, value
            generator(module, method, value)


