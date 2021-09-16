# Demonstrates reading and writing yml files.
import yaml

dict = {
    'name': 'yml test file',
    'float': 1.51,
    'list': [
        0,
        {
            'name': 'nested dictionary',
            'index': 1
        }
    ],
    'dict': {
        'item': 'fruit',
        'origin': 'brazil'
    }
}

filepath = './yml_test_file.yml'
with open(filepath, 'w') as f:
    yaml.dump(dict, f, allow_unicode=True)

# yaml.load() will result in a depreciation warning because
with open(filepath, 'r') as f:
    print(yaml.safe_load(f))
