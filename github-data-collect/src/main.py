import sys

from core.useCases.random_users_data import RandomUsersData
from core.useCases.initial_data import InitialData

from config.environments import INITIAL_USER

if __name__ == "__main__":
    
    option = int(sys.argv[2])

    if option == 1:
        initial = InitialData(username=INITIAL_USER)
        initial.Boostrap()
        
    elif option == 2:
        random = RandomUsersData(num_random_users=3)
        random.Boostrap()

    else:
        print("Invalid option")
