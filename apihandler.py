from pip._vendor.requests import get
from pathlib import Path
from json import dump, load

class ApiHandler:
    ThomasÄrDenBästa = True
    ApiKey = ''
    SearchHistory = []
    def __init__(self, API):
        self.ApiKey = API
    # def SetApiKey(self, API):
    #     self.ApiKey = API
    def Search(self, name):
        Result = get(f'http://www.omdbapi.com/?&s={str(name)}&apikey={self.ApiKey}')
        Films = []
        counter = 1
        try:
            for Movie in Result.json()['Search']:
                Film = {}
                Film['Title'] = Movie['Title']
                Film['Year'] = Movie['Year']
                Film['Type'] = Movie['Type']
                Film['Poster'] = Movie['Poster']
                Film['imdbID'] = Movie['imdbID']
                Films.append(Film)
                print(f'{counter}. Name: {Film["Title"]}, first released in: {Film["Year"]} and is a {Film["Type"]}')
                counter += 1
            if (1 < len(Films)):
                try:
                    UserInput = int(input('So which movie were you searching for?\n'))
                    counter = 1
                    for Film in Films: #I present this mad scalable menu unto thee
                        if (UserInput == counter):
                            UsersChoice = Film
                        counter += 1
                    Movie = get(f'http://www.omdbapi.com/?&i={UsersChoice["imdbID"]}&plot=full&apikey={self.ApiKey}')
                    UsersChoice['Plot'] = Movie.json()['Plot']
                    if (UsersChoice['Plot'] == 'N/A'):
                        UsersChoice['Plot'] = 'There is no plot summary in the database for this movie currently'
                    if (UsersChoice['Poster'] != 'N/A'):
                        Poster = 'the link to the movie\'s poster is ' + UsersChoice['Poster']
                    else:
                        Poster = 'the movie has no poster registered in the database'
                    print(f'The movie {UsersChoice["Title"]} which was a {UsersChoice["Type"]} was first released in {UsersChoice["Year"]} had a plot along the lines of:\n{UsersChoice["Plot"]}\nAnd {Poster}')
                    self.SearchHistory.append(UsersChoice)
                except ValueError as VErr:
                    input(f'So an "{VErr}" exception was thrown. Please enter something valid next time...')
                except UnboundLocalError as ULErr:
                    input(f'Well, it looks like an "{ULErr}" exception was thrown, looks like what you entered wasn\'t one of the choices.')
        except KeyError as KErr:
            input(f'Due to a "{KErr}" exception being thrown, there are no hit\'s in the database for your search of {name}\n')
    def LatestSearches(self):
        if (self.SearchHistory):
            counter = 1
            print(f'Allright, these are the searches stored in the memory:')
            for PastSearch in self.SearchHistory:
                print(f'{counter}. Name: {PastSearch["Title"]}, first released in: {PastSearch["Year"]} and is a {PastSearch["Type"]}')
                counter += 1
            try:
                UserInput = int(input('So which past searched movie were you looking for?\n'))
                counter = 1
                for Film in self.SearchHistory: #I present this mad scalable menu unto thee
                    if (UserInput == counter):
                        UsersChoice = Film
                    counter += 1
                if (UsersChoice['Poster']):
                    Poster = 'the link to the movie\'s poster is ' + UsersChoice['Poster']
                else:
                    Poster = 'the movie has no poster registered in the database'
                print(f'The movie {UsersChoice["Title"]} which was a {UsersChoice["Type"]} was first released in {UsersChoice["Year"]} had a plot along the lines of:\n{UsersChoice["Plot"]}\nAnd {Poster}')
            except ValueError as VErr:
                input(f'So an "{VErr}" exception was thrown. Please enter something valid next time...')
            except UnboundLocalError as ULErr:
                input(f'Well, it looks like an "{ULErr}" exception was thrown, looks like what you entered wasn\'t one of the choices.')
            input('\n')
        else:
            input('There isn\'t any data currently loaded')
    def SaveToJson(self, FileName):
        FilePath = './' + FileName + '.json'
        if (Path(FilePath).is_file()):
            UserInput = input('That file already exist, would you like to write it over? Y/N').upper()
            if (UserInput == 'Y' or UserInput == 'YE' or UserInput == 'YES'):
                FilePointer = open(FilePath, 'w', encoding='UTF-8')
                dump(self.SearchHistory, FilePointer)
                FilePointer.close()
                input('Allright, current data saved\n')
            elif (UserInput == 'N' or UserInput == 'NO' or UserInput == 'NES'):
                input('Allright, sending ya back to the main menu\n')
            else:
                input('Couldn\'t quite catch what you were saying, sending ya back.\n')
        else:
            FilePointer = open(FilePath, 'w', encoding='UTF-8')
            dump(self.SearchHistory, FilePointer)
            FilePointer.close()
            input('Allright, current data saved\n')
    def LoadFromJson(self, FileName):
        FilePath = './' + FileName + '.json'
        if (Path(FilePath).is_file()):
            UserInput = input('Are you sure you wanna do this? Any unsaved data will be deleted. Y/N').upper()
            if (UserInput == 'Y' or UserInput == 'YE' or UserInput == 'YES'):
                FilePointer = open(FilePath, 'r', encoding='UTF-8')
                try:
                    self.SearchHistory = load(FilePointer)
                    input('Allright, data loaded. Bye bye old data...')
                except ValueError:
                    input('Looks like the file was empty or unreadable, check if the file\'s data has been damaged and or deleted.')
                FilePointer.close()
            elif (UserInput == 'N' or UserInput == 'NO' or UserInput == 'NES'):
                input('Allright, sending ya back to the main menu')
            else:
                input('Couldn\'t quite catch what you were saying, sending ya back.')
        else:
            print('Looks like that file doesn\'t exist in my directory, please enter one that does?')