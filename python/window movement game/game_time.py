import copy as cp

class game_time:
    def __init__(self, clock):
        self.clock = clock
        self.last = self.current = self.clock.get_ticks()
        self.past = []
        self.memory_frames = 10 # frame time record cap
    
    def delta(self):
        return self.current - self.last
    
    def frame(self):
        self.last = cp.copy(self.current) # replace with last_update if too slow
        self.current = self.clock.get_ticks()
    
    def last_update(self):
        self.last = self.clock.get_ticks()

    def record(self):
        self.past.insert(0,self.current)
        if len(self.past) > self.memory_frames:
            self.past.pop(self.memory_frames)
