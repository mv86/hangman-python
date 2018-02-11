def board(word, misses):
    print(f"{BOARD_IMAGES[len(misses)]}")
    print(f"Word: {' '.join(word)}\n")
    print(f"Misses: {', '.join(misses)}\n")


BOARD_IMAGES = {
    0: '',
    1: '''
            ______
            |    
            |   
            |    
            | 
        ____|_________


        ''',
    2: '''
            ______
            |    |
            |   _O_
            |    |
            | __/_\__
        ____|/_______\_


        '''
}

# s = '''
#     ______
#     |    |
#     |   _O_
#     |    |
#     | __/_\__
# ____|/_______\_
# '''