#Thread

from threading import Thread as th_Thread, Event as th_Event

__all__ = ["Thread"]

class Thread:
    def __init__(self, target:function, *args, **kwargs):
        self.newtarget(target, *args, **kwargs)
        
    def _generate_thread(self):
        return th_Thread(target=self._thread["TARGET"], args=self._thread["ARGS"], kwargs=self._thread["KWARGS"], daemon=True)
        
    def newtarget(self, target:function, *args, **kwargs):
        self._thread = {
            "TARGET": target,
            "ARGS": args,
            "KWARGS": kwargs,
            "THREAD": None,
            "STOP": th_Event()
        }
        self._thread["THREAD"] = self._generate_thread()
    
    def start(self):
        self._thread["THREAD"].start()
    
    def join(self):
        self._thread["THREAD"].join()
    
    def regenthread(self):
        self._thread["THREAD"] = self._generate_thread()