# Coming soon...
# reusable grading library  via gpt

def safe_construct(module, cls, *args, fallback=None, **kwargs):
    """  cls is the class to test, conventionally written as cls
    Safely try to construct an object.
    If it fails, return `fallback` which will be the object created with
     my reference class (so I can test their later methods).
    Call like this:
    ok, obj = safe_construct(class_to_test, *args, fallback=fallback_obj)
    where fallback_obj created, e.g., like this:
    from reference import Restaurant as RefRestaurant
    # reference.py has the solution (reference) Restaurant class
    # Fallback object if student __init__ fails
    fallback_obj = RefRestaurant("Alice", "Italian")
    """
    try:  # 1st see if they have the correct class name
        cls_to_test = getattr(module, cls)
    except AttributeError:
        return False, fallback, f"Class '{cls}' not found in module."
            
    try:
        obj = cls_to_test(*args, **kwargs)
        return True, obj, "Successful"
    except Exception as e:
        return False, fallback, f"Student constructor raised an exception: {e}"
    
    
def test_method(student_cls, obj, method_name, reference_value = None, 
                *args, **kwargs):
    """ Safely call a method and compare with an expected reference value.
    Returns (True/False, result or exception, note (str)) 
    """
    if not hasattr(student_cls, method_name):
       return False, None, f"Method {method_name} not found"
    fn = getattr(student_cls, method_name)
    try:
        result = fn(obj, *args, **kwargs)
    except Exception as e:
        return False, None, f"Error calling {method_name}: {e}"
    
    # no-return-value expected
    if reference_value is None:
        if result is None:
            return True, None, ""
        else:
            return False, result, f"Should not return a value but returned {result}"

    # compare return value
    if result == reference_value:
        return True, result, ""
    else:
        return False, result, f"Expected {reference_value}, got {result}"
    