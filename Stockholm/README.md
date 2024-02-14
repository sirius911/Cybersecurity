#Stockholm

This program encrypts all files in a home/infection directory with the .WCRY extension, a reference to the Wannacry malware (https://fr.wikipedia.org/wiki/WannaCry).

### Program arguments and options :

```usage: stockholm.py [-h] [-v] [-r REVERSE] [-s] [--all-files] [-k key]

stockholm : cryptolocker virus which encrypts files $HOME/infection.

options:
  -h, --help            show this help message and exit
  -v, --version         Show version of the program.
  -r REVERSE, --reverse REVERSE
                        Reverse the infection using the provided encryption key.
  -s, --silent          Silent mode, no output
  --all-files           All files will be encrypted !!
  -k key, --key key     Length of the encryption key. Choose between 16 or 32 (default: 16)
  ```

  ### modules required and installation :

```
colorama==0.4.4
pycryptodome==3.20.0
```

```bash
pip install -r requirements.txt
```

---
This project is for educational purposes only. You should never use
this type of program for malicious purposes.