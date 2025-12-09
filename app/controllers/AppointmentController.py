from flask import Flask, render_template


class AppointmentController:

    def index(self):
        return render_template("appointment.html", page="Đặt lịch sửa xe")
