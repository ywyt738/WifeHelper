import datetime
import pathlib

import PySimpleGUI as sg

FILENAME = pathlib.Path('接单.csv')
sg.SetOptions(font=14)

layout = [
    [
        sg.Frame(
            "案件信息",
            [
                [sg.Text("单号:", size=(9, 1)), sg.Input("id", key="id")],
                [sg.Text("联系时间:", size=(9, 1)), sg.Input("", key="first")],
                [
                    sg.Text("", size=(9, 1)),
                    sg.Input("", key="second"),
                    sg.ReadButton("现在"),
                ],
                [sg.Text("", size=(9, 1)), sg.Input("", key="third")],
            ],
        )
    ],
    [
        sg.Frame(
            "案件类别",
            [
                [
                    sg.Radio("乱设摊", "type", default=False, size=(10, 1)),
                    sg.Radio("跨门经营", "type", default=False, size=(10, 1)),
                    sg.Radio("损毁承重结构", "type", default=False, size=(10, 1)),
                ],
                [
                    sg.Radio("居改非", "type", default=False, size=(10, 1)),
                    sg.Radio("夜间施工", "type", default=False, size=(10, 1)),
                    sg.Radio("占绿毁绿", "type", default=False, size=(10, 1)),
                ],
                [
                    sg.Radio("广告设施", "type", default=False, size=(10, 1)),
                    sg.Radio("油烟", "type", default=False, size=(10, 1)),
                    sg.Radio("出租车类", "type", default=False, size=(10, 1)),
                ],
                [
                    sg.Radio("非法客运类", "type", default=False, size=(10, 1)),
                    sg.Radio("其他", "type", default=False, size=(10, 1)),
                ],
            ],
        )
    ],
    [
        sg.Frame(
            "所属小队",
            [
                [
                    sg.Radio("一小队", "team", default=False, size=(10, 1), key="team"),
                    sg.Radio("二小队", "team", default=False, size=(10, 1), key="team"),
                    sg.Radio("三小队", "team", default=False, size=(10, 1), key="team"),
                ],
                [
                    sg.Radio("四小队", "team", default=False, size=(10, 1)),
                    sg.Radio("机动队", "team", default=False, size=(10, 1)),
                    sg.Radio("保安处置", "team", default=False, size=(10, 1)),
                ],
                [sg.Radio("其他", "team", default=False, size=(10, 1))],
            ],
        )
    ],
    [sg.ReadButton("提交")],
]

window = sg.Window("投诉登记").Layout(layout)


# def submit(values_dict):
#     if "数据必填项ok":
#         if not FILENAME.exists():
#             with open(FILENAME, "w", encoding="gb2312", newline="") as fp:
#                 fieldnames = ["单号", "联系时间", "案件类别", "所属小队"]
#                 writer = csv.DictWriter(fp, fieldnames=fieldnames)
#                 writer.writeheader()
#                 writer.writerow(
#                     {
#                         "单号": values_dict.get('id'),
#                         "联系时间": values_dict.get('first'),
#                         "案件类别": values_dict.get(),
#                         "所属小队": values_dict.get(),
#                     }
#                 )
#         else:
#             with open(FILENAME, "a", encoding="gb2312", newline="") as fp:
#                 fieldnames = ["单号", "联系时间", "案件类别", "所属小队"]
#                 writer = csv.DictWriter(fp, fieldnames=fieldnames)
#                 writer.writerow(
#                     {
#                         "单号": form_id.get(),
#                         "联系时间": create_datetime,
#                         "案件类别": classification.get(),
#                         "所属小队": team.get(),
#                     }
#                 )
#         # id_history.insert(tk.END, form_id.get())
#         showinfo("提交信息", "已经提交!")
#         print(form_id.get(), create_datetime.get(), classification.get(), team.get())
#     else:
#         miss_obj = [
#             k
#             for k, v in {
#                 "单号": form_id.get(),
#                 "联系时间": create_datetime.get(),
#                 "案件类别": classification.get(),
#                 "所属小队": team.get(),
#             }.items()
#             if not v
#         ]
#         err_msg = ",".join(miss_obj)
#         showerror("错误", err_msg + "没有填写。")


while 1:
    button, values = window.ReadNonBlocking()

    if button == "现在":
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        if not values["first"]:
            window.FindElement("first").Update(now)
        elif not values["second"]:
            window.FindElement("second").Update(now)
        else:
            window.FindElement("third").Update(now)
    elif button == "提交":
        sg.Popup("提交成功", values)

