import datetime
import pathlib
import math
import csv

import PySimpleGUI as sg

FILENAME = pathlib.Path("接单.csv")
CASE_TYPE = [
    "乱设摊",
    "跨门经营",
    "损毁承重结构",
    "居改非",
    "夜间施工",
    "占绿毁绿",
    "广告设施",
    "油烟",
    "出租车类",
    "非法客运类",
    "其他",
]
TEAM = ["一小队", "二小队", "三小队", "四小队", "机动队", "保安处置", "其他"]

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
                    sg.Radio(
                        CASE_TYPE[i],
                        "type",
                        default=False,
                        size=(10, 1),
                        key=CASE_TYPE[i],
                    )
                    for i in range(4 * x, 4 * x + 4)
                    if i < len(CASE_TYPE)
                ]
                for x in range(math.ceil(len(CASE_TYPE) / 4))
            ],
        )
    ],
    [
        sg.Frame(
            "所属小队",
            [
                [
                    sg.Radio(TEAM[i], "type", default=False, size=(10, 1), key=TEAM[i])
                    for i in range(4 * x, 4 * x + 4)
                    if i < len(TEAM)
                ]
                for x in range(math.ceil(len(TEAM) / 4))
            ],
        )
    ],
    [sg.ReadButton("提交")],
]

window = sg.Window("投诉登记").Layout(layout)


def write_into_cvs(data):
    if not FILENAME.exists():
        with open(FILENAME, "w", encoding="gb2312", newline="") as fp:
            fieldnames = ["单号", "联系时间", "案件类别", "所属小队"]
            writer = csv.DictWriter(fp, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow(
                {
                    "单号": data.get("case_id"),
                    "联系时间": data.get("contract_time1"),
                    "案件类别": data.get("case_type"),
                    "所属小队": data.get("team"),
                }
            )
    else:
        with open(FILENAME, "a", encoding="gb2312", newline="") as fp:
            fieldnames = ["单号", "联系时间", "案件类别", "所属小队"]
            writer = csv.DictWriter(fp, fieldnames=fieldnames)
            writer.writerow(
                {
                    "单号": data.get("case_id"),
                    "联系时间": data.get("contract_time1"),
                    "案件类别": data.get("case_type"),
                    "所属小队": data.get("team"),
                }
            )


def get_data(values):
    case_id = values.get("id")
    contract_time1 = values.get("first")
    contract_time2 = values.get("second")
    contract_time3 = values.get("third")
    _tmp_d = {k: v for k, v in values.items() if v is True}
    for k in _tmp_d:
        if k in CASE_TYPE:
            case_type = k
        if k in TEAM:
            team = k
    return {
        "case_id": case_id,
        "contract_time1": contract_time1,
        "contract_time2": contract_time2,
        "contract_time3": contract_time3,
        "case_type": case_type,
        "team": team,
    }


def set_now():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    if not values["first"]:
        window.FindElement("first").Update(now)
    elif not values["second"]:
        window.FindElement("second").Update(now)
    else:
        window.FindElement("third").Update(now)


while 1:
    button, values = window.ReadNonBlocking()

    if button == "现在":
        set_now()
    elif button == "提交":
        data = get_data(values)
        if not data.get("case_id"):
            sg.PopupError("ID为必填项")
        if any(
            [data["contract_time1"], data["contract_time2"], data["contract_time3"]]
        ):
            pass
        else:
            sg.PopupError("联系时间至少填写一个!")
        write_into_cvs(data)
        sg.PopupOK("提交成功!")
