import time

import watchdog.events
import watchdog.observers


TRACKING_FOLDER = "/Users/adrianchong/Downloads"


class EventHandler(watchdog.events.FileSystemEventHandler):
    def on_created(self, event):
        print(f"Created: {event.src_path}")

    def on_deleted(self, event):
        print(f"Deleted: {event.src_path}")

    def on_modified(self, event):
        print(f"Modifed: {event.src_path}")

    def on_moved(self, event):
        print(f"Moved  : {event.src_path} -> {event.dest_path}")


def main():
    eventHander = EventHandler()
    observer = watchdog.observers.Observer()
    observer.schedule(eventHander, TRACKING_FOLDER, recursive=True)

    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        observer.join()


if __name__ == "__main__":
    main()
