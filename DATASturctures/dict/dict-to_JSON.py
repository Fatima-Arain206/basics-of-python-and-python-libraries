#%%
import json

#   convert python dictionary into json file
py_dict={
    'name':'fatima',
    'pass':True,
    'cgpa':3.906,


}
## the dumps function convert the python text in string
# it connverts None to null '' qoute to "" and True to true
# just convert to jason string
json_string=json.dumps(py_dict , indent=4)# indent is for space and new lines
print(json_string)
print(type(json_string))
#%%
# direct convert to jason file
with open("student_records.json","w") as file:
    json.dump(py_dict,file, indent=4)