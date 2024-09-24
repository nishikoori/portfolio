import json
import test

if __name__ == '__main__':
    try:
        with open('input.json', 'r') as f: 
            data = json.loads(f.read())

        output = ','.join([*data[0]])
        for obj in data:
            # print("obj - ", obj)
            output += f'\n{obj["Name"]},{obj["age"]},{obj["birthyear"]}'
            print(output)

        with open('output.csv', 'w') as f:
            f.write(output)
    except Exception as ex:
        print(f'Error: {str(ex)}')