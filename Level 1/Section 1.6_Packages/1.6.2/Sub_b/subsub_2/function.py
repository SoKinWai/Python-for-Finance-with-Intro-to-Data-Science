#c. Create one or more Python scripts in each subfolder, at each level.
# Each script should have a unique function (you may reuse previously-created functions and/or create new functions).
# Be sure to name the scripts aptly.

def function(name, age=None, **kwargs):
    print(name,age,kwargs.get('State'),kwargs.get('Weight'),kwargs.get('Height'),kwargs.get('HairColor'))