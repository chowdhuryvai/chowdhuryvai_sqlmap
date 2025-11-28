# chowdhuryvai_sqlmap
Chowdhury-vai Sqlmap Automate Use tools



(![image](https://i.postimg.cc/Fzs9g3md/2025-11-28-134850.png)


```bash
git clone https://github.com/chowdhuryvai/chowdhuryvai_sqlmap.git
cd chowdhuryvai_sqlmap
chmod +x chowdhuryvaisqlmap.py
```



```bash
# Install required dependencies:
pip install sqlmap
# Usage Examples:
# Basic scan: 
python3 chowdhuryvai_sqlmap.py http://example.com/page.php?id=1
# Advanced scan with options: 
python3 chowdhuryvai_sqlmap.py http://example.com/page.php?id=1" -r 2 -l 3 -t 5 --tor
# Google dork search: 
python3 chowdhuryvai_sqlmap.py -g inurl:index.php?id=
# Interactive mode: 
python3 chowdhuryvai_sqlmap.py --interactive
# Show version: 
python3 chowdhuryvai_sqlmap.py -v
```
