from apihandler import ApiHandler

def MainMenu():
    ApiKey = 'ae69e649'
    MovieSearcher = ApiHandler(ApiKey)
    while(True):
        UserInput = input('Allright, so whatcha wanna do?\n1. Search for some movies by name\n2. Show last search history\n3. Terminate this Program\n')
        if ((UserInput == '1') or (UserInput == '1.') or (UserInput == '1. ')):
            MovieSearcher.Search(input('Allright, enter the name of the movie you\'re searching for.\n'))
        elif ((UserInput == '2') or (UserInput == '2.') or (UserInput == '2. ')):
            MovieSearcher.LatestSearches()
        elif ((UserInput == '3') or (UserInput == '3.') or (UserInput == '3. ')):
            return
        else:
            input('So, couldn\'t quite catch whatcha wanted to do. Please try again\n')