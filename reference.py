class Restaurant:
    
    def __init__(self, name, cuisine):
        self._name = name
        self._cuisine = cuisine
        self._ratings = []
        
    def get_name(self):
        return self._name
           
    def set_cuisine(self, new_cuisine):
        self._cuisine = new_cuisine
