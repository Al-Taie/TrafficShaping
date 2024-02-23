#!/usr/bin/python
import re
import subprocess
import time
from datetime import datetime
from threading import Thread

HOSTS_PATH = '/etc/hosts'
LOCALHOST = "127.0.0.1"


class FirewallManager:
    entries = []

    def __init__(self):
        Thread(target=self.runtime, daemon=True).start()

    def runtime(self):
        while True:
            changed = False
            current_time = datetime.now().time()
            for entry in self.entries.copy():
                if entry.start_time <= current_time <= entry.end_time:
                    # Block URL using iptables if it's not already blocked
                    if not entry.is_blocked:
                        changed = True
                        self.block(url=entry.url, start_time=entry.start_time, end_time=entry.end_time)
                elif entry.is_blocked and current_time >= entry.end_time:
                    changed = True
                    # Unblock URL using iptables if it's blocked but not in the allowed time range
                    self.unblock(url=entry.url)
            if changed:
                self.restart_network_service()
            time.sleep(30)  # Check every 30 seconds

    def block(self, url, start_time, end_time):
        current_time = datetime.now().time()
        url = self.clear_url(url)
        can_block = current_time >= start_time
        if can_block:
            with open(HOSTS_PATH, 'r+') as hosts_file:
                entry = f'{LOCALHOST} {url}\n'
                if entry not in hosts_file.readlines():
                    hosts_file.write(entry)

        self.entries.append(URLEntry(url=url, start_time=start_time, end_time=end_time, is_blocked=can_block))

    def unblock(self, url):
        url = self.clear_url(url)
        # Read the content of the hosts file
        with open(HOSTS_PATH, 'r') as hosts_file:
            lines = hosts_file.readlines()

        # Write back the content of the hosts file excluding the line with the blocked URL
        with open(HOSTS_PATH, 'w') as hosts_file:
            for line in lines:
                if not line.startswith(f'{LOCALHOST} {url}'):
                    hosts_file.write(line)

        self.entries = [entry for entry in self.entries if entry.url != url]

    @staticmethod
    def validate_url(url):
        return bool(FirewallManager.clear_url(url))

    @staticmethod
    def clear_url(url):
        regex = re.compile(r"(?:https?://)?(?:www\.)?([a-zA-Z0-9-]+\.[a-zA-Z]{2,})")
        matches = regex.search(url)
        result = matches.group(1) if matches else None
        return result

    @staticmethod
    def restart_network_service():
        process = lambda: subprocess.run(['sudo', 'systemctl', 'restart', 'networking'])
        Thread(target=process, daemon=True).start()


class URLEntry:
    def __init__(self, url, start_time, end_time, is_blocked):
        self.url = url
        self.is_blocked = is_blocked
        self.start_time = start_time
        self.end_time = end_time
