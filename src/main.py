import time

import watchdog.events

from foldermonitoring.folder_monitor import FolderMonitor


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
    folderMonitor = FolderMonitor(TRACKING_FOLDER, EventHandler())

    folderMonitor.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        folderMonitor.stop()


if __name__ == "__main__":
    main()
