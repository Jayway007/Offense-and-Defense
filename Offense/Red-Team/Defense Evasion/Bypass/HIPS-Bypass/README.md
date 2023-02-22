
## Overall
  To fight against HIDS monitoring generally starts from the following aspects:
  
- Bypass monitor technology:
  - Bypass the command monitoring method so that HIDS cannot collect the log of command execution
  - Process and parameters of command execution can be tampered with so that false logs can be collected
- Bypass Detection model/rule:
  - Guess the strategy of the command alarm and bypass it

## `Commands execute bypass`
1. *Bypass monitor technology*
- [反弹shell-逃逸基于execve的命令监控(上)](https://cloud.tencent.com/developer/article/1560417) @七夜
- [恶意命令绕过与检测](https://l0n9w4y.cc/posts/18345/)  @l0n9w4y

2. *Bypass Detection model/rule*

### Command keywords bypass
Refer to : [bypass-bash-restrictions_HackTricks](https://book.hacktricks.xyz/linux-hardening/bypass-bash-restrictions)
- Question mark
```
/usr/bin/cur?
```

- Wildcard(*)

```
/usr/bin/c*rl 
```

- [chars] 

```
/usr/bin/cur[l]
```

- Quotes

```
'c'u'r'l
cu''r''''l      #'x2
```

- Backslashes

```
\c\u\r\l
```

- $@

```
cur$@l
```

- variables

```
c$(u)ur${u}l$u
```

- Transformations (case, reverse, base64)

```
$(tr "[A-Z]" "[a-z]"<<<"CuRl") # -> Upper case to lower case
$(a="CuRL";printf %s "${a,,}") # -> transformation (only bash)
$(rev<<<'lruc') 
bash<<<$(base64 -d<<<Y2F0IC9ldGMvcGFzc3dkIHwgZ3JlcCAzMw==) #base64
```



## Tricks
- Reame the shell as normal filename : ospatch.sh /  hotfix.sh

## Reference




