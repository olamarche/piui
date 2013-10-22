import functools
import os
import random
import time
import sqlite3 as lite
import sys
from servo import Servo
from piui import PiUi

current_dir = os.path.dirname(os.path.abspath(__file__))


class CatFeeder(object):

    def __init__(self):
        servo = Servo()
        self.title = None
        self.txt = None
        self.img = None
        self.ui = PiUi(img_dir=os.path.join(current_dir, 'imgs'))

    def main(self):
        self.main_menu()
        self.ui.done()

    def main_menu(self):
        self.page = self.ui.new_ui_page(title="Cat Feeder")
        self.page.add_element("hr")
        self.list = self.page.add_list()
        self.list.add_item("Nourrir", chevron=True, onclick=self.page_control)
        self.list.add_item("Journal", chevron=True, onclick=self.page_feed_logs)
        self.ui.done()

    def page_control(self):
        self.page = self.ui.new_ui_page(title="Nourrir", prev_text="<", onprevclick=self.main_menu)
        self.title = self.page.add_textbox("Control", "h1")
        plus = self.page.add_button("Ouvrir la trap", self.onupclick)
        minus = self.page.add_button("Fermer la trap", self.ondownclick)

    def page_feed_logs(self):
        self.page.add_textbox("Journal", "h1")
        self.page.add_element("hr")
        con = lite.connect('catfeeder.db')
        with con:
            
            cur = con.cursor()    
            cur.execute("SELECT * FROM feedLogs")

            rows = cur.fetchall()

            for row in rows:
                self.page.add_textbox(row, "p")

    def onupclick(self):
        self.title.set_text("Up ")
        servo.servo_CW(1200)

    def ondownclick(self):
        self.title.set_text("Down")
        servo.servo_CCW(2000)

def main():
  piui = CatFeeder()
  piui.main()

if __name__ == '__main__':
    main()