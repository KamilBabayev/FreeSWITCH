#!/usr/bin/env python3

import os
import re
from sys import argv, exit
from datetime import datetime


class FSLogParser():

    def __init__(self):
        self.check_date_format()
        self.log_file = ''
        self.fs_log_path = '/var/log/freeswitch'
        self.matched_lines = []
        self.target_day_log_files = []
        self.fs_hangup_codes = {
                                'unallocated':      '[UNALLOCATED_NUMBER]',
                                'dest_out_of_ord':  '[DESTINATION_OUT_OF_ORDER]',
                                'interworking':     '[INTERWORKING]',
                                'normal_temp_fail': '[NORMAL_TEMPORARY_FAILURE]',
                                'normal_unspec':    '[NORMAL_UNSPECIFIED]',
                                'no_user_resp':     '[NO_USER_RESPONSE]',
                                'no_answer':        '[NO_ANSWER]',
                                'user_busy':        '[USER_BUSY]',
                                'net_out_of_ord':   '[NETWORK_OUT_OF_ORDER]',
                                'inv_num_format':   '[INVALID_NUMBER_FORMAT]',
                                'no_route_dest':    '[NO_ROUTE_DESTINATION]',
                                'nor_crct_cngst':   '[NORMAL_CIRCUIT_CONGESTION]',
                                'subs_absent':      '[SUBSCRIBER_ABSENT]',
                                'call_rejected':    '[CALL_REJECTED]',
                                'orig_cancel':      '[ORIGINATOR_CANCEL]'
                               }


    def check_date_format(self):

        if len(argv) < 2:
            raise TypeError("Please pass date as argument in yyyy-mm-dd format")
        #elif not re.match(r'\d{4}-\d{2}-\d{2}', argv[1]):
        elif not re.match(r'(?:(?<!\d)\d{4}-\d{2}-\d{2}(?!\d))', argv[1]):
            raise TypeError("Incorrect date format. It should be yyyy-mm-dd")
        else:
            self.day = argv[1]


    def find_fs_log_files_to_process(self):
        """Interesting day relayed entries can be also in rotated log files
        so we will find that files first and will read only those for parsing.
        """
        for p, d, f  in os.walk(self.fs_log_path):
            if p == self.fs_log_path and 'freeswitch.log' in f:
                files = f

        [files.remove(fname) for fname in files if not 'freeswitch.log' in fname]
        self.files = [self.fs_log_path + "/" +  f for f in files]
        self.files.sort(key=lambda x: os.path.getmtime(x))

        return self.files


    def find_log_files_containing_target_day(self):
        self.fs_log_files = self.find_fs_log_files_to_process()

        for filename in self.fs_log_files:
            with open(filename) as log_file:
                for line in log_file:
                    line = line.rstrip("\n")
                    if self.day in line:
                        if 'switch_cpp' in line:
                            continue
                        self.target_day_log_files.append(filename)
                        break

        return self.target_day_log_files


    def parse_fs_log(self):
        self.log_files = self.find_log_files_containing_target_day()

        for code in self.fs_hangup_codes:
            fs_hangup_code = '[CS_CONSUME_MEDIA]' + ' ' + self.fs_hangup_codes[code]
            #self.matched_lines = []
            self.matched_lines.append("====== " + self.fs_hangup_codes[code] + " =====\n")

            for filename in self.log_files:
                with open(filename) as log_file:
                    for line in log_file:
                        line = line.rstrip("\n")
                        if self.day in line and fs_hangup_code in line:
                            if 'switch_cpp' in line:
                                continue
                            line = line.split()
                            profile = line[6].split('/')[1]
                            number = line[6].split('/')[2]

                            self.matched_lines.append(line[1] + " " + line[2] + " " + line[8]
                                                  + " " + str(profile) + " " + str(number))


            self.matched_lines.append("--------------------------------------------\n\n")


    def generate_calls_report(self):
        self.report_file = f'/tmp/fs_calls_report-{self.day}.txt'

        if os.path.exists(self.report_file):
            os.remove(self.report_file)

        with open(self.report_file,'a+') as report_file:
            for line in self.matched_lines:
                line = line + "\n"
                report_file.write(line)


    def generate_call_stats(self):
        """Count calls per each hangup_code and all calls.
           Form percentage of calls based nums.
        """
        self.all_calls = {}
        self.all_calls['ALL CALLS: '] = len(self.matched_lines)
        call_data = str(self.matched_lines)

        for item in self.fs_hangup_codes:
            code = self.fs_hangup_codes[item].lstrip('[').rstrip(']')
            code_count = call_data.count(code)
            self.all_calls[code] = code_count

        with open(self.report_file, 'a+') as report_file:
            report_file.write("=======  CALL STATS: =========\n\n")
            for k,v in self.all_calls.items():
                line = str(k) + ": " + str(v) + "\n"
                report_file.write(line)
            report_file.write("\n")



if __name__ == '__main__':
    report = FSLogParser()
    report.parse_fs_log()
    report.generate_calls_report()
    report.generate_call_stats()
