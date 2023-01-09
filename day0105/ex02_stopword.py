import re

data='<div>!@#hello.</div>'
data = re.sub(r'<.+?>','',data)
data=data.replace('.','')
data=re.sub(r'[~!@#$%^&*()_+{}<>?/]+','',data)
print(data)