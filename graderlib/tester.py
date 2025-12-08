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
    
    
def test_method(obj, method_name, reference_value = None, *args, **kwargs):
    """ Safely call a method and compare with an expected reference value.
    Returns (True/False, result or exception) """
    note = '~~~ test_method note not done yet'
    try:
        method = getattr(obj, method_name)
        result = method(*args, **kwargs)
        success = (result == reference_value)
        return success, result, note
    except Exception as e:
        return False, e, note
    