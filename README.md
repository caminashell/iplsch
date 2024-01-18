# iplsch

IP Address List Checker

I was installing UFW on Debian and looking into IP Blocking lists.
Since I already use a well-maintained list, I thought I would compare
it to what I had come across from a UFW source.

For now, you'll need two files for the script to process;

1. `base.txt` - The file that contains your current IP Block list.
2. `test.txt` - The file containing another list of IP addresses to block.

It will print out a list of all the IP Addresses that are missing from your
control (base) file.

Example:

```log
Missing: 192.168.1.0
Missing: 192.168.1.1
Missing: 192.168.1.2
Missing: 192.168.1.3
```

Run this script alongside your list files with;

```bash
python iplsch.py
```

-- or --

```sh
python3 iplsch.py
```
