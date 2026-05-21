class Movie:
    'this class developed by shubham'
    def __init__(self,title,hero,heroin):
        self.title = title
        self.hero = hero
        self.heroin = heroin

    def display_movie_information(self):
        print(f'movie name : {self.title}')
        print(f'hero name : {self.hero}')
        print(f'heroin name : {self.heroin}')

list_of_movies = []

while True:
    title = input("Enter movie name : ")
    hero = input("Enter hero name : ")
    heroin = input("Enter heroin name : ")

    m = Movie(title,hero, heroin)
    list_of_movies.append(m)
    print("movie added successfully")

    option = input("do you want to add one more movie[yes/no] : ")

    if option.lower() =='no':
        break

print("display all movies information")

for movie in list_of_movies:
    movie.display_movie_information()
    print()