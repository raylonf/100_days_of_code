from data_uteis import FILE_SERVICE_ACCOUNT, LINK_SHEETS_URL
import gspread


class User:

    def __init__(self):
        gc = gspread.service_account(filename=FILE_SERVICE_ACCOUNT)
        list_sheets = gc.open_by_url(url=LINK_SHEETS_URL)
        self.list_user = list_sheets.worksheet('users')
        self.firstName = ''
        self.lastName = ''
        self.email = ''

    def cadastro_user(self, firstName, lastName, email):
        if self.check_exist(email):
            cadastro = [firstName, lastName, email]
            self.list_user.append_row(cadastro)
            self.firstName = firstName,
            self.lastName = lastName,
            self.email = email


    def check_exist(self, email):
        check = True
        if self.list_user.row_count < 1:
            check = True
        else:
            for user in self.list_user.get():
                if email in user:
                    check = False
        return check

    def get_all_user(self):
        lista = self.list_user.get()
        return lista[1:]



if __name__ == '__main__':
    new = User()
    new.cadastro_user(firstName='Luana', lastName='Machado', email='luanamoara@hotmail.com')
    print(new.get_all_user())





