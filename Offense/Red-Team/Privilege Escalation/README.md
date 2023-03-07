The adversary is trying to gain higher-level permissions.

## Abuse Elevation Control Mechanism([T1548](https://attack.mitre.org/techniques/T1548/))
### 1.Setuid and Setgid
   SUID is a special file permission for executable files which enables other users to run the file with effective permissions of the file owner. Instead of the normal x which represents execute permissions, you will see an s (to indicate SUID) special permission for the user.
  ```bash
   find / -perm -u=s -type f 2>/dev/null
  ```
  - [谈一谈Linux与suid提权](https://www.leavesongs.com/PENETRATION/linux-suid-privilege-escalation.html)  @Phith0n
### 2.Sudo
- Soft link
  Linux chown(change owner) is a command used to set the owner of a file.
  - Low privilege user can execute a script as root, and the script uses chown command to modify the privilege of another file, which can be modified by low-privilege user.So that the user can delete the file and create a same-name file, which link to a high-privilege user, such as /etc/passwd.
### 3.Bypass User Account Control(UAC)
### 4.Crontab
   The file that executed by crontab can be modified by a normal user.
   
   
## [Event_Triggered_Execution](https://github.com/Jayway007/Offense-and-Deffense/blob/main/Offense/Red-Team/Persistence/Event_Triggered_Execution.md)


- Kernel Exploit
- [Next-Generation Linux Kernel Exploit Suggester](https://github.com/jondonas/linux-exploit-suggester-2)
