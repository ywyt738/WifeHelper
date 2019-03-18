import csv
import datetime
import logging
import math
import pathlib

import PySimpleGUI as sg
import sentry_sdk

sentry_sdk.init("https://23d1c3732bd540b29ccc56ba6306e97a@sentry.io/1300892")

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s][行号:%(lineno)d] %(message)s",
    datefmt="%Y/%m/%d %H:%M:%S",
    filename="WifeHelper.log",
    filemode="a",
)

VERSION = "1.0"
FILENAME = pathlib.Path("接单.csv")
CASE_TYPE = [
    "乱设摊",
    "跨门经营",
    "损毁承重结构",
    "居改非",
    "夜间施工",
    "占绿毁绿",
    "广告设施",
    "环保",
    "出租车类",
    "非法客运类",
    "其他类别",
]
TEAM = ["一小队", "二小队", "三小队", "四小队", "机动队", "保安处置", "其他"]

sg.SetOptions(font=14)

layout = [
    [
        sg.Frame(
            "案件信息",
            [
                [sg.Text("单号:", size=(9, 1)), sg.Input("", key="case_id")],
                [
                    sg.Text("联系时间:", size=(9, 1)),
                    sg.Input("", key="first"),
                    sg.ReadButton("现在"),
                ],
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
                        size=(12, 1),
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
                    sg.Radio(TEAM[i], "team", default=False, size=(10, 1), key=TEAM[i])
                    for i in range(4 * x, 4 * x + 4)
                    if i < len(TEAM)
                ]
                for x in range(math.ceil(len(TEAM) / 4))
            ],
        )
    ],
    [sg.ReadButton("提交")],
]


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


def get_data():
    case_id = values.get("case_id")
    contract_time1 = values.get("first")
    _tmp_d = {k: v for k, v in values.items() if v is True}
    for k in _tmp_d:
        if k in CASE_TYPE:
            case_type = k
        if k in TEAM:
            team = k
    return {
        "case_id": case_id,
        "contract_time1": contract_time1,
        "case_type": case_type,
        "team": team,
    }


def set_now():
    now = datetime.datetime.now().strftime("%F %H:%M")
    if not values["first"]:
        window.FindElement("first").Update(now)
    else:
        now = values["first"] + " " + now
        window.FindElement("first").Update(now)
    window.FindElement("case_id").Update(values["case_id"])


window = sg.Window("投诉登记 " + VERSION).Layout(layout)

while True:
    button, values = window.Read()
    logging.debug("ACTION:%s\nVALUES:%s", button, values)
    if button is None:
        break
    if button == "现在":
        set_now()
    elif button == "提交":
        data = get_data()
        if not data.get("case_id"):
            sg.Popup("ID为必填项", non_blocking=True)
            continue
        if not data["contract_time1"]:
            sg.Popup("联系时间至少填写一个!", non_blocking=True)
            window.FindElement("case_id").Update(values["case_id"])
            continue
        try:
            write_into_cvs(data)
        except PermissionError as e:
            sg.PopupError('请关闭"接单.csv"!', non_blocking=True)
        else:
            sg.PopupOK("提交成功!", non_blocking=True)
