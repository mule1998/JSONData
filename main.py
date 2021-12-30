import json

class JsonData:
    @staticmethod
    def load_data(json_file):
        '''load the json data and covert json into dictionary format'''
        data = open(json_file)
        json_file = json.load(data)
        return json_file

    @staticmethod
    def dump_data():
        '''converting dictionary format data into the json'''
        data_dict = {
            "emp1": {
                "name": "Lisa",
                "designation": "programmer",
                "age": "34",
                "salary": "54000"
                },
            "emp2": {
                "name": "Elis",
                "designation": "Trainee",
                "age": "24",
                "salary": "40000"
                },
            }
        out_json = open("dumpf.json", "w")
        json_dump = json.dump(data_dict, out_json)
        out_json.close()
        return json_dump

value = JsonData()
data1 = value.load_data('C:\Users\Shubham\Desktop\Python\JSON\sample2.json')
data2 = value.dump_data()
print(data1)
print(data2)