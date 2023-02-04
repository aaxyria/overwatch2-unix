#!/usr/bin/env python3

from sys import exit
from time import sleep, time
from typing import Optional

import psutil
from pypresence import Presence

# The client ID for a Discord application. This is the client identification number for a
# verified Overwatch 2 game. You can find this number by either searching for a verified Discord
# games list on Google, or by ripping it from someone that is already playing Overwatch 2 by using
# the inspect element tool in your browser.
client_id = "356875221078245376"

# The interval between application polls. This is the amount of time in seconds that the
# application will wait before polling the game again. This is to prevent this to be still opened
# after the game is closed.
poll_interval = 5

# The maximum value for a tick delta. This is the maximum amount of time in seconds that the
# application will tick before resetting the tick delta. This is to prevent the tick delta from
# overflowing.
max_tick_delta = 10

# Attempts to initialize a RPC connection to Discord.
def connect() -> Optional[Presence]:
    rpc = Presence(client_id)
    try:
        rpc.connect()
        rpc.update(start=int(time()))
        return rpc
    except:
        return None


# Return whether the Overwatch 2 process is running.
def is_running() -> bool:
    return any("Overwatch.exe" in p.name() for p in psutil.process_iter())


# The loop that will poll the game for status updates.
def loop(app: Presence, is_running_: bool, delta: int):
    delta = 0 if delta > max_tick_delta else delta
    exceeded_time_limit = delta > 2 and not is_running_
    if exceeded_time_limit:
        app.clear()
        app.close()
        print("Overwatch 2 has been closed.")
        return exit(0)
    sleep(poll_interval)
    return loop(app, is_running(), delta + 1)


# Wait for the Overwatch 2 process to start in order to initialize the loop.
def wait_for_process():
    while not is_running():
        print("Waiting for Overwatch 2 to be opened...")
        sleep(poll_interval)
    connection = connect()
    if connection is None:
        print("Failed to connect to Discord. Please make sure that Discord is running.")
    else:
        print("Connected to Discord.")
        loop(connection, True, 0)


if __name__ == "__main__":
    wait_for_process()
