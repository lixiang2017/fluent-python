
import os 
from pprint import pprint 
import sys

print(sys.executable)
# print(os.environ)
pprint(dict(os.environ))

print(sys.platform)

'''
/Library/Frameworks/Python.framework/Versions/3.9/bin/python3
{'HOME': '/Users/xiangli',
 'LC_CTYPE': 'UTF-8',
 'LOGNAME': 'xiangli',
 'OLDPWD': '/',
 'PATH': '/Library/Frameworks/Python.framework/Versions/3.9/bin:/Library/Frameworks/Python.framework/Versions/3.8/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/Cellar:/Applications/VMware '
         'Fusion.app/Contents/Public:/usr/local/go/bin:/usr/local/MacGPG2/bin:/Applications/Wireshark.app/Contents/MacOS',
 'PYTHONIOENCODING': 'utf-8',
 'SHELL': '/bin/zsh',
 'SSH_AUTH_SOCK': '/private/tmp/com.apple.launchd.U15wuS0agf/Listeners',
 'SSL_CERT_FILE': '/Applications/Sublime '
                  'Text.app/Contents/MacOS/Lib/python3/certifi/cacert.pem',
 'TMPDIR': '/var/folders/0s/w75vmqvx2ygfqmsrnv93phmr0000gn/T/',
 'USER': 'xiangli',
 'XPC_FLAGS': '0x0',
 'XPC_SERVICE_NAME': '0',
 '__CF_USER_TEXT_ENCODING': '0x1F5:0x0:0x0'}
[Finished in 47ms]
darwin
'''
