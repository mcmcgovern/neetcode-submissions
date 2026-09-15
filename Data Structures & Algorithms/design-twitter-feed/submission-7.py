class Twitter:

    def __init__(self):
        # presumably a heap, 10 allowed
        self.timestamp = 0
        self.tweets = defaultdict(list) # maps userId to list of (timestamp, tweetId)
        self.follow_map = defaultdict(set) # maps userId: set(people they follow)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.timestamp, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # first get all tweets from all users that userId follows (plus user's tweets)
        most_recent = []
        for user in self.follow_map[userId].union({userId}):
            # with this user we can key into tweets list
            # get 10 most recent tweets from each user, add to list of lists
            ten_recent = sorted(self.tweets[user], key=lambda tweet_list: tweet_list[0])[-10:]
            for tweet in ten_recent:
                most_recent.append(tweet)

        news_feed_values = sorted(most_recent, key=lambda tweet: tweet[0], reverse=True)[:10]
        # print(news_feed_values)
        # news_feed_values = sorted(most_recent, key=lambda tweet: tweet[0], reverse=True)[-10:]
        return [tweet[1] for tweet in news_feed_values]

        


    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId != followerId and followeeId not in self.follow_map[followerId]:
            self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follow_map[followerId]:
            self.follow_map[followerId].remove(followeeId)
