import 5-rock_paper_scissors


while True:
    play = input('Would you like to play rock, paper, scissors? y/n: ').lower()
    if play == 'n':
        print('Thanks for playing.  Goodbye.\n')
        break
    elif play == 'y':
        rock_paper_scissors.play_rps()
    else:
        print('Make a choice of y or n.')
