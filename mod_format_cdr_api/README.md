# Simple api will be started to accept posted cdr json data from freeswitch side


tool.sh will build and run container
```
server:~# bash tool.sh
Successfully built 52c83bfc84ea
Successfully tagged demo_cdr_web_api:latest
c49f7ce8c1bda629835bc158a0d9d44baacfa1f946a66dc91298def0ee775099
 * Serving Flask app 'main'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://172.17.0.2:5000
Press CTRL+C to quit
uuid:  616ad3ed-dffe-4d31-9638-85a961718ea6
sip_from_user:  555555555
domain_name: " c2sipsystem.demo.lab
tenant_id:  2
start_stamp:  2023-01-07 16:04:42
profile_start_stamp:  2023-01-07 16:04:42
answer_stamp: : missing
progress_media_stamp: : missing
end_stamp:  2023-01-07 16:04:52
start_epoch:  1673093082
profile_start_epoch:  1673093082
answer_epoch:  0
progress_media_epoch:  0
end_epoch:  1673093092
duration:  10
billsec:  0

```



We can see cdr datas in logs also. But this is only filtered and some part of cdr
```
server:~# docker logs -f demo_api

10.50.36.25 - - [07/Jan/2023 12:07:14] "POST /cdr?uuid=a_89939633-f8ba-464a-9e52-84921085df3a HTTP/1.1" 200 -
uuid:  518c0621-9485-46be-9316-e27f65689877
sip_from_user:  555558517
domain_name: " c93flexy.atl.az
tenant_id:  93
start_stamp:  2023-01-07 16:07:02
profile_start_stamp:  2023-01-07 16:07:14
answer_stamp:  2023-01-07 16:07:04
progress_media_stamp:  2023-01-07 16:07:03
end_stamp:  2023-01-07 16:07:25
start_epoch:  1673093222
profile_start_epoch:  1673093234
answer_epoch:  1673093224
progress_media_epoch:  1673093223
end_epoch:  1673093245
duration:  23
billsec:  21
```

**cdr.txt** in current dir will contains full cdr data
```
FULL CDR:

state: CS_REPORTING
direction: inbound
state_number: 11
flags: 0=1;1=1;3=1;38=1;39=1;41=1;44=1;54=1;76=1;96=1;113=1;114=1;123=1;160=1;165=1;166=1
caps: 1=1;2=1;3=1;4=1;5=1;6=1;8=1;9=1
audio: {'inbound': {'raw_bytes': 96492, 'media_bytes': 91504, 'packet_count': 561, 'media_packet_count': 532, 'skip_packet_count': 7, 'jitter_packet_count': 0, 'dtmf_packet_count': 0, 'cng_packet_count': 0, 'flush_packet_count': 29, 'largest_jb_size': 0, 'jitter_min_variance': 0, 'jitter_max_variance': 0, 'jitter_loss_rate': 0, 'jitter_burst_rate': 0, 'mean_interval': 20, 'flaw_total': 0, 'quality_percentage': 100, 'mos': 4.5}, 'outbound': {'raw_bytes': 85828, 'media_bytes': 85828, 'packet_count': 499, 'media_packet_count': 499, 'skip_packet_count': 0, 'dtmf_packet_count': 0, 'cng_packet_count': 0, 'rtcp_packet_count': 0, 'rtcp_octet_count': 0}}
direction: inbound
uuid: 7937b887-2ae3-4e24-9a75-d81a04947458
session_id: 4224
sip_from_params: user=phone
sip_from_user: 5555555555
sip_from_port: 51006
sip_from_uri: 55555555@sipprovider.lab:51006
sip_from_host: sipprovider.lab
video_media_flow: disabled
text_media_flow: disabled
channel_name: sofia/sipprovider/5555555555@sipprovider.lab:51006
sip_local_network_addr: local-address
sip_network_ip: local_adderss
sip_network_port: 5060
sip_invite_stamp: 1673093466801141
sip_received_ip: local-address
sip_received_port: 5060
sip_via_protocol: udp
sip_from_user_stripped: 555555555
sofia_profile_name: azintelecom
sofia_profile_url: sip:mod_sofia@local-address:4959
recovery_profile_name: sipprovider
sip_P-Asserted-Identity: 555555555
sip_cid_type: pid
sip_allow: INVITE, BYE, REGISTER, ACK, OPTIONS, CANCEL, SUBSCRIBE, NOTIFY, PRACK, INFO, REFER, UPDATE, PUBLISH, MESSAGE
sip_req_params: user=phone;transport=udp

< redacted >
```

storing data in SQLite or or DB can be added for more serious impementation

P.S. This was developed quickly for cdr posts debugging without refactoring.
