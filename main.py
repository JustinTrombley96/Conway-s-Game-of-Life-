from map import Map

def main():
    user_rows = int(input('How many rows would you like? '))
    user_columns = int(input('How many columns would you like? '))

    game_of_life_map = Map(user_rows, user_columns)

    game_of_life_map.draw_map()

    user_action = ''
    while user_action != 'q':
        user_action = input('Press enter to add generation or q to quit:')

        if user_action == '':
            game_of_life_map.update_map()
            game_of_life_map.draw_map()
main()