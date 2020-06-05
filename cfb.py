import mechanize, time
import os

os.system('clear')
banner = """

\033[1;32m __         __      
\033[1;32m/  \.-'''-./  \           \033[1;36m[\033[1;30m#\033[1;36m] \033[1;31mSpammer \033[1;33mComment \033[0;35mFacebook \033[1;36m[\033[1;30m#\033[1;36m]
\033[1;32m\    -   -    /     
\033[1;32m |   o   o   |                    \033[1;34mAuthor \033[1;37m: \033[1;36mMrCimin
\033[1;32m \  .-'''-.  /           \033[1;34mGithub \033[1;37m: \033[1;36mhttps://github.com/MrCimin
\033[1;32m  '-\__Y__/-'               \033[1;34mEmail \033[1;37m: \033[1;36mskyla_term@yopmail.com
\033[1;32m     `---`          

"""
print(banner)
br = mechanize.Browser()
br.set_handle_robots(False)

kuki = input("\033[1;32m[\033[1;36m#\033[1;32m] \033[1;33mYour Facebook Cookies \033[1;37m: \033[0;35m")
br.addheaders = []
br.addheaders.append(("User-Agent", "Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/71.0.3578.99 Mobile Safari/537.36"))
br.addheaders.append(("cookie", kuki))

if "mbasic_logout_button" in br.open("https://mbasic.facebook.com").read().decode():
  print("\033[1;31m[\033[1;33m☆\033[1;31m] \033[0;35mlogin \033[1;34msukses")
else:
  print("\033[1;37m[\033[1;31m!\033[1;37m] \033[1;33mCookies Tidak Valid")

for _ in range(20):
  print("\033[1;32m[\033[1;31m×\033[1;32m] \033[1;36mEx : https://mbasic.facebook.com/photo.php?fbid=166694224710808&id=100041106940465")
  url = input("\033[1;36m[\033[0;35m?\033[1;36m] \033[1;30mUrl to post (use mbasic)\033[1;37m: \033[1;36m")
  try:
    if not "https://mbasic.facebook.com":
      raise Exception
    html = br.open(url).read().decode()
    if "Konten Tidak Ditemukan" in html:
      raise Exception
    break
  except:
    print("\033[1;32m[\033[1;31m!\033[1;32m] \033[1;31mUrl tidak valid/Post tidak di temukan")
else:
  exit("\033[1;31m[!] Dah Lah")

text = input("\033[1;37m[\033[1;34m?\033[1;37m] \033[1;32mIsi Komentar \033[1;37m: \033[1;30m")
for _ in range(int(input("\033[1;32m[\033[1;36m?\033[1;32m] \033[1;34mJumlah Komentar \033[1;37m: \033[1;36m"))):
  br.open(url)
  br.select_form(nr=0)
  br["comment_text"] = text
  br.submit()
  print("Ok")
  time.sleep(1.1)
