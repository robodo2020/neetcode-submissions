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
        

    def getNewsFeed_og(self, userId: int) -> List[int]:
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

    
    def getNewsFeed(self, userId: int) -> List[int]:
        # check followers, max take 10 posts, check the heap[0]
        """
        having ptr for each follower, every time get the most recent one from all of them, move the ptr
        TC: O(N) N -> number of followers O(10)
        """
        heap = []
        # initialize each user pointers
        followees = self.users_followers[userId]
        for f in followees:
            posts = self.users_post[f]
            if posts:
                idx = len(posts) - 1
                time, tid = posts[idx]
                heapq.heappush(heap, (time, tid, f, idx)) # push each followee's last post to heap
        res = []

        while heap and len(res) < 10:
            time, tid, f, idx = heapq.heappop(heap)
            res.append(tid)

            idx -= 1
            if idx >= 0:
                next_time, next_tid = self.users_post[f][idx] # since already use the original post, take the next post and put to heap
                heapq.heappush(heap, (next_time, next_tid, f, idx))
        return res
        
    def follow(self, followerId: int, followeeId: int) -> None:
        self.users_followers[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.users_followers[followerId] and followerId != followeeId:
            self.users_followers[followerId].remove(followeeId)
        
