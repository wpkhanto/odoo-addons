[![Build Status](https://runbot.odoo.com/runbot/badge/flat/1/master.svg)](https://runbot.odoo.com/runbot)
[![Tech Doc](https://img.shields.io/badge/master-docs-875A7B.svg?style=flat&colorA=8F8F8F)](https://www.odoo.com/documentation/17.0)
[![Help](https://img.shields.io/badge/master-help-875A7B.svg?style=flat&colorA=8F8F8F)](https://www.odoo.com/forum/help-1)
[![Nightly Builds](https://img.shields.io/badge/master-nightly-875A7B.svg?style=flat&colorA=8F8F8F)](https://nightly.odoo.com/)

ขั้นตอนการ run odoo by source code
--------------------------------

1. Activate venv หลังจากนั้นติดตั้ง Library
```bash
pip install -r requirements.txt
```
2. เมื่อติดตั้งขั้นตอนที่ 1 เสร็จแล้วให้ Compile Odoo จาก Source Code
```bash
python setup.py install
```
3. เมื่อติดตั้งขั้นตอนที่ 2 เรียบร้อยแล้วจะปรากฏ Folder `build` ขึ้นมา
4. เปิดการทำงาน Odoo Server โดยใช้คำสั่ง
```bash
python build/scripts-3.12/odoo -r openpg -w openpgpwd
```
* `scripts-3.12` อ้างอิงจากใน Folder Build
* โดย Options `-r` จะเป็นชื่อผู้ใช้ฐานข้อมูล
* ส่วน `-w` คือรหัสผ่านฐานข้อมูล PostgreSQL