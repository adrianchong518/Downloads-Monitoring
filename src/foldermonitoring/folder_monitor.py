import watchdog.observers


class FolderMonitor:
    def __init__(self, folderToTrack, eventHandler):
        self.observer = watchdog.observers.Observer()
        self.observer.schedule(eventHandler, folderToTrack, recursive=True)

    def start(self):
      self.observer.start()

    def stop(self):
      self.observer.stop()
      self.observer.join()
