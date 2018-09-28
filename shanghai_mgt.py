# -*- coding=utf-8 -*-
import tkinter as tk
from tkinter.font import Font
import csv
import pathlib
import datetime
from tkinter.messagebox import showinfo, showerror

FILENAME = pathlib.Path('接单.csv')

# def lookup_data(form_id):
#     with open(FILENAME, 'r', encoding='gb2312') as fp:
#         reader = csv.DictReader(fp)
#         for row in reader:
#             if row['单号'] == form_id:
#                 return row
#             else:
#                 return None


def submit():
    if form_id.get() and classification.get() and team.get() and (
            create_datetime_1.get() or create_datetime_2.get()
            or create_datetime_3.get()):
        create_datetime = ' '.join([
            create_datetime_1,
            create_datetime_2,
            create_datetime_3,
        ])
        if not FILENAME.exists():
            with open(FILENAME, 'w', encoding='gb2312', newline='') as fp:
                fieldnames = ['单号', '联系时间', '案件类别', '所属小队']
                writer = csv.DictWriter(fp, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerow({
                    '单号': form_id.get(),
                    '联系时间': create_datetime,
                    '案件类别': classification.get(),
                    '所属小队': team.get()
                })
        else:
            with open(FILENAME, 'a', encoding='gb2312', newline='') as fp:
                fieldnames = ['单号', '联系时间', '案件类别', '所属小队']
                writer = csv.DictWriter(fp, fieldnames=fieldnames)
                writer.writerow({
                    '单号': form_id.get(),
                    '联系时间': create_datetime,
                    '案件类别': classification.get(),
                    '所属小队': team.get()
                })
        # id_history.insert(tk.END, form_id.get())
        showinfo('提交信息', '已经提交!')
        print(form_id.get(), create_datetime.get(), classification.get(),
              team.get())
    else:
        miss_obj = [
            k for k, v in {
                '单号': form_id.get(),
                '联系时间': create_datetime.get(),
                '案件类别': classification.get(),
                '所属小队': team.get()
            }.items() if not v
        ]
        err_msg = ','.join(miss_obj)
        showerror('错误', err_msg + '没有填写。')


def now():
    if not create_datetime_1.get():
        create_datetime_1.set(datetime.datetime.now().strftime("%F %H:%M"))
    elif not create_datetime_2.get():
        create_datetime_2.set(datetime.datetime.now().strftime("%F %H:%M"))
    elif not create_datetime_3.get():
        create_datetime_3.set(datetime.datetime.now().strftime("%F %H:%M"))


def about():
    showinfo(
        '关于', """
        版      本:  0.3 Beta
        作      者:  好心人
        联系方式:  不能告诉你
        """)


# def select_history_id(event):
#     w = event.widget
#     index = w.curselection()[0]
#     print(index)
#     value = w.get(index)
#     form_id.set(value)

# def del_history_id():
#     index = id_history.curselection()[0]
#     if index:
#         id_history.delete(index)

root = tk.Tk()
root.title('接单')
root.geometry('718x520')
# 字体
ft = Font(size=16)
root.option_add("*Font", ft)
# 菜单栏Menu
menubar = tk.Menu(root)
menubar.add_command(label='关于', command=about)
root['menu'] = menubar

left1_fr = tk.LabelFrame(root, text='案件信息', width=432, heigh=162)
left1_fr.grid(row=0, column=0, padx=15, sticky=tk.W)
tk.Label(left1_fr, text="单号:").place(x=5, y=5)
form_id = tk.StringVar()
form_id_entry = tk.Entry(left1_fr, textvariable=form_id)
form_id_entry.place(x=108, y=5)
called_times = tk.StringVar()
called_times_label = tk.Label(left1_fr, textvariable=called_times)
called_times_label.place(x=340, y=6)
tk.Label(left1_fr, text="联系时间:").place(x=5, y=38)
create_datetime_1 = tk.StringVar()
create_datetime_2 = tk.StringVar()
create_datetime_3 = tk.StringVar()
tk.Entry(left1_fr, textvariable=create_datetime_1).place(x=108, y=38)
tk.Entry(left1_fr, textvariable=create_datetime_2).place(x=108, y=71)
tk.Entry(left1_fr, textvariable=create_datetime_3).place(x=108, y=104)
tk.Button(left1_fr, text='现在', command=now).place(x=340, y=33)

left2_fr = tk.LabelFrame(root, text='案件类别', width=432, heigh=165)
left2_fr.grid(row=1, column=0, padx=15, sticky=tk.W)
classification = tk.StringVar()
classification_list = tk.Radiobutton(
    left2_fr, text='乱设摊', variable=classification, value='乱设摊').place(
        x=5, y=5)
classification_list = tk.Radiobutton(
    left2_fr, text='跨门经营', variable=classification, value='跨门经营').place(
        x=135, y=5)
classification_list = tk.Radiobutton(
    left2_fr, text='损毁承重结构', variable=classification, value='损毁承重结构').place(
        x=270, y=5)
classification_list = tk.Radiobutton(
    left2_fr, text='居改非', variable=classification, value='居改非').place(
        x=5, y=38)
classification_list = tk.Radiobutton(
    left2_fr, text='夜间施工', variable=classification, value='夜间施工').place(
        x=135, y=38)
classification_list = tk.Radiobutton(
    left2_fr, text='占绿毁绿', variable=classification, value='占绿毁绿').place(
        x=270, y=38)
classification_list = tk.Radiobutton(
    left2_fr, text='广告设施', variable=classification, value='广告设施').place(
        x=5, y=71)
classification_list = tk.Radiobutton(
    left2_fr, text='油烟', variable=classification, value='油烟').place(
        x=135, y=71)
classification_list = tk.Radiobutton(
    left2_fr, text='出租车类', variable=classification, value='出租车类').place(
        x=270, y=71)
classification_list = tk.Radiobutton(
    left2_fr, text='非法客运类', variable=classification, value='非法客运类').place(
        x=5, y=104)
classification_list = tk.Radiobutton(
    left2_fr, text='其他', variable=classification, value='其他').place(
        x=135, y=104)

left3_fr = tk.LabelFrame(root, text='所属小队', width=432, heigh=135)
left3_fr.grid(row=2, column=0, padx=15, sticky=tk.W)
team = tk.StringVar()
team_list = tk.Radiobutton(
    left3_fr, text='一小队', variable=team, value='一小队').place(
        x=5, y=5)
team_list = tk.Radiobutton(
    left3_fr, text='二小队', variable=team, value='二小队').place(
        x=135, y=5)
team_list = tk.Radiobutton(
    left3_fr, text='三小队', variable=team, value='三小队').place(
        x=270, y=5)
team_list = tk.Radiobutton(
    left3_fr, text='四小队', variable=team, value='四小队').place(
        x=5, y=38)
team_list = tk.Radiobutton(
    left3_fr, text='机动队', variable=team, value='机动队').place(
        x=135, y=38)
team_list = tk.Radiobutton(
    left3_fr, text='保安处置', variable=team, value='保安处置').place(
        x=270, y=38)
team_list = tk.Radiobutton(
    left3_fr, text='退单', variable=team, value='退单').place(
        x=5, y=71)

# right_fr = tk.LabelFrame(root, text='历史单号', width=240, heigh=376)
# right_up_fr = tk.Frame(right_fr)
# right_up_fr.pack()
# scrollbar = tk.Scrollbar(right_up_fr, orient=tk.VERTICAL)
# id_history = tk.Listbox(right_up_fr, heigh=16, yscrollcommand=scrollbar.set)
# scrollbar.config(command=id_history.yview)
# scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
# id_history.bind("<Double-Button-1>", select_history_id)
# id_history.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
# right_down_fr = tk.Frame(right_fr)
# right_down_fr.pack()
# tk.Button(right_down_fr, text="删除", command=del_history_id).pack()

left4_fr = tk.Frame(root)
left4_fr.grid(row=3, column=0, padx=15, pady=10)
tk.Button(left4_fr, text='提交', command=submit).grid(row=0, column=0)

root.mainloop()
