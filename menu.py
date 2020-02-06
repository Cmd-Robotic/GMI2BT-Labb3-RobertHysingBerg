from apihandler import ApiHandler

def MainMenu():
    MovieSearcher = ApiHandler('ae69e649')
    while(True):
        UserInput = input('Allright, so whatcha wanna do?\n1. Search for some movies by name\n2. Show last search history\n3. Save the currently loaded data\n4. Load some previously saved data\n5. Terminate this Program\n')
        if ((UserInput == '1') or (UserInput == '1.') or (UserInput == '1. ')):
            MovieSearcher.Search(input('Allright, enter the name of the movie you\'re searching for.\n'))
        elif ((UserInput == '2') or (UserInput == '2.') or (UserInput == '2. ')):
            MovieSearcher.LatestSearches()
        elif ((UserInput == '3') or (UserInput == '3.') or (UserInput == '3. ')):
            MovieSearcher.SaveToJson(input('Ok, what do you want the filename to be?'))
        elif ((UserInput == '4') or (UserInput == '4.') or (UserInput == '4. ')):
            MovieSearcher.LoadFromJson(input('Alright, what\'s the name of the file you wanna load?'))
        elif ((UserInput == '5') or (UserInput == '5.') or (UserInput == '5. ')):
            return
        else:
            input('So, couldn\'t quite catch whatcha wanted to do. Please try again\n')