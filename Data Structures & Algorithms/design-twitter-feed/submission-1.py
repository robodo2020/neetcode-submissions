class Twitter:
    """
    users_dict: {}
    users_post: {} user: [(time, id)] heap
    users_followers: {}
    global_feeds [(time, user)]
    """

    def __init__(self):
        self.users_post = collections.defaultdict(list)
        self.users_followers = collections.defaultdict(set) # users: followers
        self.time = 0



    def postTweet(self, userId: int, tweetId: int) -> None:
        self.users_followers[userId].add(userId)
        self.users_post[userId].append((-self.time, tweetId))
        self.time += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        # check followers, max take 10 posts, check the heap[0]
        """
        1: [2,3,4]
        """
        all_post = []
        for follower in self.users_followers[userId]:
            all_post += self.users_post[follower]
        
        heapq.heapify(all_post)
        res = []
        while all_post and len(res) < 10:
            _, tweet_id = heapq.heappop(all_post)
            res.append(tweet_id)
        return res



        
    def follow(self, followerId: int, followeeId: int) -> None:
        self.users_followers[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.users_followers[followerId] and followerId != followeeId:
            self.users_followers[followerId].remove(followeeId)
        
