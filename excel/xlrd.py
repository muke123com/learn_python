import xlrd
import xlwt


# 读Excel
def read_excel():
    workbook = xlrd.open_workbook(r'C:\Users\Administrator\Desktop\py1.xlsx')

    sheet1_name = workbook.sheet_names()[0]

    sheet1 = workbook.sheet_by_index(0)

    print(sheet1.name, sheet1.nrows, sheet1.ncols)

    # 获取整行整列的值
    for i in range(sheet1.nrows):
        rows = sheet1.row_values(i)
        print(rows)

    # cols = sheet1.col_values(0)
    # print(cols)

    # 获取单元格内容
    print(sheet1.cell(0, 0).value)

    # 获取单元格内容的数据类型
    print(sheet1.cell(0, 0).ctype)

    pass


# 写Excel
def set_style():
    style = xlwt.XFStyle()
    font = xlwt.Font()
    font.name = "微软雅黑"
    font.bold = True
    font.colour_index = 0
    font.height = 220
    style.font = font

    return style
    pass


def write_excel():
    url = r'C:\Users\Administrator\Desktop\py1.xlsx'
    workbook = xlwt.Workbook()  # 创建工作簿
    sheet = workbook.add_sheet('s1', cell_overwrite_ok=True)
    row0 = [u'业务', u'状态', u'北京', u'上海', u'广州', u'深圳', u'状态小计', u'合计']
    colum0 = [u'机票', u'船票', u'火车票', u'汽车票', u'其它']
    status = [u'预订', u'出票', u'退票', u'业务小计']

    # 生成第一行
    for i in range(1, 10):
        for j in range(1, 10):
            text = str(i) + '*' + str(j) + '=' + str(i*j)
            sheet.write(i-1, j-1, text, set_style())
            pass

    workbook.save('demo1.xls')
    pass


if __name__ == '__main__':
    write_excel()
