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
