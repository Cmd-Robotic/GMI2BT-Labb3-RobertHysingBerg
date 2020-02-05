from requests import get

class ApiHandler:
    ApiKey = ''
    SearchHistory = []
    def __init__(self, API):
        self.ApiKey = API
    # def SetApiKey(self, API):
    #     self.ApiKey = API
    def Search(self, name):
        Result = get(f'http://www.omdbapi.com/?apikey={self.ApiKey}&s={str(name)}')
        Films = []
        counter = 1
        try:
            for Movie in Result.json()['Search']:
                Film = {}
                Film['Title'] = Movie['Title']
                Film['Year'] = Movie['Year']
                Film['Type'] = Movie['Type']
                Films.append(Film)
                print(f'{counter}. {Film}')
                counter += 1
            if (1 < len(Films)):
                try:
                    UserInput = int(input('So which movie were you searching for?\n'))
                    counter = 1
                    for Film in Films: #I present this mad scalable menu unto thee
                        if (UserInput == counter):
                            UsersChoice = Film
                        counter += 1
                    self.SearchHistory.append(UsersChoice)
                except ValueError as VErr:
                    input(f'So an "{VErr}" exception was thrown. Please enter something valid next time...')
                except UnboundLocalError as ULErr:
                    input(f'Well, it looks like an "{ULErr}" exception was thrown, looks like what you entered wasn\'t one of the choices.')
        except KeyError as KErr:
            input(f'Due to a "{KErr}" being thrown, there are no hit\'s in the database for your search of {name}\n')
    def LatestSearches(self):
        counter = 1
        print(f'Allright, these are the searches stored in the memory:')
        for PastSearch in self.SearchHistory:
            print(f'{counter}. {PastSearch}')
            counter += 1
    def SaveToJson(self, FileName):
        print('')
    def LoadFromJson(self, FileName):
        print('')