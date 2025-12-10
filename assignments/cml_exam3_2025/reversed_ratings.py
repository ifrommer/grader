privilege_names = ['lead','vote','attend']

class Member():
    
    def __init__(self, name, privileges = [0,0,1]):
        self._name = name
        self._privileges = privileges
        # self._rating = None       
        
    def get_name(self):
        return self._name
    
    def add_priv(self, priv_type):
        if priv_type == 'attend':
            self._privileges[2] = 1
        elif priv_type == 'vote':
            self._privileges[1] = 1
        elif priv_type == 'lead':
            self._privileges[0] = 1    
              
    def compute_rating(self):
        b = self._privileges
        rating = b[0] + 2 * b[1] + 4 * b[2]  # or self._rating = 
        return rating
    
    def __repr__(self):
        msg = self._name + " has these privileges:\n"
        for i in range(len(self._privileges)):
            msg += privilege_names[i] * self._privileges[i] + " "
        return msg
    
    def __lt__(self, other):
        self_rating = self.compute_rating()
        other_rating = other.compute_rating()
        return self_rating < other_rating
    
if __name__ == "__main__":
    x = Member("Joe")
    y = Member('Jane',[0,1,1])
    print(x)
    print(y)
    print(f'{x.get_name()} < {y.get_name()}? {x < y}')
