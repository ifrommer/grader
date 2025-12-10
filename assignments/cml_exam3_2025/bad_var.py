privilege_names = ['lead','vote','attend']

class Member():
    
    def __init__(self, name, privileges = [0,0,1]):
        self._name = name
        self._privileges = [1,1,1]

    def get_name(self):
        print('in bad_init''s get_name with fallback obj',self)
        return self._name