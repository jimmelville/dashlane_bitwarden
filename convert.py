import csv

class BitwardenCredential:
    def __init__(self, folder,favorite,type,name,notes,fields,reprompt,login_uri,login_username,login_password,login_totp):
        self.folder = folder
        self.favorite = favorite
        self.type = type
        self.name = name
        self.notes = notes
        self.fields = fields
        self.reprompt = reprompt
        self.login_uri = login_uri
        self.login_username = login_username
        self.login_password = login_password
        self.login_totp = login_totp


class DashlaneCredential:
    def __init__(self, username, username2, username3, title, password, note, url, category, otpSecret):
        self.username = username
        self.username2 = username2
        self.username3 = username3
        self.title = title
        self.password = password
        self.note = note
        self.url = url
        self.category = category
        self.optSecret = otpSecret

    def asBitwarden(self):

        fields = ""
        if self.username2:
            fields += f"username2: {self.username2}"
        if self.username3:
            fields += f"username3: {self.username3}"

        return BitwardenCredential(self.category,
                                   0,
                                   'login',
                                   self.title,
                                   self.note,
                                   fields,
                                   0,
                                   self.url,
                                   self.username,
                                   self.password,
                                   self.optSecret)

dashlane_creds = []

with open('credentials.csv', newline='', encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        dashlane_creds.append(DashlaneCredential(row['username'], 
                                                 row['username2'], 
                                                 row['username3'],
                                                 row['title'],
                                                 row['password'], 
                                                 row['note'], 
                                                 row['url'], 
                                                 row['category'], 
                                                 row['otpSecret']))

bitwarden_creds = [cred.asBitwarden() for cred in dashlane_creds]

for bw_cred in bitwarden_creds:
    print (f"title: {bw_cred.name}")







        
    