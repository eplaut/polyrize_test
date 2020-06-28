# Polyrize Home Exercise
Answers for Polyrize Home exercise 

# Installation
Unfortunatly, there is not installation method.

In order to use the code in this repo, you will have to clone it and run it locally. alternativly, you can move the file to a path available in your `PYTHONPATH` environment variable.

# Question #1

The is an implemenation for a magic list, where you may set the next element, without explictly amend the element.

    from magiclist import MagicList
    
    my_list = MagicList()
    my_list[0] = 42
    my_list[1] = ['foo', 'bar']
    
    # You cannot create new index, without consecutive order
    # my_list[10] = 'jumping few indexes' -> Will raise IndexError
   
Additional feature will give you simular experiance as `collections.defautdict`, where you can have assign default classtype to the new element

    from magiclist import MagicList
    
    my_list = MagicList(cls_type=dict)
    my_list[0]['name'] = 'Raymond'
    
# Question #2

Sanic web application to short list of dictionaries to a key-value object. The API assume the input is list of object, where each objecj has a `name` key and one key with the str `val` in it.

For example:

    [
        {
            "name": "Raymond",
            "val": "Hettinger"
        },
        {
            "name": "David",
            "val": "Beazley"
        }
    ]
    
will be shorten to:

    {
        "Raymond": "Hettinger",
        "David": "Beazley"
    }
    
Notes:
1. Any other feild will be ignored.
2. Value feild can be anything contains the str "val" (case insensitive)
3. Multiple values which follows the note above, will behave inconsistently

The application uses an `auth.pw` file for authentication. File format is json of user to password dictionary.
