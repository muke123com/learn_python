import pdfkit

# pdfkit.from_file('./1.html', 'out.pdf')
pdfkit.from_url('http://baidu.com', 'out.pdf')