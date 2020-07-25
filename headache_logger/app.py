# app.py
import datetime
from datetime import timedelta
from flask import Flask, render_template  # importing the render_template function

app = Flask(__name__)


# home route
@app.route("/")
def form():
    return common(None)


@app.route('/form-handler', methods=['POST'])
def handle_data():
   return common("Headache meditation logged. Hope you feel better soon!")

def common(message):
    f = open("head_log.csv", "r")
    log_lines = f.readlines()
    f.close()
    h_dates = get_hdates(log_lines)
    log_head()
    longest = longest_streak(log_lines)
    last_taken = last(log_lines)
    labels = get_labels()
    data = get_data(h_dates)
    if message:
        return render_template('form.html', message=message, last=last_taken, longest=longest, labels=labels, data=data)
    else:
        return render_template('form.html', last=last_taken, longest=longest, labels=labels, data=data)


def get_hdates(log_lines):
    hdates = []
    for log_line in log_lines:
        log_line = log_line.strip()
        dt = datetime.datetime.strptime(log_line, "%b %d %Y")
        hdates.append(dt)
    return hdates


def get_data(date_list):
    data = []
    delta = datetime.timedelta(days=1)
    now_dt = datetime.datetime.now()
    for day_offset in range(6, -1, -1):
        count = 0
        data_date = now_dt - delta * day_offset
        for date in date_list:
            if date.toordinal() == data_date.toordinal():
                count += 1
        data.append(count)
    return data


def get_labels():
    cd = datetime.datetime.now()
    delta = datetime.timedelta(days=1)
    labels = []
    for x in range(6, -1, -1):
        label_date = cd - delta * x
        labels.append(label_date.strftime("%b %d"))

    return labels


def log_head():
    x = datetime.datetime.now()
    head_time = (x.strftime("%b %d %Y"))
    message = f"{head_time}\n"
    f = open("head_log.csv", "a")
    f.write(message)
    f.close()
    #print("Headache medication taken logged. Hope you feel better soon!")


def head_log(log_lines):
    for log_line in log_lines:
        print(log_line)


def last_datetime(log_lines):
    index = len(log_lines) - 1
    if index == -1:
        return None
    last_line = log_lines[index]
    last_line = last_line.strip()
    last_taken_datetime = datetime.datetime.strptime(last_line, "%b %d %Y")  # datetime
    return last_taken_datetime


def last(log_lines):
    now = datetime.datetime.now()
    last_dt = last_datetime(log_lines)
    if last_dt is None:
        print("You haven't recorded taking headache medication.")
    else:
        diff = now - last_dt  # TimeDelta
        days = diff.days
        last_taken_pretty = last_dt.strftime("%b %d")
        print(f"{days} days ago, {last_taken_pretty}")
        return days


def longest_streak(log_lines):
    top_streak = 0
    for i in range(0, len(log_lines) - 1):
        thing1 = datetime.datetime.strptime(log_lines[i].strip(), "%b %d %Y")
        thing2 = datetime.datetime.strptime(log_lines[i + 1].strip(), "%b %d %Y")
        diff = thing2 - thing1
        days = diff.days
        if days - 1 > top_streak:
            top_streak = days - 1
        # print(days)

    # Get streak now
    last_dt = last_datetime(log_lines)
    if last_dt is None:
        print("You haven't recorded taking headache medication.")
    else:
        now = datetime.datetime.now()
        diff = now - last_dt  # TimeDelta
        days = diff.days
        if days - 1 > top_streak:
            top_streak = days - 1

        print(top_streak)
    return top_streak


app.run(debug=True)
