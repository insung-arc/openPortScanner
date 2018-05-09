## openPortScanner
사이트의 링크 혹은 IP address로 포트를 스캔 하는 방식이다.

## Requirements
<ul>
  <li><a href="www.python.org">[Python]</a></li>
  <li><a href="www.nmap.org">[Nmap]</a></li>
</ul>

별거 없이 간단하게 되어 있다. Nmap 스캐너 같은 경우에는 반드시 GUI 어플을 설치할 필요가 없다. </br>
간단히 터미널에다가 **pip install nmap** 라고 입력을 하면
```
~ $ pip install nmap
Collecting nmap
  Downloading https://files.pythonhosted.org/packages/33/65/1bb09cc9532e75d84890d2b3c96be812fd6076fbc3c8ed4e5531abd4898f/nmap-0.0.1.tar.gz
Building wheels for collected packages: nmap
  Running setup.py bdist_wheel for nmap ... done
  Stored in directory: /Users/Bahk_InSung/Library/Caches/pip/wheels/e9/e9/70/115b4091d085a311723addc72f19aedeb6098757ddc32d5bc1
Successfully built nmap
Installing collected packages: nmap
Successfully installed nmap-0.0.1
~ $
```
위와 같이 설치가 된다.
## Qucik Start
```
~ $ python openPort.py

::::::::::::::::::::::::::::::
******PLEASE DO NOT WIRTE 'http://' OR 'https://'*****
Write IP address >>> www.google.com
('www.google.com', '172.217.25.196')
::::::::::::::::::::::::::::::
Please enter your Computer Password

Password:
===> Successfully Login...
===> Start Scanning...

Starting Nmap 7.60 ( https://nmap.org ) at 2018-05-09 17:19 KST
Nmap scan report for nrt12s13-in-f196.1e100.net (172.217.25.196)
Host is up (0.035s latency).
Not shown: 998 filtered ports
Some closed ports may be reported as filtered due to --defeat-rst-ratelimit
PORT    STATE SERVICE
80/tcp  open  http
443/tcp open  https

Nmap done: 1 IP address (1 host up) scanned in 4.81 seconds
```

## Thank you
**Contect me**

If you have problem about this code, then contect me. </br>
Email : insung.park123@gmail.com  </br>
Facebook : https://www.facebook.com/insung.bahk </br>

If you want to give me some money..Please send here! </br>
Bitcoin : 17qKUu57aUBcvx9T1ea8Ga87EPnDdmwAEP </br>
Ether : 0xdFE8D1536deE8F839Ede7c1f3A0c44116287D931 </br>
Bitcoin Cash : qp90gf09r3y3h06czmtnsfhz9w7s90se4s72vd9pam </br>

</br>
🙇‍♀️👾🤩Thank you! 🤩👾🙇‍♂️

