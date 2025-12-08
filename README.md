# grader
Grade student Python code

# notes
Add a `config.py` file to hold:
- standard constructor arguments
- method test arguments
- expected outputs
- class names
- point values  
etc.   

See gpt for more info

I think there might be an issue:
- if constructor fails, then calling the method may be calling the fallback, but want it to use the method from the class with the broken __init__

Can work around this - use their get_name on fallback object created with my constructor:

student_method = student_module.Restaurant.get_name  
result = student_method(fallback_obj)

it's close but getting an error plus i didn't implement this  
success, obj, note = safe_construct(module, CLASS_NAME, *INIT_ARGS)  
see that line in gpt and stuff below it