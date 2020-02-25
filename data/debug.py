import yaml
import os

curpath = os.path.dirname(os.path.realpath(__file__))
yamlpath = os.path.join(curpath, "data.yaml")

data = {'name': '测试',
        'data':'1233',
        'age':123}

# with open(yamlpath, 'w', encoding='utf-8') as f:
#     yaml_obj = yaml.dump(data, f,allow_unicode=True,sort_keys=False)

f = open(yamlpath,'r',encoding='utf-8')
# with open(yamlpath,'r',encoding='utf-8') as f:
#     f_data = f.read()
#     yaml_data = yaml.load(f_data,Loader=yaml.FullLoader)
#     print(yaml_data)
