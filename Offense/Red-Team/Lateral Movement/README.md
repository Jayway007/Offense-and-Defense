# Point:
*Loop Attack* ： Based on the new environment to redirect, discover and collection, finding new weakness to transfer to the next one

- Discovery
  - SSH
    - known_hosts: logged
    - .ssh/
      - authorized_keys
      - id_rsa
  - .bash_history
    - plaintext password
  - configure
    - /WEB-INF
  - ciphertext
    - reverse and decrypt
  - private key
    - scenes : login
    
    
- service exploit
  - Brute force : SSH, FTP, Mysql
  - Unauthorization Access : Redis, Mongodb, Etcd, Rsync, Kafka, Zookeper, Docker, Hadoop, NFS
    - socket coding : automation write ssh key by redis
  - other netstat information
  
