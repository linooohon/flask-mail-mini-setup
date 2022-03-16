# Sendgrid / Gmail Config for Flask App Demo(Email 設定)
### Blog 紀錄可參考此:
[linooohon.com/blog - Flask: Sendgrid/Gmail <三種寄信設定>](https://linooohon.com/blog/posts/21/220316/Flask_Email_Setting_%E4%B8%89%E7%A8%AE%E5%AF%84%E4%BF%A1%E8%A8%AD%E5%AE%9A/)


### Step:
1. Clone this repo.
2. `pip install -r requirements.txt`
3. `source ./venv/bin/activate`
4. Setting your "`.env` file", "Sendgrid Secret Key".
5. Execute file:
   - `python gmail_mailman.py`
   - `python sendgrid_mailman.py`
   - `python sendgrid_webapi.py`

### References:

- Sendgrid:
  - https://github.com/sendgrid/sendgrid-python#with-mail-helper-class
  - https://github.com/sendgrid/sendgrid-python/blob/main/sendgrid/helpers/mail/mail.py
  - https://stackoverflow.com/questions/43240050/simple-way-to-send-an-html-text-email-using-sendgrid-python

- flask_mailman
  - https://www.waynerv.com/flask-mailman/
