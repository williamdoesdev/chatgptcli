import yaml

def set_config(key, value):
    with open('config.yml', 'r') as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
        config[key] = value
    with open('config.yml', 'w') as f:
        yaml.dump(config, f)

def get_config(key):
    with open('config.yml', 'r') as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
        return config[key]