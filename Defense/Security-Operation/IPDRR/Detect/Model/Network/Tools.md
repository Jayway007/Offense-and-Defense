# Netcat
Netcat (or nc) is a command-line utility that reads and writes data across network connections, using the TCP or UDP protocols.
## arg
- -l : listen mode, inbound connects
- -u : UDP mode
- -p port : Specify the local port for remote connections
- -n : suppress name/port resolutions
- -v : verbose, detailed

# Curl
```bash
curl https://xx.com/v1/api  \
-X POST  \
-H "Content-Type: application/json" \
-H "Authorization: Bearer xxx" \
-d '{"input": "Sample text goes here"}'
```

```bash
```bash
curl https://xx.com/v1/api  \
-F 'key=@/path/to/file'
--form file=@/path/to/file
```
```
