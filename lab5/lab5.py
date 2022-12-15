#!/usr/bin/env python
# -*- coding: utf-8 -*-


# log_format ui_short '$remote_addr  $remote_user $http_x_real_ip [$time_local] "$request" '
#                     '$status $body_bytes_sent "$http_referer" '
#                     '"$http_user_agent" "$http_x_forwarded_for" "$http_X_REQUEST_ID" "$http_X_RB_USER" '
#                     '$request_time';


import re
import os
import gzip
import io

from statistics import median

config = {
    "LOG_DIR": ".\log"
}


def main():
    logs = {}
    log_names = os.listdir(config.get('LOG_DIR'))
    log_name = log_names[-1]
    parsed_line = f'{config.get("LOG_DIR")}/{log_name}'
    regex = re.compile(r'\"[A-Z]+ (\S+) .* (\d+\.\d+)\n')
    total_count = 0

    def read_log(file):
        nonlocal total_count
        for line in file:
            result = regex.findall(line)
            total_count += 1
            if not len(result):
                continue
            url, time = result[0]
            if url not in logs:
                logs[url] = []
            logs[url].append(float(time))

    if log_name.lower().endswith('.gz'):
        with gzip.open(parsed_line, 'r') as archive:
            with io.TextIOWrapper(archive, encoding='utf-8') as file:
                read_log(file)

    else:
        with open(parsed_line, 'r') as file:
            read_log(file)

    for key in logs:
        count = len(logs[key])
        print(f'URL: {key} \n'
              f'\tcount: {count}'
              f'\n\tcount_perc: {count/total_count * 100}'
              f'\n\ttime_avg: {sum(logs[key])/count}'
              f'\n\ttime_max: {max(logs[key])}'
              f'\n\ttime_median: {median(logs[key])}')
        print('\n')


main()
