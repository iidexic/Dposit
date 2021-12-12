import copy as cp
class game_time:
    def __init__(self, time, clock, FPS = 60):
        self.time = time
        self.clock = clock
        self.last = self.current = self.time.get_ticks()
        self.past = []
        self.memory_frames = 10 # frame time record cap
        self.FPS = FPS
    
    def delta(self):
        return self.current - self.last
    
    def frame(self):
        self.last = cp.copy(self.current) # replace with last_update if too slow
        self.current = self.time.get_ticks()
        self.record()
        
    def endframe(self):
        self.clock.tick(self.FPS)
    def last_update(self):
        self.last = self.time.get_ticks()

    def record(self):
        self.past.insert(0,self.current)
        if len(self.past) > self.memory_frames:
            self.past.pop(self.memory_frames)
