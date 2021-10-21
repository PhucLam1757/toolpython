import re
from sre_constants import RANGE_UNI_IGNORE
content = '''nhật ký vàng anh
hôm nay là một ngày đẹp trời, mình đi ra ngoài và gặp anh Lâm đẹp trai
và sau đó mình cũng gặp được anh X đẹp trai'''
handler = re.compile(r"anh (.*?) đẹp")
result = handler.findall(content)
a = ""
print(a.join(result[0]).join(result[1]))