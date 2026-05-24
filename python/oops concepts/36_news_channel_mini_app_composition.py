# Movie News Class
class MovieNews:

    def __init__(self, movie_name, actor, rating, release_year):

        self.movie_name = movie_name
        self.actor = actor
        self.rating = rating
        self.release_year = release_year

    def show_movie_news(self):

        print("===== Movie News =====")
        print("Movie Name   :", self.movie_name)
        print("Main Actor   :", self.actor)
        print("Rating       :", self.rating)
        print("Release Year :", self.release_year)


# Sports News Class
class SportsNews:

    def __init__(self, sport_name, team, captain, trophy):

        self.sport_name = sport_name
        self.team = team
        self.captain = captain
        self.trophy = trophy

    def show_sports_news(self):

        print("\n===== Sports News =====")
        print("Sport Name :", self.sport_name)
        print("Team       :", self.team)
        print("Captain    :", self.captain)
        print("Trophy     :", self.trophy)

# Politics News Class
class PoliticsNews:

    def __init__(self, party_name, leader, state, election_year):

        self.party_name = party_name
        self.leader = leader
        self.state = state
        self.election_year = election_year

    def show_politics_news(self):

        print("\n===== Politics News =====")
        print("Party Name    :", self.party_name)
        print("Leader        :", self.leader)
        print("State         :", self.state)
        print("Election Year :", self.election_year)


# Main ABP News Channel Class
class ABPNewsChannel:

    def __init__(self):

        # HAS-A Relationship

        self.movie = MovieNews(
            "Pushpa 2",
            "Allu Arjun",
            9.2,
            2025
        )

        self.sports = SportsNews(
            "Cricket",
            "India",
            "Rohit Sharma",
            "World Cup"
        )

        self.politics = PoliticsNews(
            "BJP",
            "Narendra Modi",
            "Maharashtra",
            2026
        )

    def show_all_news(self):

        print("========= ABP NEWS CHANNEL =========\n")

        self.movie.show_movie_news()
        self.sports.show_sports_news()
        self.politics.show_politics_news()

# Object Creation
abp = ABPNewsChannel()

# Calling Method
abp.show_all_news()
