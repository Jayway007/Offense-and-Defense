# Protocol Tunneling([T1572](https://attack.mitre.org/techniques/T1572/))
## DNS 
  - DNS over HTTPS
## HTTPS
## SSH
- [Mapping a intranet port to internet with SSH](https://blog.csdn.net/Hezhoutheone/article/details/123113020)
 ```bash
 $ ssh -f -N -R 16666:172.18.128.150:80 ubuntu@106.52.XX.XX
 ```
- [Create a SOCKS proxy on a Linux server with SSH to bypass content filters](https://ma.ttias.be/socks-proxy-linux-ssh-bypass-content-filters/#set-up-socks5-ssh-tunnel)
```bash
$ ssh -D 1337 -q -C -N -f user@ma.ttias.be
```
 
 ![](https://ma.ttias.be/wp-content/uploads/2017/01/ssh_socks5_proxy_linux.png)
- RDP
- SOCKS5
