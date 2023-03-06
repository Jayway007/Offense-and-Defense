
## Process
| scene | rule | tacnic |
|------|-----------|-------|
| dowload file from external network | name: wget, curl, rsync, ftp, sftp | Init Access, resistence |
| view sensitive information in system | cmd: tail, head, vi, cat, less, more, tac  | Collection |
| RCE from Java Application | pathlink contains java && path contains /usr/bin/ | Execution | 
| ssh trust replationship | view file: known_host and login the same ip | Lateral Movement| 


## Network
| scene | rule | tacnic |
|------|-----------|-------|
| external connecting | CTI: black ip & domain | |
| internal access | high risk open port connection | |

## Log
| scene | rule | tacnic |
|------|-----------|-------|
