import threading

from UI.app import draw_app
from data.eventdata import EventData
from input_events.input_events import mouse_event_listener
from updater.updater import TimerUpdater


def main():
    timer_updater = TimerUpdater()

    event_data = EventData()

    event_data.loadData()
    event_data.writeMouseEvent()

    # t1 = threading.Thread(target=mouse_event_listener, args=[timer_updater], daemon=True)
    # t1.start()

    draw_app(timer_updater)


main()
