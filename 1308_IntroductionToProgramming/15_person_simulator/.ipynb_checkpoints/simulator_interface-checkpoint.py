
from simulator.life import Person

print("""
# --------------------------------------------------------------------- #
Welcome to the person simulator game!

This game will do stuff!
""")

name  = input('What is the name of your character?\n').title()
place = input('What is the birth place of your character?\n')
year  = int(input('What is the birth year of your character?\n'))

p = Person(name=name, birth_place=place, birth_year=year)

# TODO: the person must be able to quit the game halfway through
while p.alive:
    print('Player status:\n\tFood: %s\n\tMoney: %s\n\tEnergy: %s\n\tSocial: %s' % (p.food, p.money, p.energy, p.social))
    print('Location: %s' % p.location.title())
    print('What do you want to do?')
    print('\t[R]un\n\t[W]ork\n\t[E]at\n\t[S]leep\n\t[P]arty')
    choice = input('Option: ')
    std_choice = choice[0].lower()
    
    if std_choice == 'r':
        print('Select destination:')
        print('\t[W]ork\n\t[H]ome\n\t[U]rban Beach')
        dest = input('Choice: ')
        std_dest = dest[0].lower()
        if std_dest == 'w':
            p.run('work')
        elif std_dest == 'h':
            p.run('home')
        elif std_dest == 'u':
            p.run('urban beach')
        else:
            print('That is not a valid destination!')
        
    elif std_choice == 'w':
        print('How many hours will your character work?')
        hours = float(input('Choice: '))
        p.work(hours)
        
    elif std_choice == 'e':
        print('Here\'s the menu [food, €]:')
        print(p.menu)
        meal = input('Choose your meal:\n\t[S]paghetti\n\t[C]hicken\n\t[A]pple\nChoice: ')
        std_meal = meal[0].lower()
        if std_meal == 's':
            p.eat('spaghetti')
        elif std_meal == 'c':
            p.eat('chicken')
        elif std_meal == 'a':
            p.eat('apple')
        else:
            print('That meal is not on the menu!')
        
    elif std_choice == 's':
        print('How many hours will your character sleep?')
        hours = float(input('Choice: '))
        p.sleep(hours)
        
    elif std_choice == 'p':
        print('How many hours will your character party?')
        hours = float(input('Choice: '))
        p.party(hours)

    else:
        print('That is not a valid choice!')
        
    keep_playing = input('Continue? [y]/n: ')
    if len(keep_playing)>0:
        if keep_playing[0].lower() == 'n':
            break

print('Thanks for playing this awesome game! I hope your character didn\'t die!')
        
        