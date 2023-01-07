# FreeSWITCH

Usage of fs_call_report.
```
python3 reporter.py 2022-12-22
```

Generates file in /tmp folder with current date suffix.
Report will contain entry for each call and also summary at the end.

```
cat /tmp/fs_calls_report-2022-12-22.txt  | tail -30

... redacted

=======  CALL STATS: =========

ALL CALLS: : 9923
UNALLOCATED_NUMBER: 923
DESTINATION_OUT_OF_ORDER: 100
INTERWORKING: 245
NORMAL_TEMPORARY_FAILURE: 740
NORMAL_UNSPECIFIED: 5275
NO_USER_RESPONSE: 349
NO_ANSWER: 1594
USER_BUSY: 361
NETWORK_OUT_OF_ORDER: 104
INVALID_NUMBER_FORMAT: 16
NO_ROUTE_DESTINATION: 3
NORMAL_CIRCUIT_CONGESTION: 15
SUBSCRIBER_ABSENT: 34
CALL_REJECTED: 15
ORIGINATOR_CANCEL: 134
```
