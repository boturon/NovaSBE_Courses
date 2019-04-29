class Person:
    """
    This will describe what our simulator does!
    """
    def __init__(self, name, birth_place=None, birth_year=2000, energy=10, money=10, food=10, social=10):
        self.name = name
        self.birth_place = birth_place
        self.birth_year = birth_year
        self.money  = money
        self.food   = food
        self.social = social
        self.energy = energy
        self.alive = True
        self.location = 'home'
        self.missing_fields()
        self.menu = {'spaghetti':[3,1],'chicken':[4,2],'apple':[0.5,0.1]}
    
    def missing_fields(self):
        args = {'name':        self.name, 
                'birth_place': self.birth_place, 
                'birth_year':  self.birth_year,
                'energy':      self.energy, 
                'money':       self.money, 
                'food':        self.food, 
                'social':      self.social}
        
        for arg in args:
            if args[arg]==None:
                print('Argument %s is empty!' % arg)

    def get_info(self):
        print("""
        %s is from %s and was born in the year %s. 
        Currently he has %s food, %s energy, %s money and %s social!
        """ % (self.name, self.birth_place, self.birth_year, self.food, self.energy, self.money, self.social))
    
    def status(self):
        if self.energy<=0:
            print('%s is out of energy! He/She died of a heart attack!' % self.name)
            self.alive = False
        if self.money<=0:
            print('%s is out of money! He/She became a homeless and died of hypothermia!' % self.name)
            self.alive = False
        if self.food<=0:
            print('%s died out of hunger!' % self.name)
            self.alive = False
        if self.social<=0:
            print('%s went into a depression and died!' % self.name)
            self.alive = False
    
    def run(self, destination):
        self.energy-=1
        self.food-=0.5
        self.location=destination
        # do this in every activity
        self.status()
        
    def work(self, num_hours, income_per_hour=0.5):
        # energy -
        # food   -
        # money  +
        # social -
        if self.location == 'work':
            self.energy-=0.2*num_hours
            self.food-=0.4*num_hours
            self.social-=0.1*num_hours
            self.money+=income_per_hour*num_hours
            # do this in every activity
            self.status()
        else:
            print('%s is not at work! You will need to make him/her run to it!' % self.name)
    
    def eat(self, meal):
        # structure of list [food, €]
        
        chosen_meal = self.menu[meal]
        
        self.food  += chosen_meal[0]
        self.money -= chosen_meal[1]
        # do this in every activity
        self.status()

    def sleep(self, num_hours):
        if self.location == 'home':
            self.energy += 1.2*num_hours 
            self.food   -= 0.2*num_hours
            self.social -= 0.1*num_hours
            # do this in every activity
            self.status()
        else:
            print('%s is not at home! You will need to make him/her run to it!' % self.name)
            
    def party(self, num_hours):
        if self.location == 'urban beach':
            self.energy -= 0.3*num_hours
            self.food   -= 0.3*num_hours
            self.money  -= 0.5*num_hours
            self.social += 1.5*num_hours
            # do this in every activity
            self.status()
        else:
            print('%s is not at urban beach! You will need to make him/her run to it!' % self.name)
    
    
    
    