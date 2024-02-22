#!/usr/bin/python
import re
import time
from datetime import datetime
from threading import Thread


class FirewallManager:
    entries = []

    def __init__(self):
        Thread(target=self.runtime, daemon=True).start()

    def runtime(self):
        while True:
            current_time = datetime.now().time()
            for entry in self.entries:
                if entry.start_time <= current_time <= entry.end_time:
                    # Block URL using iptables if it's not already blocked
                    self.block(url=entry.url, start_time=entry.start_time, end_time=entry.end_time)
                else:
                    # Unblock URL using iptables if it's blocked but not in the allowed time range
                    self.unblock(url=entry.url)
            time.sleep(30)  # Check every 30 seconds

    def block(self, url, start_time, end_time):
        url = self.clear_url(url)
        with open('/etc/hosts', 'r+') as hosts_file:
            entry = f'127.0.0.1 {url}\n'
            if entry not in hosts_file.readlines():
                hosts_file.write(entry)

        self.entries.append(URLEntry(url=url, start_time=start_time, end_time=end_time))

    def unblock(self, url):
        url = self.clear_url(url)
        # Read the content of the hosts file
        with open('/etc/hosts', 'r') as hosts_file:
            lines = hosts_file.readlines()

        # Write back the content of the hosts file excluding the line with the blocked URL
        with open('/etc/hosts', 'w') as hosts_file:
            for line in lines:
                if not line.startswith(f'127.0.0.1 {url}'):
                    hosts_file.write(line)

        self.entries = [entry for entry in self.entries if entry.url != url]

    @staticmethod
    def clear_url(url):
        pattern = r"(?:https?://)?([A-Za-z0-9\.]+)/?"
        regex = re.compile(pattern)
        matches = regex.search(url)
        result = matches.group(1)
        return result


class URLEntry:
    def __init__(self, url, start_time, end_time):
        self.url = url
        self.start_time = start_time
        self.end_time = end_time
