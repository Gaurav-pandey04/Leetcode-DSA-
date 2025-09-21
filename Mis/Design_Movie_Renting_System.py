from sortedcontainers import SortedSet

class MovieRentingSystem:
    def __init__(self, n, entries):
        # Price lookup
        self.price = {}
        for shop, movie, p in entries:
            self.price[(shop, movie)] = p

        # Unrented: Movie -> SortedSet[(price, shop)]
        self.unrented = {}
        for shop, movie, p in entries:
            if movie not in self.unrented:
                self.unrented[movie] = SortedSet()
            self.unrented[movie].add((p, shop))

        # Rented: global SortedSet[(price, shop, movie)]
        self.rented = SortedSet()

    def search(self, movie):
        if movie not in self.unrented:
            return []
        # take cheapest 5
        return [shop for (price, shop) in list(self.unrented[movie])[:5]]
    
    def rent(self, shop, movie):
        p = self.price[(shop, movie)]
        self.unrented[movie].discard((p, shop))
        self.rented.add((p, shop, movie))

    def drop(self, shop, moive):
        p = self.price[(shop, moive)]
        self.rented.discard((p, shop, moive))
        self.unrented[moive].add((p, shop))

    def report(self):
        # Take cheapest 5
        return [[shop, movie] for (p, shop, movie) in list(self.rented)[:5]]
    
movieRentingSystem = MovieRentingSystem(3, 
    [[0, 1, 5], [0, 2, 6], [0, 3, 7], [1, 1, 4], [1, 2, 7], [2, 1, 5]]
)

print(movieRentingSystem.search(1))  # [1, 0, 2]
movieRentingSystem.rent(0, 1)
movieRentingSystem.rent(1, 2)
print(movieRentingSystem.report())   # [[0, 1], [1, 2]]
movieRentingSystem.drop(1, 2)
print(movieRentingSystem.search(2))  # [0, 1]
